#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

from app import app

import numpy as np
from fetch_data import fetch_data
from LinearRegression_homemade import get_param_HM
from numpy_reg_linear import get_param_numpy
from scipy_reg_linear import get_param_scipy
from sklearn_reg_linear import get_param_sklearn, get_param_sklearn_multivariate

car_data = fetch_data()


@app.callback(
    Output('div_mono', 'children'),
    [
        Input("choix-method", 'value'),
    ])
def update_graph_mono(method):
    children = []
    if method == "monovariable":
        fig = {
            'data': [
                go.Scatter(
                    x=car_data[0],
                    y=car_data[1],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name="données",
                )
            ]
        }

        def fig_append(a, b, data, method):
            colors = {"numpy": 'rgba(0, 255, 0,1 )', 'scipy': 'rgba(255, 0, 0, 1)', 'sklearn': 'rgba(255, 255, 0, 1)',
                      'HM': 'rgba(0, 255, 255, 1)'}
            fig_app = go.Scatter(
                x=[np.min(data[0]), np.max(data[0])],
                y=[np.min(data[0]) * a + b, np.max(data[0]) * a + b],
                mode="lines",
                marker={'color': colors[method]},
                name=method,
            )
            return fig_app

        a_numpy, b_numpy = get_param_numpy(np.vstack((car_data[0], car_data[1])))
        fig['data'].append(fig_append(a_numpy, b_numpy, car_data, 'numpy'))

        a_scipy, b_scipy = get_param_scipy(np.vstack((car_data[0], car_data[1])))
        fig['data'].append(fig_append(a_scipy, b_scipy, car_data, 'scipy'))

        a_sklearn, b_sklearn = get_param_sklearn(np.vstack((car_data[0], car_data[1])))
        fig['data'].append(fig_append(a_sklearn, b_sklearn, car_data, 'sklearn'))

        fig["layout"] = go.Layout(
            xaxis={'title': 'Year'},
            yaxis={'title': 'Selling Price'},
            margin={'l': 40, 'b': 40, 't': 40, 'r': 10},
            legend={'x': 1.0, 'y': 0.3},
            title="Prix de vente en fonction de l'année",
            hovermode='closest',
        )

        children.append(
            dcc.Graph(
                figure=fig
            )
        )

    return children


@app.callback(
    Output('div_multi', 'children'),
    [
        Input('choix-method', 'value'),
    ]
)
def update_graph_multi(method):
    children = []
    if method == "multivariable":
        idx_annee = np.argwhere(car_data[0] == 2003)
        idx = np.argwhere(car_data[3][idx_annee.T[0]] == 1).T[0]

        a_multi, b_multi = get_param_sklearn_multivariate(car_data)

        fig1 = {
            'data': [
                go.Scatter(
                    x=car_data[2][idx],
                    y=car_data[1][idx],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name="données",
                ),
                go.Scatter(
                    x=[np.min(car_data[2][idx]), np.max(car_data[2][idx])],
                    y=[np.dot(a_multi, [2003, np.min(car_data[2][idx]), 1]) + b_multi, np.dot(a_multi, [2003, np.max(car_data[2][idx]), 1]) + b_multi],
                    mode = "lines",
                )
            ],
            "layout": go.Layout(
                xaxis={'title': 'Kms Driven'},
                yaxis={'title': 'Selling Price'},
                margin={'l': 40, 'b': 40, 't': 50, 'r': 50},
                legend={'x': 1.0, 'y': 0.3},
                hovermode='closest',
                title="année 2003",
            )}
        children.append(
            dcc.Graph(
                id='fig1_Years_f',
                figure=fig1
            ),
        )
        slider_years = html.Div([
            html.H5("Quelle année ?"),
            dcc.Slider(
                id='year_slider',
                min=2003,
                max=2018,
                step=1,
                value=2003,
                marks={i: '{}'.format(i) for i in range(2003, 2019)}
            )]
        )
        children.append(slider_years)

        transmission_radio = html.Div([
            html.H5("Quelle type de transmission ?"),
            dcc.RadioItems(
                id="choix_transmission",
                options=[
                    {'label': 'manual', 'value': 1},
                    {'label': 'automatic', 'value': 0},
                ],
                value=1,
                labelStyle={'display': 'inline-block'}
            ),
        ])
        children.append(transmission_radio)

    return children


@app.callback(
    Output('fig1_Years_f', 'figure'),
    [
        Input('year_slider', 'value'),
        Input('choix_transmission', 'value'),
    ]
)
def update_fig1(annee, transmission):
    idx_annee = np.argwhere(car_data[0] == annee)
    idx = np.argwhere(car_data[3][idx_annee.T[0]] == transmission).T[0]

    a_multi, b_multi = get_param_sklearn_multivariate(car_data)

    fig1 = {
        'data': [
            go.Scatter(
                x=car_data[2][idx],
                y=car_data[1][idx],
                mode='markers',
                opacity=0.8,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name="données",
            ),
            go.Scatter(
                x=[np.min(car_data[2][idx]), np.max(car_data[2][idx])],
                y=[np.dot(a_multi, [annee, np.min(car_data[2][idx]), transmission]) + b_multi,
                   np.dot(a_multi, [annee, np.max(car_data[2][idx]), transmission]) + b_multi],
                mode="lines",
            )
        ],
        "layout": go.Layout(
            xaxis={'title': 'Kms Driven'},
            yaxis={'title': 'Selling Price'},
            margin={'l': 40, 'b': 40, 't': 50, 'r': 10},
            legend={'x': 1.0, 'y': 0.3},
            hovermode='closest',
            title="année " + str(annee),
        )}
    return fig1
