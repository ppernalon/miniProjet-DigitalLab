import pandas as pd
import matplotlib.pyplot as plt

car_data = pd.read_csv("carData.csv")
print(car_data.head())
print(car_data.dtypes)


def apercu_hist():
    plt.hist(car_data.Year)
    plt.title('Year')
    plt.show()

    plt.hist(car_data.Selling_Price)
    plt.title('Selling_Price')
    plt.show()

    plt.hist(car_data.Present_Price)
    plt.title('Present_Price')
    plt.show()

    plt.hist(car_data.Kms_Driven)
    plt.title('Kms_Driven')
    plt.show()

    plt.hist(car_data.Fuel_Type)
    plt.title('Fuel_Type')
    plt.show()

    plt.hist(car_data.Seller_Type)
    plt.title('Seller_Type')
    plt.show()

    plt.hist(car_data.Transmission)
    plt.title('Transmission')
    plt.show()


#apercu_hist()
