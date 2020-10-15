import sqlite3 as sql
import seaborn as sb
import numpy as np
import pandas as pd

conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price FROM car_data')
rows = np.array(cursor.fetchall()).T

dataBase = pd.DataFrame({'Year': rows[0], 'Selling_Price': rows[1]})

sb.set_theme(style='ticks')
g = sb.catplot(x='Year', y='Selling_Price', data=dataBase)

conn.close()