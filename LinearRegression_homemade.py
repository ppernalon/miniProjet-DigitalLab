import numpy as np
import sqlite3 as sql

class LinearRegression_HM(object):
    def __init__(self):
        self.coef = None
        self.origine = None

    def fit(self, entries, targets):
        self.coef = np.dot(np.linalg.inv(np.dot(entries.T, entries)), np.dot(entries.T, targets))
        self.origine = np.mean(targets) - np.dot(self.coef, np.mean(entries, axis=0))


    def predict(self, entries):
        return np.dot(self.coef, entries) + self.origine


conn = sql.connect('mini_projet.db')
cursor = conn.cursor()
cursor.execute('SELECT Year, Selling_Price, Kms_Driven, Transmission FROM car_data')
rows = np.array(cursor.fetchall()).T

transmission_row = []
for x in rows[3]:
    if x == 'Manual':
        transmission_row.append(1)
    else:
        transmission_row.append(0)

rows[3] = transmission_row
rows = rows.astype(float)

model = LinearRegression_HM()
reg = model.fit(rows[:3].T, rows[3])