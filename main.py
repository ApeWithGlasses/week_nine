import pandas as pd

df = pd.read_csv('data/sales.csv')

def calculate_average_sales_by_month(df):
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    df['Year'], df['Month'] = df['Sale_Date'].dt.year, df['Sale_Date'].dt.month
    avg_sales = df.groupby(['Year', 'Month'])['Sale_Amount'].mean()
    return avg_sales

def analyze_restaurant_data():
    df = pd.read_csv('data/restaurant.csv')
    avg_salaries = df.groupby('Site')['Salary'].mean()
    highest_salary_site = avg_salaries.idxmax()
    total_salaries = df.groupby(['Site', 'Type of food', 'Type of drink'])['Salary'].sum()
    most_sold_food = df['Type of food'].value_counts().idxmax()
    all_avg_salaries = df['Salary'].mean()
    total_sells = df['Salary'].sum()
    print('Type of food with the most sales: ', most_sold_food)
    print('\nTotal salary by site, type of food, and type of drink: \n', total_salaries)
    print('\nSite with the highest average salary: ', highest_salary_site)
    print('\nAverage salaries: ', all_avg_salaries)
    print('\nTotal sells: ', total_sells)

def read_manipulate_temperatures():
    df = pd.read_csv('data/temperatures.csv')

    print('First 5 rows: \n', df.head())

    print('\nNumber of rows: ', df.shape[0])
    print('\nNumber of columns: ', df.shape[1])

    print('\nNull values per column: \n', df.isnull().sum())

    print('\nAverage temperature_1: ', df['temperature_1'].mean())
    print('Average temperature_2: ', df['temperature_2'].mean())
    print('Average temperature_3: ', df['temperature_3'].mean())

    print('\nMaximum temperature_1: ', df['temperature_1'].max())
    print('Maximum temperature_2: ', df['temperature_2'].max())
    print('Maximum temperature_3: ', df['temperature_3'].max())

    print('\nMinimum temperature_1: ', df['temperature_1'].min())
    print('Minimum temperature_2: ', df['temperature_2'].min())
    print('Minimum temperature_3: ', df['temperature_3'].min())

def run():
    electronics_df = df[df['Category'] == 'Electronics']

    print('Testing data: \n', df.head())
    print('\nNumber of rows: ', df.shape[0])
    print('\nNumber of columns: ', df.shape[1])
    print('\nNull values per column: \n', df.isnull().sum(),  '\n')
    print('Sum of sales: ', df['Sale_Amount'].sum())
    print('\nAverage sales by month: \n', calculate_average_sales_by_month(df))
    print('\nMost sold product: ', df['Product_ID'].value_counts().idxmax())
    electronics_df.to_csv('data/electronics_sales.csv', index=False)
    read_manipulate_temperatures()
    analyze_restaurant_data()

if __name__ == "__main__":
    run()