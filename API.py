import pymysql
import csv
import sys
import pandas as pd
import random
import string
from datetime import date



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


def UserPage(user_id):
    inp = input("1: Write Review\n"
                "2: Follow Group / Topic \n"
                "3: Unread Notification\n")
    if inp == "1":
        Review(user_id)
    elif inp == "2":
        Follow(user_id)
    elif inp == "3":
        Notification()
    elif inp == "exit":
        sys.exit(0)
    else:
        print("Wrong Input Try Again\n")


def Review(user_id):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            while True:
                try:
                    business_id = input("Enter Business ID:  ")
                    sql = "SELECT B.name, B.stars, B.review_count ,B.is_open ,C.category FROM Business B inner join Category C on B.business_id = C.business_id where B.business_id = '{}'".format(
                        business_id)
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    connection.commit()
                    if data:
                        print("Business abstraction shown below.\n")
                        columns = ["name", "stars", "review_count", "is_open", "categories"]
                        df = pd.DataFrame(data, columns=columns)
                        print(df)
                        user_choice = input("type 1 to insert a review for business {}.\n".format(df['name'][0]))
                        if user_choice == "1":
                            print(">>>>>>>>>>>>>>>.")
                            sql = "describe Review"
                            cursor.execute(sql)
                            for columns in cursor.fetchall():
                                print(columns)

                            my_input = {}
                            my_input['review_id'] = randomString(25)
                            my_input['user_id'] = user_id
                            my_input['business_id'] = business_id
                            my_input['date'] = date.today()

                            try:
                                inp = input("Enter stars from 1 - 5: ")
                                if 1 <= int(inp) <= 5:
                                    my_input['stars'] = int(inp)

                                inp = input("Enter useful 0 or 1:  ")
                                if 0 <= int(inp) <= 1:
                                    my_input['useful'] = int(inp)

                                inp = input("Enter useful 0 or 1:  ")
                                if 0 <= int(inp) <= 1:
                                    my_input['funny'] = int(inp)

                                inp = input("Enter useful 0 or 1:  ")
                                if 0 <= int(inp) <= 1:
                                    my_input['cool'] = int(inp)

                                my_input['text'] = input("Enter review below: \n")

                                insert_data("Review", my_input)

                            except ValueError:
                                print("invalid entry")
                        else:
                            return 0
                    else:
                        raise pymysql.err.InternalError()
                except pymysql.err.InternalError as e:
                    print("an Error happened: ")
                    print("Maybe choose another Business ID From Following:")
                    sql = "SELECT business_id FROM Business limit 5"
                    cursor.execute(sql)
                    business_list = cursor.fetchall()
                    connection.commit()
                    print(business_list)
    finally:
        connection.close()


def Group(user_id):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            name = input("Please input the group name:")
            sql = "SELECT U.user_id " \
                  "FROM Groups_info G INNER JOIN User_Group U ON G.group_id = U.group_id " \
                  "WHERE G.name = '{}';".format(name)
            cursor.execute(sql)
            user_list = cursor.fetchall()
            cols = cursor.description
            connection.commit()
            col = []
            for i in cols:
                col.append(i[0])
            data_list = list(map(list, user_list))
            data_list = pd.DataFrame(data_list, columns=col)
            if user_list and user_id in data_list['user_id'].values:
                print("You already in the group {}".format(name))
                return
            elif user_list and user_id not in data_list['user_id'].values:
                sql = "INSERT INTO User_Group(group_id, user_id) SELECT" \
                      "(SELECT group_id FROM Groups_info WHERE name = '{name}'), '{user}';" \
                    .format(name=name, user=user_id)
                cursor.execute(sql)
                connection.commit()
                print("Successfully join in the group {}".format(name))
            else:
                inp = input("The group {} is not exist, do you want to create this group(Y/N): ".format(name))
                if inp == "Y" or "y":
                    sql = "INSERT INTO Groups_info(name) VALUES('{}');".format(name)
                    cursor.execute(sql)
                    connection.commit()
                    sql = "INSERT INTO User_Group(group_id, user_id) SELECT" \
                          "(SELECT group_id FROM Groups_info WHERE name = '{group}'), '{user}';"\
                        .format(group=name, user=user_id)
                    cursor.execute(sql)
                    connection.commit()
                    print("Successfully create the group {}".format(name))
                elif inp == "N" or "n":
                    return
    finally:
        connection.close()


def Topic(user_id):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            business_name = input("Please input the topic name:")
            sql = "SELECT F.user_id " \
                  "FROM Business B INNER JOIN Follow F ON B.business_id = F.business_id " \
                  "WHERE B.name = '{}'; ".format(business_name)
            cursor.execute(sql)
            user_list = cursor.fetchall()
            cols = cursor.description
            connection.commit()
            col = []
            for i in cols:
                col.append(i[0])
            data_list = list(map(list, user_list))
            data_list = pd.DataFrame(data_list, columns=col)
            if user_list and user_id in data_list['user_id'].values:
                print("You already follow the topic {}".format(business_name))
                return
            elif user_list and user_id not in data_list['user_id'].values:
                sql = "INSERT INTO Follow(business_id, user_id) SELECT" \
                      "(SELECT business_id FROM Business WHERE name = '{group}'), '{user}';" \
                    .format(group=business_name, user=user_id)
                cursor.execute(sql)
                connection.commit()
                print("Successfully follow in the topic {}".format(business_name))
            else:
                print("Do not have this topic")
    finally:
        connection.close()


def Follow(user_id):
    inp = input("1: Follow a group\n"
                "2: Follow a topic\n")
    if inp == "1":
        Group(user_id)
    elif inp == "2":
        Topic(user_id)
    else:
        print("Wrong Input Try Again")


def Notification():
    print("Notification")


def HomePage(user_name, user_id):
    print("Hi {}".format(user_name))
    inp = input("1:Search\n"
                "2:Me\n")
    if inp == "1":
        BusinessPage()
    elif inp == "2":
        UserPage(user_id)
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
                user_id = input("Please Enter Your User ID:  ")
                sql = "SELECT name FROM User WHERE user_id = '{}'".format(user_id)
                cursor.execute(sql)
                user_name = cursor.fetchall()
                connection.commit()
                if user_name:
                    return user_name[0][0], user_id
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


def randomString(stringLength):
    """Generate a random string of fixed length """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def convert_sql(dict):
    col = ', '.join("`" + str(x).replace('/', '_') + "`" for x in dict.keys())
    val = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
    return col,val

def insert_data(table_name, mydata):
    # Open database connection
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])

    try:
        with connection.cursor() as cursor:
            column, value = convert_sql(mydata)
            query = 'INSERT INTO {} ({}) VALUES ({})'.format('Test', column, value)
            cursor.execute(query)
            connection.commit()

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        print("{}: update complete".format(table_name))
        sys.stdout.flush()
        connection.close()


def main():
    pd.set_option('display.max_columns', None)
    print("Welcome to Yelp!")
    result = login()
    user_name = result[0]
    user_id = result[1]
    while True:
        HomePage(user_name, user_id)


if __name__ == '__main__':
    main()
