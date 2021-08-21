# General imports
########################################################################################################################
import utils.flask_compress_fix  # Flask compress fix
from pathlib import Path
from datetime import date

# Dash imports
########################################################################################################################
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Define the app object #####
########################################################################################################################
app = dash.Dash(__name__)  # For offline use, the .css is stored in assets folder. assets/style.css

# Set up server using waitress (For robust local hosting and not using Dash development tools)
########################################################################################################################
server = app.server  # Added so that the app can be served using waitress.

# The dash app
#############################################################################################################

df = pd.read_csv("data/data.csv")

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

logo = html.Img(
    src=app.get_asset_url('plotly_image_cc_license.PNG'),  # Create a dash object for the logo
    style={'height': '80px',
           'float': 'middle',
           }
)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    logo
])


# Run the app on a server
########################################################################################################################
if __name__ == '__main__':
    # app.run_server(debug=True)  # When developing with Dash

    app.run_server(debug=False)  # For production deployment with waitress
