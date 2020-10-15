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
                id="radio-x",
                children=[
                    html.H5("choix des données sur l'axe x"),
                    dcc.RadioItems(
                        id="choix-axis-x",
                        options=[
                            {'label': u'teaching', 'value': 'teaching'},
                            {'label': 'international', 'value': 'international'},
                            {'label': 'research', 'value': 'research'},
                            {'label': 'citations', 'value': 'citations'},
                            {'label': 'income', 'value': 'income'},
                            {'label': 'num_students', 'value': 'num_students'},
                            {'label': 'student_staff_ratio', 'value': 'student_staff_ratio'},
                            {'label': 'international_students', 'value': 'international_students'},
                            {'label': 'female_male_ratio', 'value': 'female_male_ratio'},
                        ],
                        value='female_male_ratio',
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

