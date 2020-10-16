import sqlite3 as sql
import numpy as np
from scipy import stats

conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price FROM car_data')
rows = np.array(cursor.fetchall()).T
rows[0] = 2020 - rows[0]

a_scipy, b_scipy, r_scipy, p_scipy, err_scipy = stats.linregress(rows[0], rows[1])

conn.close()


def get_param_scipy(data):
    a_scipy, b_scipy, r_scipy, p_scipy, err_scipy = stats.linregress(data[0], data[1])
    return a_scipy, b_scipy
