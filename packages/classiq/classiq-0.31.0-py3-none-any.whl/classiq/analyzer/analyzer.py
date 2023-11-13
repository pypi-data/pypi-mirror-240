"""Analyzer module, implementing facilities for analyzing circuits using Classiq platform."""
import json
import webbrowser
from importlib.util import find_spec
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from urllib.parse import urljoin

import plotly.graph_objects as go

from classiq.interface.analyzer import analysis_params
from classiq.interface.analyzer.analysis_params import (
    AnalysisComparisonParams,
    ComparisonProperties,
)
from classiq.interface.backend.quantum_backend_providers import AnalyzerProviderVendor
from classiq.interface.generator import generated_circuit as generator_result
from classiq.interface.generator.model import Preferences, SynthesisModel as APIModel

from classiq import GeneratedCircuit
from classiq._internals import client
from classiq._internals.api_wrapper import ApiWrapper
from classiq._internals.async_utils import Asyncify
from classiq.analyzer.analyzer_utilities import (
    AnalyzerUtilities,
    DeviceName,
    HardwareGraphs,
    ProviderAvailableDevices,
    ProviderNameEnum,
)
from classiq.analyzer.url_utils import circuit_page_uri, client_ide_base_url
from classiq.exceptions import ClassiqAnalyzerError
from classiq.model.model import Model
from classiq.synthesis import synthesize_async

find_ipywidgets = find_spec("ipywidgets")
VBox = Any

if find_ipywidgets is not None:
    from ipywidgets import VBox  # type: ignore[import, no-redef]

    from classiq._analyzer_extras.interactive_hardware import InteractiveHardware


