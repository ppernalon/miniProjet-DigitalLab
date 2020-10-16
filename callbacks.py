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
    Output('plot', 'figure'),
    [
        Input("choix-method", 'value'),
    ])
def update_graph(method):
    if method == "monovariable":
        fig = {
            'data': [
                go.Scatter(
                    x=car_data[0],
                    y=car_data[-2],
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
            fig = go.Scatter(
                x=[np.min(data[0]), np.max(data[0])],
                y=[np.min(data[0]) * a + b, np.max(data[0]) * a + b],
                mode="lines",
                marker={'color': colors[method]},
                name=method,
            )
            return fig

        a_numpy, b_numpy = get_param_numpy(np.vstack((car_data[0], car_data[-2])))
        fig['data'].append(fig_append(a_numpy, b_numpy, car_data, 'numpy'))

        a_scipy, b_scipy = get_param_scipy(np.vstack((car_data[0], car_data[-2])))
        fig['data'].append(fig_append(a_scipy, b_scipy, car_data, 'scipy'))

        a_sklearn, b_sklearn = get_param_sklearn(np.vstack((car_data[0], car_data[-2])))
        fig['data'].append(fig_append(a_sklearn, b_sklearn, car_data, 'sklearn'))
        
    return fig