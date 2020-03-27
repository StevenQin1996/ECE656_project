import pymysql
import csv
import sys
import pandas as pd
import random
import string
from datetime import date


class emptyQuery(Exception):
    pass


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
                search_name = input("Please enter the search content:  ")
                sql = "Select business_id FROM Category WHERE category = '{data}'".format(data=search_name)
                cursor.execute(sql)
                data = cursor.fetchall()
                connection.commit()
                if data:
                    Search_Business_List(search_name)
                    return
                print("{} is not in category list, please choose one from following:\n".format(search_name))
                sql = "select category FROM Category GROUP BY category order by count(business_id) desc limit 10;"
                result = display_sql(sql)
                print(result)
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


def Search_Business_List(name):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            while True:
                business = input("Please enter the business name:  ")
                sql = "SELECT B.business_id FROM " \
                      "Category C INNER JOIN Business B ON C.business_id = B.business_id " \
                      "WHERE C.category LIKE {x} AND B.name = '{y}';" \
                    .format(x="'%" + name + "%'", y=business)
                cursor.execute(sql)
                data_id = cursor.fetchall()
                connection.commit()
                if data_id:
                    Search_Business_Info(data_id[0][0])
                    return
                print("{x} is not in {y} list, please choose one from following:".format(x=business, y=name))
                sql = "SELECT name FROM Category C INNER JOIN Business B ON C.business_id = B.business_id WHERE category LIKE {x};" \
                    .format(x="'%" + name + "%'")
                result = display_sql(sql)
                print(result)
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


def Search_Business_Info(id):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT name, address, city, state, stars FROM Business WHERE business_id = '{}'".format(id)
            result = display_sql(sql)
            print(result)
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


def UserPage(user_id):
    inp = input("1: Write Review\n"
                "2: Follow Group / Topic \n"
                "3: Unread Notification\n")
    if inp == "1":
        Review(user_id)
    elif inp == "2":
        Follow()
    elif inp == "3":
        Notification(user_id)
    elif inp == "exit":
        sys.exit(0)
    else:
        print("Wrong Input Try Again\n")


def Review(user_id):
    while True:
        try:
            business_id = input("Enter Business ID:  ")
            sql = "SELECT B.name, B.stars, B.review_count ,B.is_open ,C.category FROM Business B inner join Category C on B.business_id = C.business_id where B.business_id = '{}'".format(
                business_id)
            result = display_sql(sql)
            if result.empty:
                raise emptyQuery
            else:
                print("Business abstraction shown below.\n")
                print(result, "\n")
                user_choice = input("type 1 to insert a review for business {}.\n".format(result['name'][0]))
                if user_choice == "1":
                    my_input = {}
                    my_input['review_id'] = randomString(25)
                    my_input['user_id'] = user_id
                    my_input['business_id'] = business_id
                    my_input['date'] = date.today()

                    # try:
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

                    push_notification_Friend(my_input['review_id'], my_input['user_id'],
                                             my_input['business_id'])
                return 0
        except emptyQuery:
            print("an Error happened: ")
            print("Maybe choose another Business ID From Following:")
            sql = "SELECT business_id FROM Business limit 5"
            result = display_sql(sql)
            print(result)


def Follow():
    print("follow")


def push_notification_Friend(review_id, review_user, review_business):
    sql = "SELECT friend_id as user_id FROM Friends WHERE user_id = '{}'".format(review_user)
    result = display_sql(sql)
    result.insert(1, "review_id", review_id, allow_duplicates=False)
    result.insert(1, "reviewbusiness_id", review_business, allow_duplicates=False)
    result.insert(1, "reviewuser_id", review_user, allow_duplicates=False)
    result.insert(1, "is_read", 0, allow_duplicates=False)

    insert_pandas("Notification", result)


def Notification(user_id):
    while True:
        try:
            sql = "select count(notification_id) as 'count' " \
                  "from Notification N " \
                  "where N.user_id = '{}' and N.is_read = 0".format(user_id)
            result = display_sql(sql)
            if result.empty:
                print("There is no new notification")
                print(">>>>>>>>>>>.continue working")
                raise emptyQuery
            else:
                print("You have {} new messages".format(result["count"].values))
                user_choice = input("type 1 to read reviews \n")
                if user_choice == "1":
                    sql = "select N.notification_id,R.review_id,B.name as business_name, R.stars, R.date, R.text, R.useful, R.funny, R.cool " \
                          "from Notification N " \
                          "inner join Review R on N.review_id = R.review_id " \
                          "inner join Business B on R.business_id = B.business_id " \
                          "where N.user_id = '{}' and N.is_read = 0".format(user_id)
                    result = display_sql(sql)
                    print(result)

                    update_sql("Notification", "is_read", 1, "notification_id", result["notification_id"])

        except emptyQuery:
            print("an Error happened: ")
            print("Maybe choose another Business ID From Following:")
            sql = "SELECT business_id FROM Business limit 5"
            result = display_sql(sql)
            print(result)


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
    while True:
        try:
            user_id = input("Please Enter Your User ID:  ")
            sql = "SELECT name FROM User WHERE user_id = '{}'".format(user_id)
            result = display_sql(sql)
            if result.empty:
                raise emptyQuery
            else:
                return (result["name"][0], user_id)
        except emptyQuery:
            print("ID do not exist, choose another User ID From Following:")
            sql = "SELECT user_id FROM User limit 5"
            result = display_sql(sql)
            print(result)


def randomString(stringLength):
    """Generate a random string of fixed length """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def convert_sql(dict):
    col = ', '.join("`" + str(x).replace('/', '_') + "`" for x in dict.keys())
    val = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
    return col, val


def insert_data(table_name, mydata):
    # Open database connection
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])
    try:
        with connection.cursor() as cursor:
            column, value = convert_sql(mydata)
            query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, column, value)
            cursor.execute(query)
            connection.commit()

            print("{}: update complete".format(table_name))
            sys.stdout.flush()
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


def insert_pandas(table_name, mydata):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            # creating column list for insertion
            cols = "`,`".join([str(i) for i in mydata.columns.tolist()])

            # Insert DataFrame recrds one by one.
            sql = "INSERT INTO {}".format(table_name)
            sql += "(`" + cols + "`) VALUES (" + "%s," * (len(mydata.columns) - 1) + "%s)"
            records = mydata.to_records(index=False).tolist()
            cursor.executemany(sql, records)
            connection.commit()

            # the connection is not autocommitted by default, so we must commit to save our changes
            connection.commit()

            print("{}: update complete".format(table_name))
            sys.stdout.flush()
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


def display_sql(sql):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            data_list = cursor.fetchall()
            cols = cursor.description
            connection.commit()
            col = []
            for i in cols:
                col.append(i[0])
            data_list = list(map(list, data_list))
            data_list = pd.DataFrame(data_list, columns=col)
            return data_list
    except pymysql.InternalError as error:
        print(">>>>>>>>>>>>>", error)
    except pymysql.err.ProgrammingError as error:
        print(">>>>>>>>>>>>>", error)
    except pymysql.err.OperationalError as error:
        print(">>>>>>>>>>>>>", error)

    finally:
        connection.close()


def update_sql(table, update_column, update_value, clause_column, clause_value):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE {} set {} = {} where {} = ".format(table, update_column, update_value, clause_column)
            sql += "%s"
            records = clause_value.tolist()
            print(type(records))
            cursor.executemany(sql, records)
            connection.commit()
    except pymysql.err.OperationalError as error:
        print(">>>>>>>>>>>>>", error)
    finally:
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
