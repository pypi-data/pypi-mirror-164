from dash.testing.application_runners import import_app


# Basic test for the component rendering.
# The dash_duo pytest fixture is installed with dash (v1.0+)
def test_render_component(dash_duo):
    # Start a dash app contained as the variable `app` in `usage.py`
    app = import_app("usage")
    dash_duo.start_server(app)

    # Get the generated component input with selenium
    # The html input will be a children of the #input dash component
    qr_component = dash_duo.find_element("#input > qr-input")

    assert qr_component.get_attribute("result") is None
    assert qr_component.get_attribute("status") == "idle"

    # Clear the input
    button_component = dash_duo.find_element("#input > start-scanning-button")
    assert qr_component.get_attribute("n_clicks") == 0
    # Send keys to the custom input.
    qr_component.click()

    # Wait for the text to equal, if after the timeout (default 10 seconds)
    # the text is not equal it will fail the test.
    dash_duo.wait_for_property_to_equal("#input > start-scanning_button", "status", "reading")
