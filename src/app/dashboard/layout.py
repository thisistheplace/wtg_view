from dash import html
import dash_bootstrap_components as dbc

from .tabs import banner, sidecol

def layout(tabs):
    """Defines the overall layout of the dashboard.

    The layouts of individual panels are defined in subpackages.

    Args:
        tabs: objects defining tabs

    Returns:
        dash.html.Div
    """
    return html.Div(
        children=[
            dbc.Offcanvas(
                sidecol.Sidecol().layout,
                id="sidebar-column",
                is_open=False,
            ),
            # Heading data
            banner.Banner().layout,
            dbc.Container(
                dbc.Row([
                    dbc.Col(
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    tab.layout,
                                    label=tab.name,
                                    label_style={
                                        "paddingLeft": "0.5rem",
                                        "paddingRight": "0.5rem"
                                    }
                                ) for tab in tabs]
                        ),
                        id="tabs-column"
                    )
                ])
            )
        ],
        style={
            "padding": "30px",
            "height": "100%",
        },
    )