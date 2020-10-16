import sqlite3 as sql
import numpy as np


def fetch_data():
    conn = sql.connect('mini_projet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Year, Selling_Price, Kms_Driven, Transmission FROM car_data')
    data = np.array(cursor.fetchall()).T
    conn.close()

    transmission_row = []
    for x in data[3]:
        if x == 'Manual':
            transmission_row.append(1)
        else:
            transmission_row.append(0)

    data[3] = transmission_row
    rows = data.astype(float)
    return rows