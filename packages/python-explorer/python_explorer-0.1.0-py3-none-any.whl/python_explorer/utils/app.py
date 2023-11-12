'''Primary app definition and utility.'''

import webbrowser
from pathlib import Path

from dash import Dash, html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from waitress import serve

# locals
from python_explorer.layouts import comp_id, page_layout, stores
from python_explorer.utils import callbacks

def serve_layout():
    return dmc.NotificationsProvider(
        html.Div(
            [
                html.Div(id=comp_id('notifier', 'app', 0)),
                page_layout,
                stores,  
            ],
            style={
                    'height':'100vh',
                    'width':'100vw',
                    'margin':'0',
                    'padding':'0',
                }
        ),
        position='top-right',
        autoClose=2200,
    )

app = Dash(
    __name__,
    assets_folder=Path(__file__).parent.parent/'assets',
    title='python-explorer',
    suppress_callback_exceptions=True,
)  

app.layout = serve_layout()

server = app.server   

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = '8080'
DEFAULT_THREADS = 8

def run_app(
    host: str = DEFAULT_HOST,
    port: str = DEFAULT_PORT,
    threads: int = DEFAULT_THREADS,
):
    site = f'http://{host}:{port}/'
    webbrowser.open(site)
    serve(server, host=host, port=port, threads=threads)