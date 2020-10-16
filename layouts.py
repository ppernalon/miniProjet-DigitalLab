#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


def layout_generator():
    layout = \
        html.Div([
            html.Div(
                id="radio-method",
                children=[
                    html.H5("Nombre de variables sélectionnées"),
                    dcc.RadioItems(
                        id="choix-method",
                        options=[
                            {'label': 'monovariable', 'value': 'monovariable'},
                            {'label': 'multivariable', 'value': 'multivariable'},
                        ],
                        value='monovariable',
                        labelStyle={'display': 'inline-block'}
                    ),
                ]
            ),

            html.Div(
                id="div_mono",
                children=[],
            ),

            html.Div(
                id='div_multi',
                children=[],
            )
        ])
    return layout

