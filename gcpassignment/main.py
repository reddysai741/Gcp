# import os
# import pandas as pd
# import mysql.connector
# from google.cloud import storage
# from dotenv import load_dotenv
# from io import StringIO

# load_dotenv()

# DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# DB_PORT = int(os.getenv("DB_PORT", 3307))
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")

# GCS_BUCKET = os.getenv("GCS_BUCKET")
# GCS_FILE = os.getenv("GCS_FILE")

# client = storage.Client()
# bucket = client.bucket(GCS_BUCKET)
# blob = bucket.blob(GCS_FILE)

# csv_text = blob.download_as_text()
# df = pd.read_csv(StringIO(csv_text))

# conn = mysql.connector.connect(
#     host=DB_HOST,
#     port=DB_PORT,
#     user=DB_USER,
#     password=DB_PASSWORD,
#     database=DB_NAME
# )

# cursor = conn.cursor()

# insert_query = """
# INSERT INTO user_transactions
# (user_id, user_name, age, gender, location, membership, total_spent, last_purchase_cat)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
# """

# data = [tuple(row) for row in df.itertuples(index=False)]
# cursor.executemany(insert_query, data)
# conn.commit()

# cursor.execute("""
# INSERT INTO high_value_users
# (user_id, user_name, age, gender, location, membership, total_spent, last_purchase_cat)
# SELECT
#     user_id, user_name, age, gender, location, membership, total_spent, last_purchase_cat
# FROM user_transactions
# WHERE total_spent > 25000
# """)

# conn.commit()
# cursor.close()
# conn.close()


import base64
import json
import os
import mysql.connector

def on_file_upload(event=None):
    
    if event and "data" in event:
        message = base64.b64decode(event["data"]).decode("utf-8")
        payload = json.loads(message)
    else:
        payload = {}

    
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.getenv("DB_PORT", 3307))  
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    
    conn = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = conn.cursor(dictionary=True)

    
    cursor.execute("""
        SELECT user_id, user_name, total_spent
        FROM high_value_users
        ORDER BY total_spent DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    
    print("Top High-Value User:")
    if result:
        print(f"User ID: {result['user_id']}")
        print(f"Name: {result['user_name']}")
        print(f"Total Spent: {result['total_spent']}")
    else:
        print("No users found.")


if __name__ == "__main__":
    on_file_upload()

