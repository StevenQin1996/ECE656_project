import pymysql
import csv
import sys
import pandas as pd

csv.field_size_limit(sys.maxsize)


# change to be made later:
# 1. CML to control user name, password, and database
# 2. check if validation and handle wrong username/password
# 3. check database existance, create new database if need(if mistyped, then recommend an existing database similar to the entry)
def get_connection_key():
    connection_key = {'host': '149.248.53.217', 'port': 3306, 'username': 'steven', 'password': '123456',
                      'database': 'Test2'}
    return connection_key


def get_data_from_csv(myfile):
    df = pd.read_csv(myfile, delimiter=',')
    df.fillna("NULL", inplace = True)
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


def split_data(id, column_name, table_name):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT {id},{column} FROM {table} WHERE {column} <> 'None' ".format(id=id, column=column_name, table=table_name)
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
        split_data = (data.set_index([id])[column_name]
                               .str.split(',', expand=True)
                               .stack()
                               .reset_index(level=1, drop=True)
                               .reset_index(name=column_name))
        print(data)
        return split_data


def split_friend(id, column_name, table_name):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT {id},{column} FROM {table} WHERE {column} <> 'None' ".format(id=id, column=column_name, table=table_name)
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
        length = len(data)% 10000
        for i in range(1,length):
            split_data = (data.set_index([id])[column_name][i*(i-1)*10000:i*10000]
                   .str.split(',', expand=True)
                   .stack()
                   .reset_index(level=1, drop=True)
                   .reset_index(name=column_name))
            insert_data("Friends", split_data)
        split_data = (data.set_index([id])[column_name][length * (length - 1) * 10000:-1]
                      .str.split(',', expand=True)
                      .stack()
                      .reset_index(level=1, drop=True)
                      .reset_index(name=column_name))
        insert_data("Friends", split_data)


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

    # retrieve data local
    # file_business_attributes = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_attributes.csv"
    # file_business_hours = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_hours.csv"
    # file_business = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business.csv"
    # file_checkin = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_checkin.csv"
    # file_review = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_review.csv"
    # file_tip = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_tip.csv"
    # file_user = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_user.csv"

    # business_attributes = get_data_from_csv(file_business_attributes)
    # insert_data("Business_attributes", business_attributes)
    #
    # business_hours = get_data_from_csv(file_business_hours)
    # insert_data("Business_hours", business_hours)

    # business = get_data_from_csv(file_business)
    # insert_data("Business", business)

    # checkin = get_data_from_csv(file_checkin)
    # insert_data("Checkin", checkin)
    #
    # user = get_data_from_csv(file_user)
    # insert_data("User", user)
    #
    # review = get_data_from_csv(file_review)
    # insert_data("Review", review)
    #
    # tips = get_data_from_csv(file_tip)
    # insert_data("Tips", tips)
    #
    # split_elite = split_data("user_id", "elite", "User")
    # insert_data("Elite", split_elite)

    # split_category = split_data("business_id", "categories", "Business")
    # insert_data("Category", split_category)

    split_friends = split_friend("user_id", "friends", "User")



if __name__ == '__main__':
    main()
