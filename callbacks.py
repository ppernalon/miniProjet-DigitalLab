#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

from app import app

timesData = pd.read_csv("data/timesData.csv")
resultats = pd.read_csv('data/resultats.csv')

@app.callback(
    Output('plot', 'figure'),
    [
        Input("choix-axis-x", 'value'),
        Input('url', 'pathname')
    ])
def update_graph(axis_x, pathname):
    if pathname in ['/2011', '/2012', '/2013', '/2014', '/2015']:
        if not('apps' in pathname):
            annee = 2011
        else:
            annee = int(pathname[-4:])
        dataFrame = timesData[timesData.year == annee].iloc[:50, :]
        fig = {'data': [go.Scatter(x=dataFrame[dataFrame['country'] == i][axis_x],
                                   y=dataFrame[dataFrame['country'] == i]["total_score"],
                                   text=dataFrame[dataFrame['country'] == i]['university_name'],
                                   mode='markers',
                                   opacity=0.8,
                                   marker={
                                       'size': 15,
                                       'line': {'width': 0.5, 'color': 'white'}
                                   },
                                   name=i
                                   ) for i in dataFrame.country.unique()],
               'layout': go.Layout(
                   xaxis={'title': axis_x},
                   yaxis={'title': "Score"},
                   margin={'l': 40, 'b': 40, 't': 50, 'r': 10},
                   legend={'x': 0.0, 'y': -1.5},
                   hovermode='closest',
                   height= 1000,
                   title="Score en fonction de " + axis_x + " pour l'année " + str(annee)
               )
               }
    elif pathname == "/2016":
        fig = {
            'data':
                [
                    go.Bar(
                        x=resultats.university_name.iloc[:25],
                        y=resultats.score.iloc[:25],
                        name="Score"
                    ),
                    go.Bar(
                        x=resultats.university_name.iloc[:25],
                        y=resultats.prediction.iloc[:25],
                        name="Prédiction du modèle"
                    ),
                ],
            'layout': go.Layout(
                title= "Comparaison des prédictions du modèle aux scores",
                height= 500,
            )
        }
    else:
        fig = {}
    return fig

@app.callback(
    Output('radio-x', 'children'),
    [
        Input('url', 'pathname')
    ])
def update_graph_choice(pathname):
    if pathname in ['/2011', '/2012', '/2013', '/2014', '/2015']:
        children=\
            [
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
    else:
        children = []
    return children
