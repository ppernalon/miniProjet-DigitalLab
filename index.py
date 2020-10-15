#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from layouts import layout_generator
import callbacks
import pandas as pd

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='menu',
             children=
             [
                dcc.Link('Voir les données de 2011 | ', href='/2011'),
                dcc.Link('Voir les données de 2012 | ', href='/2012'),
                dcc.Link('Voir les données de 2013 | ', href='/2013'),
                dcc.Link('Voir les données de 2014 | ', href='/2014'),
                dcc.Link('Voir les données de 2015 | ', href='/2015'),
                dcc.Link('Prediction des scores de 2016', href='/2016')
             ]),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return layout_generator()


if __name__ == '__main__':
    app.run_server(debug=True)
