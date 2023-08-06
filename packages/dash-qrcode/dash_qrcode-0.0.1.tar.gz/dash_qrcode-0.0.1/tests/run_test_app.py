import dash
from dash import html
from dash.dependencies import Input, Output, State

import dash_qrcode

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P("Testing"),
        html.Br(),
        html.Div(html.Button("Start scanning", id="start-scanning-button")),
        html.Div(dash_qrcode.QRCode(id="qr-input"), style={"width": "300px"}),
        html.P(id="output"),
    ]
)


@app.callback(
    Output("qr-input", "status"),
    Output("start-scanning-button", "children"),
    Input("start-scanning-button", "n_clicks"),
    State("qr-input", "status"),
)
def start_scanning(n_clicks, scan_state) -> tuple[str, str]:
    if n_clicks:
        if scan_state != "reader":
            return "reader", "Stop"
    return "idle", "Start scanning"


@app.callback(Output("output", "children"), Input("qr-input", "result"))
def get_qr_result(result: str | None) -> str:
    if result:
        return f"Scanned value: {result}"
    return ""


if __name__ == "__main__":
    app.run_server(debug=True)
