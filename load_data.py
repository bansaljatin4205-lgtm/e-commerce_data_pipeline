import csv
import mysql.connector
from getpass import getpass

# MySQL password enter karein
password = getpass("Enter MySQL password: ")

# MySQL database se connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="ecommerce_db"
)

cursor = connection.cursor()

# CSV file se data read karna
with open("data/orders.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    sql = """
    INSERT INTO orders
    (order_id, order_date, customer_name, city, product,
     category, quantity, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    count = 0

    for row in reader:
        cursor.execute(sql, (
            int(row["order_id"]),
            row["order_date"],
            row["customer_name"],
            row["city"],
            row["product"],
            row["category"],
            int(row["quantity"]),
            float(row["price"])
        ))

        count += 1

# Data save karna
connection.commit()

print("Successfully inserted", count, "orders into MySQL!")

cursor.close()
connection.close()