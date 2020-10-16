from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import sqlite3 as sql
import numpy as np

conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price FROM car_data')
rows = np.array(cursor.fetchall()).T

model = LinearRegression()
reg = model.fit(X=rows[0].reshape((-1, 1)), y=rows[1])
a_sklearn = reg.coef_
b_sklearn = reg.intercept_

cursor.execute('SELECT Year, Selling_Price, Kms_Driven, Transmission FROM car_data')
rows = np.array(cursor.fetchall()).T
conn.close()

transmission_row = []
for x in rows[3]:
    if x == 'Manual':
        transmission_row.append(1)
    else:
        transmission_row.append(0)

rows[3] = transmission_row
rows = rows.astype(float)

model = LinearRegression()
reg = model.fit(X=rows[:3].T, y=rows[3])
a = reg.coef_
b = reg.intercept_

predicted_prices = model.predict(rows[:3].T)


def get_param_sklearn(data):
    model = LinearRegression()
    reg = model.fit(X=data[0].reshape((-1, 1)), y=data[1])
    return reg.coef_, reg.intercept_


def get_param_sklearn_multivariate(data):
    model = LinearRegression()
    reg = model.fit(X=data[np.array([0, 2, 3])].T, y=data[1])
    return reg.coef_, reg.intercept_
