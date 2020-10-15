from sklearn.linear_model import LinearRegression
import sqlite3 as sql
import numpy as np

conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price FROM car_data')
rows = np.array(cursor.fetchall()).T
rows[0] = 2020 - rows[0]

model = LinearRegression()
reg = model.fit(X=rows[0].reshape((-1, 1)), y=rows[1])
a_sklearn = reg.coef_
b_sklearn = reg.intercept_

conn.close()