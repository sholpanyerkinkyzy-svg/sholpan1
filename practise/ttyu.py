import pandas as pd
import numpy as np


try:
    df = pd.read_csv('products_advanced_dataset.csv')

except FileNotFoundError:
    print("Файл табылмады ")

    data = {
        'product_id': range(1, 11),
        'category': ['Electronics', 'Beauty', 'Electronics', 'Home', 'Beauty'] * 2,
        'brand': ['Apple', 'Loreal', 'Samsung', 'IKEA', 'Dior'] * 2,
        'price': [1200, 50, 1000, 300, 80, 1100, 45, 950, 350, 90],
        'rating': [4.8, 3.5, 4.2, 4.0, 4.9, 4.7, 3.2, 2.1, 4.1, 4.8],
        'sales_count': [150, 200, 120, 80, 300, 140, 210, 15, 85, 310],
        'date': pd.date_range(start='2024-01-01', periods=10, freq='ME')
    }

    df = pd.DataFrame(data)


# 1. EDA ANALYSIS

def task_1_eda_report(df):
    print("\n  1-ТАПСЫРМА: EDA \n")

    print("Categories:")
    print(df['category'].value_counts())

    print("\nBrands:")
    print(df['brand'].value_counts())

    print("\nStatistics:")
    print(df[['price', 'rating', 'sales_count']].describe())

    stability = df.groupby('category').agg({
        'rating': ['mean', 'std'],
        'sales_count': 'sum'
    })

    print("\nCategory stability:")
    print(stability)

    print("\nConclusion:")
    for cat in stability.index:
        mean_rating = stability.loc[cat, ('rating', 'mean')]
        std_rating = stability.loc[cat, ('rating', 'std')]

        status = "Stable" if std_rating < 0.5 else "Unstable"
        print(f"- {cat}: {status} | avg rating = {mean_rating:.2f}")


task_1_eda_report(df)



# 2. TREND ANALYSIS

def analyze_trends_over_time(df):
    print("\n 2-ТАПСЫРМА: TRENDS \n")

    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month

    trends = df.groupby(['year', 'month']).agg({
        'price': 'mean',
        'rating': 'mean',
        'sales_count': 'sum'
    }).reset_index()

    print(trends)

    high_sales = trends[trends['sales_count'] > trends['sales_count'].mean()]

    print("\nHigh sales months:")
    print(high_sales[['year', 'month']])

    diff = trends.iloc[-1]['price'] - trends.iloc[0]['price']

    print("\nPrice trend:")
    print("Up " if diff > 0 else "Down ")


analyze_trends_over_time(df)



# 3. ANOMALY DETECTION

def get_anomalous_products(df):
    price_median = df['price'].median()
    rating_q1 = df['rating'].quantile(0.25)
    sales_q3 = df['sales_count'].quantile(0.75)

    for _, row in df.iterrows():
        if row['price'] > price_median and row['rating'] < rating_q1 and row['sales_count'] >= sales_q3:
            yield row


print("\n 3-ТАПСЫРМА: ANOMALIES ")

found = False
for product in get_anomalous_products(df):
    print(product.to_dict())
    found = True

if not found:
    print("No anomalies found")



# 4. SEGMENTATION

def assign_segment(row):
    if row['price'] > 500 and row['rating'] >= 4.5:
        return "Premium Star"
    elif row['rating'] < 3.0 and row['sales_count'] < 20:
        return "Underperformer"
    elif row['sales_count'] > 100 and row['rating'] >= 4.0:
        return "Best Seller"
    elif row['rating'] >= 4.7:
        return "Hidden Gem"
    else:
        return "Standard"


df['segment'] = df.apply(assign_segment, axis=1)

print("\n 4-ТАПСЫРМА: SEGMENTS ")
print(df[['product_id', 'price', 'rating', 'segment']])