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
        html.Div(dash_qrcode.QRCode(id="qr-input", scanDelay=1000), style={"width": "300px"}),
        html.P(id="output"),
        html.P(id="all-output"),
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


@app.callback(
    Output("output", "children"),
    Output("all-output", "children"),
    Input("qr-input", "result"),
    State("all-output", "children"),
)
def get_qr_result(result: str | None, all_output) -> tuple[str, str]:
    if not all_output:
        all_output = ""
    if result:
        all_output += f"{result}, "
        return f"Scanned value: {result}", all_output
    return "", all_output


if __name__ == "__main__":
    app.run_server(debug=True)
