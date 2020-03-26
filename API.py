import pymysql
import csv
import sys
import pandas as pd


def get_connection_key():
    connection_key = {'host': '149.248.53.217', 'port': 3306, 'username': 'steven', 'password': '123456',
                      'database': 'Test2'}
    return connection_key


def BusinessPage():
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            while True:
                search_name = input("Please enter the search content:")
                sql = "Select business_id FROM Category WHERE category = '{data}'".format(data=search_name)
                cursor.execute(sql)
                data = cursor.fetchall()
                connection.commit()
                if data:
                    Search_Business_List(search_name)
                    return
                print("{} is not in category list, please choose one from following:\n".format(search_name))
                sql = "select category FROM Category GROUP BY category order by count(business_id) desc limit 10;"
                cursor.execute(sql)
                data_list = cursor.fetchall()
                cols = cursor.description
                connection.commit()
                col = []
                for i in cols:
                    col.append(i[0])
                data_list = list(map(list, data_list))
                data_list = pd.DataFrame(data_list, columns=col)
                print(data_list)
    finally:
        connection.close()


def Search_Business_List(name):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            while True:
                business = input("Please enter the business name:")
                sql = "SELECT B.business_id FROM " \
                      "Category C INNER JOIN Business B ON C.business_id = B.business_id " \
                      "WHERE C.category LIKE {x} AND B.name = '{y}';"\
                    .format(x="'%"+name+"%'", y=business)
                cursor.execute(sql)
                data_id = cursor.fetchall()
                connection.commit()
                if data_id:
                    Search_Business_Info(data_id[0][0])
                    return
                print("{x} is not in {y} list, please choose one from following:".format(x=business, y=name))
                sql = "SELECT name FROM Category C INNER JOIN Business B ON C.business_id = B.business_id WHERE category LIKE {x};" \
                    .format(x="'%" + name + "%'")
                cursor.execute(sql)
                data_list = cursor.fetchall()
                cols = cursor.description
                connection.commit()
                col = []
                for i in cols:
                    col.append(i[0])
                data_list = list(map(list, data_list))
                data_list = pd.DataFrame(data_list, columns=col)
                print(data_list)
    finally:
        connection.close()

def Search_Business_Info(id):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT name, address, city, state, stars FROM Business WHERE business_id = '{}'".format(id)
            cursor.execute(sql)
            data_list = cursor.fetchall()
            cols = cursor.description
            connection.commit()
            col = []
            for i in cols:
                col.append(i[0])
            data_list = list(map(list, data_list))
            data_list = pd.DataFrame(data_list, columns=col)
            print(data_list)
    finally:
        connection.close()

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
                cols = cursor.description
                connection.commit()
                col = []
                for i in cols:
                    col.append(i[0])
                user_list = list(map(list, user_list))
                data = pd.DataFrame(user_list, columns=col)
                print(data)
    finally:
        connection.close()


def main():
    print("Welcome to Yelp!")
    user_name = login()
    while True:
        HomePage(user_name)


if __name__ == '__main__':
    main()