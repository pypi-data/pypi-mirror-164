# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class QRCode(Component):
    """A QRCode component.
    A Dash component for reading QR codes from an attached webcam.

    Keyword arguments:

    - id (string; optional):
        The ID used to identify this compnent in Dash callbacks.

    - result (string; optional):
        Prop that will contain the result.

    - scanDelay (number; default 2000):
        Delay for the scanning in ms.

    - status (string; default 'idle'):
        Contains the status of the renderer."""

    _children_props = []
    _base_nodes = ["children"]
    _namespace = "dash_qrcode"
    _type = "QRCode"

    @_explicitize_args
    def __init__(
        self,
        id=Component.UNDEFINED,
        scanDelay=Component.UNDEFINED,
        result=Component.UNDEFINED,
        status=Component.UNDEFINED,
        **kwargs
    ):
        self._prop_names = ["id", "result", "scanDelay", "status"]
        self._valid_wildcard_attributes = []
        self.available_properties = ["id", "result", "scanDelay", "status"]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != "children"}
        for k in []:
            if k not in args:
                raise TypeError("Required argument `" + k + "` was not specified.")
        super(QRCode, self).__init__(**args)
