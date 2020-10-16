#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


timesData = pd.read_csv("data/timesData.csv")
resultats = pd.read_csv('data/resultats.csv')


def layout_generator():
    layout = \
        html.Div([
            html.Div(
                id="radio-method",
                children=[
                    html.H5("choix des données sur l'axe x"),
                    dcc.RadioItems(
                        id="choix-method",
                        options=[
                            {'label': 'monovariable', 'value': 'monovariable'},
                            {'label': 'multivarible', 'value': 'multivarible'},
                        ],
                        value='monovariable',
                        labelStyle={'display': 'inline-block'}
                    ),
                ]
            ),

            dcc.Graph(
                id='plot',
                figure={}
            ),

            html.Div(id='id'),
        ])
    return layout

