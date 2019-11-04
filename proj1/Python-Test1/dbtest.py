import mysql.connector
import tweepy

conn = mysql.connector.connect(
         user='root',
         password='',
         host='127.0.0.1',
         database='airflow')

conn.close()