class Analyzer(AnalyzerUtilities, metaclass=Asyncify):
    """Analyzer is the wrapper object for all analysis capabilities."""

    def __init__(self, circuit: generator_result.GeneratedCircuit) -> None:
        """Init self.

        Args:
            circuit (): The circuit to be analyzed.
        """
        if circuit.qasm is None:
            raise ClassiqAnalyzerError(
                "Analysis requires a circuit with valid QASM code"
            )
        self._params: analysis_params.AnalysisParams = analysis_params.AnalysisParams(
            qasm=circuit.qasm
        )
        self.circuit: generator_result.GeneratedCircuit = circuit
        self.hardware_comparison_table: Optional[go.Figure] = None
        self.available_devices: ProviderAvailableDevices = dict()
        self.hardware_graphs: HardwareGraphs = dict()

        self.transpilation_params = analysis_params.AnalysisHardwareTranspilationParams(
            hardware_data=self.circuit.hardware_data,
            model_preferences=self.circuit.model.preferences,
        )

    async def analyzer_app_async(self) -> None:
        """Opens the analyzer app with synthesis interactive results.

        Returns:
            None.
        """
        result = await ApiWrapper.call_analyzer_app(self.circuit)
        webbrowser.open_new_tab(
            urljoin(
                client_ide_base_url(),
                circuit_page_uri(
                    circuit_id=result.id, circuit_version=self.circuit.version
                ),
            )
        )

    async def get_available_devices_async(
        self, providers: Optional[List[ProviderNameEnum]] = None
    ) -> Dict[ProviderNameEnum, List[DeviceName]]:
        """Returns dict of the available devices by the providers. only devices
        with sufficient number of qubits are returns

        Args: providers (): List of providers (string or `AnalyzerProviderVendor`).
        if None, the table include all the available hardware.

        Returns:
            available devices (): dict of the available devices (Dict[str,List[str]]).
        """
        if providers is None:
            providers = list(AnalyzerProviderVendor)
        await self.request_available_devices_async(providers=providers)
        return {
            provider: self._filter_devices_by_qubits_count(provider)
            for provider in providers
        }

    async def plot_hardware_connectivity_async(
        self,
        provider: Optional[ProviderNameEnum] = None,
        device: Optional[DeviceName] = None,
    ) -> VBox:
        """plot the hardware_connectivity graph. It is required to required  install the
        analyzer_sdk extra.

        Args:
            provider (): provider name (optional - string or `AnalyzerProviderVendor`).
            device (): device name (optional - string).
        Returns:
         hardware_connectivity_graph (): interactive graph.
        """

        self._validate_analyzer_extra()
        interactive_hardware = InteractiveHardware(
            circuit=self.circuit,
            params=self._params,
            available_devices=self.available_devices,
            hardware_graphs=self.hardware_graphs,
        )
        await interactive_hardware.enable_interactivity_async()
        if provider is not None:
            interactive_hardware.providers_combobox.value = provider
            if device is not None:
                interactive_hardware.devices_combobox.value = device

        return interactive_hardware.show_interactive_graph()

    async def get_hardware_comparison_table_async(
        self,
        providers: Optional[Sequence[Union[str, AnalyzerProviderVendor]]] = None,
        devices: Optional[List[str]] = None,
    ) -> None:
        """create a comparison table between the transpiled circuits result on different hardware.
        The  comparison table included the depth, multi qubit gates count,and total gates count of the circuits.

        Args: providers (): List of providers (string or `AnalyzerProviderVendor`). if None, the table include all
        the available hardware.
        devices (): List of devices (string). if None, the table include all the available devices of the selected
        providers.
        Returns: None.
        """
        if providers is None:
            providers = list(AnalyzerProviderVendor)
        params = analysis_params.AnalysisHardwareListParams(
            qasm=self._params.qasm,
            providers=providers,
            devices=devices,
            transpilation_params=self.transpilation_params,
        )
        result = await ApiWrapper.call_table_graphs_task(params=params)
        self.hardware_comparison_table = go.Figure(json.loads(result.details))

    async def plot_hardware_comparison_table_async(
        self,
        providers: Optional[List[Union[str, AnalyzerProviderVendor]]] = None,
        devices: Optional[List[str]] = None,
    ) -> None:
        """plot the comparison table. if it has not been created it, it first creates the table using all the
        available hardware.

        Returns:
            None.
        """
        await self._hardware_comparison_condition_async(
            providers=providers, devices=devices
        )
        self.hardware_comparison_table.show()  # type: ignore[union-attr]

    async def hardware_aware_resynthesize_async(
        self, device: str, provider: Union[str, AnalyzerProviderVendor]
    ) -> generator_result.GeneratedCircuit:
        """resynthesize the analyzed circuit using its original model, and a new  backend preferences.

        Args:
            provider (): Provider company or cloud for the requested backend (string or `AnalyzerProviderVendor`).
            device (): Name of the requested backend"
        Returns:
            circuit (): resynthesize circuit (`GeneratedCircuit`).
        """

        update_preferences = self._validated_update_preferences(
            device=device, provider=provider
        )

        model = Model()
        model._model = self.circuit.model.copy(deep=True)
        model._model.preferences = update_preferences
        return GeneratedCircuit.parse_raw(
            await synthesize_async(model._model.get_model())
        )

    async def optimized_hardware_resynthesize_async(
        self,
        comparison_property: Union[str, ComparisonProperties],
        providers: Optional[Sequence[Union[str, AnalyzerProviderVendor]]] = None,
        devices: Optional[List[str]] = None,
    ) -> generator_result.GeneratedCircuit:
        """Re-synthesize the analyzed circuit using its original model, and a new backend preferences, which is the
         devices with the best fit to the selected comparison property.

        Args: comparison_property (): A comparison properties using to compare between the devices (string or
        `ComparisonProperties`).
        providers (): List of providers (string or `AnalyzerProviderVendor`). If None, the comparison include all the
        available hardware.
        devices (): List of devices (string). If None, the comparison include all the available devices of the selected
        providers.
        Returns: circuit (): resynthesize circuit (`GeneratedCircuit`).
        """
        optimized_device, optimized_provider = await self._get_optimized_hardware_async(
            providers=providers,
            devices=devices,
            comparison_property=comparison_property,
        )
        return await self.hardware_aware_resynthesize_async(
            provider=optimized_provider, device=optimized_device
        )

    async def _get_optimized_hardware_async(
        self,
        comparison_property: Union[str, ComparisonProperties],
        providers: Optional[Sequence[Union[str, AnalyzerProviderVendor]]] = None,
        devices: Optional[List[str]] = None,
    ) -> Tuple[str, str]:
        await self._hardware_comparison_condition_async(
            providers=providers, devices=devices
        )
        optimized_device, optimized_provider = self._choose_optimized_hardware(
            comparison_property=comparison_property
        )
        return optimized_device, optimized_provider

    def _choose_optimized_hardware(
        self, comparison_property: Union[str, ComparisonProperties]
    ) -> Tuple[str, str]:
        comparison_params = AnalysisComparisonParams(property=comparison_property)
        if not isinstance(self.hardware_comparison_table, go.Figure):
            raise ClassiqAnalyzerError(
                "The analyzer does not contains a valid hardware comparison table"
            )
        column_names = self.hardware_comparison_table.data[0].header.values
        param = self._get_right_form_of_comparison_params(
            comparison_params=comparison_params
        )
        property_index = column_names.index(param)

        sort_button = self.hardware_comparison_table.layout.updatemenus[0]
        sort_data = sort_button.buttons[property_index].args[0]["cells"]["values"]
        return sort_data[0][0], sort_data[1][0]

    @staticmethod
    def _get_right_form_of_comparison_params(
        comparison_params: AnalysisComparisonParams,
    ) -> str:
        return comparison_params.property.upper().replace("_", " ")

    def _validated_update_preferences(
        self, device: str, provider: Union[str, AnalyzerProviderVendor]
    ) -> Preferences:
        if not isinstance(self.circuit.model, APIModel):
            raise ClassiqAnalyzerError("The circuit does not contains a valid model")

        preferences_dict = self.circuit.model.preferences.dict()
        preferences_dict.update(
            dict(backend_service_provider=provider, backend_name=device)
        )

        return Preferences.parse_obj(preferences_dict)

    async def _hardware_comparison_condition_async(
        self,
        providers: Optional[Sequence[Union[str, AnalyzerProviderVendor]]] = None,
        devices: Optional[List[str]] = None,
    ) -> None:
        if (
            providers is not None
            or devices is not None
            or self.hardware_comparison_table is None
        ):
            await self.get_hardware_comparison_table_async(
                providers=providers, devices=devices
            )

    @staticmethod
    def _open_route(path: str) -> None:
        backend_uri = client.client().get_backend_uri()
        webbrowser.open_new_tab(f"{backend_uri}{path}")

    @staticmethod
    def _validate_analyzer_extra() -> None:
        if find_ipywidgets is None:
            raise ClassiqAnalyzerError(
                "To use this method, please install the `analyzer sdk`. Run the  \
                following line: - pip install classiq[analyzer_sdk]"
            )
