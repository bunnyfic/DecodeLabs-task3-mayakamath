import pandas as pd
import mysql.connector

try:
    print("Reading CSV...")

    df = pd.read_csv("sales_data.csv")

    # Convert date column
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    print("CSV Loaded")
    print(df.columns)

    conn = mysql.connector.connect(
        host="localhost",
        port=3305,
        user="root",
        password="bbyningning",
        database="eda_project"
    )

    print("Connected to MySQL")

    cursor = conn.cursor()

    insert_query = """
        INSERT INTO sales_data
(
 OrderID,
 Date,
 CustomerID,
 Product,
 Quantity,
 UnitPrice,
 ShippingAddress,
 PaymentMethod,
 OrderStatus,
 TrackingNumber,
 ItemsInCart,
 CouponCode,
 ReferralSource,
 TotalPrice
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    data = [
        (
            (
 row['OrderID'],
 row['Date'],
 row['CustomerID'],
 row['Product'],
 row['Quantity'],
 row['UnitPrice'],
 row['ShippingAddress'],
 row['PaymentMethod'],
 row['OrderStatus'],
 row['TrackingNumber'],
 row['ItemsInCart'],
 row['CouponCode'],
 row['ReferralSource'],
 row['TotalPrice']
)
            
        )
        for _, row in df.iterrows()
    ]

    # Much faster than executing inside a loop
    cursor.executemany(insert_query, data)

    conn.commit()

    print(f"SUCCESS: {cursor.rowcount} rows inserted")

except Exception as e:
    print("ERROR:")
    print(e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
