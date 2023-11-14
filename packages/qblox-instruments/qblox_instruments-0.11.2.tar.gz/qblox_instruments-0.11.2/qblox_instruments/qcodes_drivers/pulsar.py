# --------------------------------------------------------------------------
# Description    : Pulsar QCoDeS interface
# Git repository : https://gitlab.com/qblox/packages/software/qblox_instruments.git
# Copyright (C) Qblox BV (2020)
# --------------------------------------------------------------------------


# -- include -----------------------------------------------------------------

from typing import Any, Callable, List, Optional, Union
from qcodes import Instrument, InstrumentChannel, Parameter
from qcodes import validators as vals
from qblox_instruments import PulsarType
from qblox_instruments.native import Pulsar as PulsarNative
from qblox_instruments.qcodes_drivers.qcm_qrm import add_qcodes_params, invalidate_qcodes_parameter_cache, get_item


# -- class -------------------------------------------------------------------

class Pulsar(PulsarNative, Instrument):
    """
    This class connects `QCoDeS <https://qcodes.github.io/Qcodes/>`_ to the
    Pulsar native interface.
    """

    # ------------------------------------------------------------------------
    def __init__(
        self,
        name: str,
        identifier: Optional[str] = None,
        port: Optional[int] = None,
        debug: Optional[int] = None,
        dummy_type: Optional[PulsarType] = None,
    ):
        """
        Creates Pulsar QCoDeS class and adds all relevant instrument
        parameters. These instrument parameters call the associated methods
        provided by the native interface.

        Parameters
        ----------
        name : str
            Instrument name.
        identifier : Optional[str]
            Instrument identifier. See :func:`~qblox_instruments.resolve()`.
            If None, the instrument is identified by name.
        port : Optional[int]
            Override for the TCP port through which we should connect.
        debug : Optional[int]
            Debug level (0 | None = normal, 1 = no version check, >1 = no
            version or error checking).
        dummy_type : Optional[PulsarType]
            Configure as dummy module of specified type.

        Returns
        ----------

        Raises
        ----------
        """

        # Initialize parent classes.
        if identifier is None:
            identifier = name
        super().__init__(identifier, port, debug, dummy_type)
        Instrument.__init__(self, name)

        # Add QCoDeS parameters
        add_qcodes_params(self, num_seq=6)

        self.add_parameter(
            "led_brightness",
            label="LED brightness",
            docstring="Sets/gets frontpanel LED brightness.",
            unit="",
            vals=vals.Strings(),
            val_mapping={"off": "OFF", "low": "LOW", "medium": "MEDIUM", "high": "HIGH"},
            set_parser=str,
            get_parser=str,
            set_cmd=self._set_led_brightness,
            get_cmd=self._get_led_brightness,
        )

        self.add_parameter(
            "reference_source",
            label="Reference source",
            docstring="Sets/gets reference source ('internal' = internal "
                      "10 MHz, 'external' = external 10 MHz).",
            unit="",
            vals=vals.Bool(),
            val_mapping={"internal": True, "external": False},
            set_parser=bool,
            get_parser=bool,
            set_cmd=self._set_reference_source,
            get_cmd=self._get_reference_source,
        )

        self.add_parameter(
            "ext_trigger_input_delay",
            label="Trigger input delay.",
            docstring="Sets/gets the input delay of the external input trigger. "
                    "This parameter can be used to delay the external trigger and "
                    "move it out of the setup/hold time of the instruments system "
                    "clock.",
            unit="ps",
            vals=vals.Multiples(39, min_value=0, max_value=31*39),
            set_parser=int,
            get_parser=int,
            set_cmd=self.set_trg_in_delay,
            get_cmd=self.get_trg_in_delay,
        )

        self.add_parameter(
            "ext_trigger_input_trigger_en",
            label="Trigger input enable.",
            docstring="Enable/disable the external input trigger.",
            unit="",
            vals=vals.Bool(),
            set_parser=bool,
            get_parser=bool,
            set_cmd=self.set_trg_in_map_en,
            get_cmd=self.get_trg_in_map_en,
        )

        self.add_parameter(
            "ext_trigger_input_trigger_address",
            label="Trigger address.",
            docstring="Sets/gets the trigger address to which the external input"
                      "trigger is mapped to the trigger network (T1 to T15).",
            unit="",
            vals=vals.Numbers(1,15),
            set_parser=int,
            get_parser=int,
            set_cmd=self.set_trg_in_map_addr,
            get_cmd=self.get_trg_in_map_addr,
        )

    # ------------------------------------------------------------------------
    @property
    def sequencers(self) -> List:
        """
        Get list of sequencers submodules.

        Parameters
        ----------

        Returns
        ----------
        list
            List of sequencer submodules.

        Raises
        ----------
        """

        return list(self.submodules.values())

    # ------------------------------------------------------------------------
    def reset(self) -> None:
        """
        Resets device, invalidates QCoDeS parameter cache and clears all
        status and event registers (see
        `SCPI <https://www.ivifoundation.org/docs/scpi-99.pdf>`_).

        Parameters
        ----------

        Returns
        ----------

        Raises
        ----------
        """

        self._reset()
        self._invalidate_qcodes_parameter_cache()

    # ------------------------------------------------------------------------
    def disconnect_outputs(self) -> None:
        """
        Disconnects all outputs from the waveform generator paths of the
        sequencers.

        Parameters
        ----------

        Returns
        ----------

        Raises
        ----------
        """

        self._disconnect_outputs()
        self._invalidate_qcodes_parameter_cache()

    # ------------------------------------------------------------------------
    def disconnect_inputs(self) -> None:
        """
        Disconnects all inputs from the acquisition paths of the sequencers.

        Parameters
        ----------

        Returns
        ----------

        Raises
        ----------
        """

        self._disconnect_inputs()
        self._invalidate_qcodes_parameter_cache()

    # ------------------------------------------------------------------------
    def connect_sequencer(self, sequencer: int, *connections: str) -> None:
        """
        Makes new connections between the indexed sequencer and some inputs
        and/or outputs. This will fail if a requested connection already
        existed, or if the connection could not be made due to a conflict with
        an existing connection (hardware constraints). In such a case, the
        channel map will not be affected.

        Parameters
        ----------
        sequencer : int
            Sequencer index
        *connections : str
            Zero or more connections to make, each specified using a string.
            The string should have the format `<direction><channel>` or
            `<direction><I-channel>_<Q-channel>`. `<direction>` must be `in`
            to make a connection between an input and the acquisition path,
            `out` to make a connection from the waveform generator to an
            output, or `io` to do both. The channels must be integer channel
            indices. If only one channel is specified, the sequencer operates
            in real mode; if two channels are specified, it operates in complex
            mode.

        Returns
        ----------

        Raises
        ----------
        RuntimeError
            If the connection command could not be completed due to a conflict.
        ValueError
            If parsing of a connection fails.
        """

        self._sequencer_connect(sequencer, *connections)
        self._invalidate_qcodes_parameter_cache(sequencer)

    # ------------------------------------------------------------------------
    def _invalidate_qcodes_parameter_cache(
        self,
        sequencer: Optional[int]=None
    ) -> None:
        """
        Marks the cache of all QCoDeS parameters in the module, including in
        any sequencers the module might have, as invalid. Optionally,
        a sequencer can be specified. This will invalidate the cache of that
        sequencer only in stead of all parameters.

        Parameters
        ----------
        sequencer : Optional[int]
            Sequencer index of sequencer for which to invalidate the QCoDeS
            parameters.

        Returns
        ----------

        Raises
        ----------
        """

        # Invalidate instrument parameters
        if sequencer is None:
            for param in self.parameters.values():
                param.cache.invalidate()

        # Invalidate module parameters
        invalidate_qcodes_parameter_cache(self, sequencer)

    # ------------------------------------------------------------------------
    def __getitem__(
        self,
        key: str
    ) -> Union[InstrumentChannel, Parameter, Callable[..., Any]]:
        """
        Get sequencer or parameter using string based lookup.

        Parameters
        ----------
        key : str
            Sequencer, parameter or function to retrieve.

        Returns
        ----------
        Union[InstrumentChannel, Parameter, Callable[..., Any]]
            Sequencer, parameter or function.

        Raises
        ----------
        KeyError
            Sequencer, parameter or function does not exist.
        """

        return get_item(self, key)

    # ------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Returns simplified representation of class giving just the class,
        name and connection.

        Parameters
        ----------

        Returns
        ----------
        str
            String representation of class.

        Raises
        ----------
        """

        loc_str = ""
        if hasattr(self._transport, "_socket"):
            address, port = self._transport._socket.getpeername()
            loc_str = f" at {address}:{port}"
        return f"<{type(self).__name__}: {self.name}" + loc_str + ">"
