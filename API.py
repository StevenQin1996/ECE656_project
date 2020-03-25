import pymysql
import csv
import sys
import pandas as pd

def get_connection_key():
    connection_key = {'host': '149.248.53.217', 'port': 3306, 'username': 'steven', 'password': '123456',
                      'database': 'Test2'}
    return connection_key

def BusinessPage():
    inp = input("Select Category:\n"
                "1: Restaurant\n"
                "2: Coffee & Tea\n"
                "3: Hair Salons\n"
                "4: More\n")


def UserPage():
    inp = input("1: Write Review\n"
                "2: Follow Group\n"
                "3: Follow Topic\n"
                "4: Unread Notification")


def HomePage(user_name):
    print("Hi {}".format(user_name))
    inp = input("1:Search\n"
                "2:Me\n")
    if inp == "1":
        BusinessPage()
    elif inp == "2":
        UserPage()
    elif inp == "exit":
        sys.exit(0)
    else:
        print("Wrong Input Try Again")


def login():
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            while True:
                user_id = input("Please Enter Your User ID: ")
                sql = "SELECT name FROM User WHERE user_id = '{}'".format(user_id)
                cursor.execute(sql)
                user_name = cursor.fetchall()
                connection.commit()
                if user_name:
                    return user_name[0][0]
                print("User ID do not exist, choose another User ID From Following:")
                sql = "SELECT user_id FROM User limit 5"
                cursor.execute(sql)
                user_list = cursor.fetchall()
                connection.commit()
                print(user_list)
    finally:
        connection.close()


def main():
    print("Welcome to Yelp!")
    user_name = login()
    while True:
        HomePage(user_name)


if __name__ == '__main__':
    main()