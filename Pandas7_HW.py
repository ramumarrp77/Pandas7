# Problem 1 : Immediate Food Delivery I 

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediateOrders = delivery['order_date'] == delivery['customer_pref_delivery_date']
    immediateCount = immediateOrders.sum()
    return pd.DataFrame([round((immediateCount/ len(delivery)) * 100,2)], columns=['immediate_percentage'])



# Problem 2 : Count Salary Categories

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal = accounts.income < 20000
    avg_sal = (accounts.income >= 20000) & (accounts.income <= 50000)
    high_sal = accounts.income > 50000
    low_cnt = low_sal.sum()
    avg_cnt = avg_sal.sum()
    high_cnt = high_sal.sum()
    return pd.DataFrame([['Low Salary',low_cnt],['Average Salary', avg_cnt],['High Salary', high_cnt]], columns = ['category','accounts_count'])
