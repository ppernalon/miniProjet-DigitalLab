import sqlite3 as sql
import numpy as np

conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price FROM car_data')
rows = np.array(cursor.fetchall()).T
rows[0] = 2020 - rows[0]

a_numpy, b_numpy = np.polyfit(rows[0], rows[1], 1)

print(b_numpy)

conn.close()