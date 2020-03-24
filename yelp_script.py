import pymysql
import csv
import sys
import pandas as pd
import gc
import math

csv.field_size_limit(sys.maxsize)


# change to be made later:
# 1. CML to control user name, password, and database
# 2. check if validation and handle wrong username/password
# 3. check database existance, create new database if need(if mistyped, then recommend an existing database similar to the entry)
def get_connection_key():
    connection_key = {'host': '149.248.53.217', 'port': 3306, 'username': 'steven', 'password': '123456',
                      'database': 'Test3'}
    return connection_key


def get_data_from_csv(myfile):
    df = pd.read_csv(myfile, delimiter=',')
    df.fillna("NULL", inplace=True)
    print("get data complete")
    return df


def insert_data(table_name, mydata):
    # Open database connection
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])

    try:
        with connection.cursor() as cursor:
            print("{}: update start".format(table_name))

            sql = "INSERT INTO {} VALUES (".format(table_name)
            for count in range(len(mydata.columns) - 1):
                sql += ("%s,")
            sql += ("%s)")

            records = mydata.to_records(index=False).tolist()
            cursor.executemany(sql, records)
            connection.commit()
    finally:
        print("{}: update complete".format(table_name))
        connection.close()


def load_from_csv(table_name, mydata):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)

    try:
        with connection.cursor() as cursor:
            sql = "LOAD DATA local INFILE {} INTO TABLE {} FIELDS TERMINATED BY ',' ENCLOSED BY '""' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS IGNORE 1".format(
                mydata, table_name)
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


def execute_query(file_path):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)

    try:
        with connection.cursor() as cursor:
            sql = "source {}".format(file_path)
            cursor.execute(sql)
    finally:
        connection.close()


def split_data(id, column_name, table_name, spliter, target_table):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT {id},{column} FROM {table} WHERE {column} <> 'None' ".format(id=id, column=column_name,
                                                                                       table=table_name)
            cursor.execute(sql)
            data = cursor.fetchall()
            cols = cursor.description
            connection.commit()
    finally:
        connection.close()
        col = []
        for i in cols:
            col.append(i[0])
        data = list(map(list, data))
        data = pd.DataFrame(data, columns=col)
        length = math.floor(len(data) / 1000)
        for i in range(1, length):
            split_data = (data.set_index([id])[column_name][i * 1000 - 1000:i * 1000 - 1]
                          .str.split(spliter, expand=True)
                          .stack()
                          .reset_index(level=1, drop=True)
                          .reset_index(name=column_name))
            insert_data(target_table, split_data)
            del split_data
            gc.collect()
            print("split data status: {}".format(i))

        split_data = (data.set_index([id])[column_name][length * 1000:-1]
                      .str.split(spliter, expand=True)
                      .stack()
                      .reset_index(level=1, drop=True)
                      .reset_index(name=column_name))
        insert_data(target_table, split_data)
        print("split data complete")


# set up python on server
def main():
    # retrieve data ubuntu
    file_business_attributes = "/var/lib/mysql-files/yelp_business_attributes.csv"
    file_business_hours = "/var/lib/mysql-files/yelp_business_hours.csv"
    file_business = "/var/lib/mysql-files/yelp_business.csv"
    file_checkin = "/var/lib/mysql-files/yelp_checkin.csv"
    file_review = "/var/lib/mysql-files/yelp_review.csv"
    file_tip = "/var/lib/mysql-files/yelp_tip.csv"
    file_user = "/var/lib/mysql-files/yelp_user.csv"

    business_attributes = get_data_from_csv(file_business_attributes)
    insert_data("Business_attributes", business_attributes)

    business_hours = get_data_from_csv(file_business_hours)
    insert_data("Business_hours", business_hours)

    business = get_data_from_csv(file_business)
    insert_data("Business", business)

    checkin = get_data_from_csv(file_checkin)
    insert_data("Checkin", checkin)

    user = get_data_from_csv(file_user)
    insert_data("User", user)

    review = get_data_from_csv(file_review)
    insert_data("Review", review)

    tips = get_data_from_csv(file_tip)
    insert_data("Tips", tips)

    split_data("business_id", "Category", "Business", ";", "Category")

    split_data("user_id", "elite", "User", ",", "Elite")

    split_data("user_id", "friends", "User", ",", "Friends")

    # execute_query("/home/ECE656_project/remove_duplicate.sql")

if __name__ == '__main__':
    main()
