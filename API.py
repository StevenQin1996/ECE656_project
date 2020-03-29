import pymysql
import sys
import pandas as pd
import random
import string
from datetime import date


# zYagTYoClQeP-7JxiTa7jw

class emptyQuery(Exception):
    pass


def get_connection_key():
    connection_key = {'host': '149.248.53.217', 'port': 3306, 'username': 'steven', 'password': '123456',
                      'database': 'Test2'}
    return connection_key


def BusinessPage(user_id):
    try:
        while True:
            search_name = input("Please enter the search content:  ")
            sql = "Select business_id FROM Category WHERE category = '{data}'".format(data=search_name)
            result = display_sql(sql)
            if not result.empty:
                Search_Business_List(search_name,user_id)
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


def Search_Business_List(name,user_id):
    try:
            while True:
                business = input("Please enter the business name:  ")
                sql = "SELECT B.business_id FROM " \
                      "Category C INNER JOIN Business B ON C.business_id = B.business_id " \
                      "WHERE C.category LIKE {x} AND B.name = '{y}';" \
                    .format(x="'%" + name + "%'", y=business)
                result = display_sql(sql)
                if not result.empty:
                    Search_Business_Info(result.values[0][0],user_id)
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


def Search_Business_Info(id,user_id):
    try:
        sql = "SELECT name, address, city, state, stars FROM Business WHERE business_id = '{}'".format(id)
        result = display_sql(sql)
        print(result)
        print("==================== "
              "Review of this business:"
              " ====================")
        sql = "SELECT review_id, useful, funny, cool, text FROM Review WHERE business_id = '{}'".format(id)
        result = display_sql(sql)
        print(result)
        inp = input("type review id to continue reading a post / type skip to continue")
        if inp == "skip":
            return
        else:
            read_review(inp, user_id)
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)

def read_review(review_id, user_id):
    sql = "SELECT * FROM Review WHERE review_id = '{}'".format(review_id)
    review_result = display_sql(sql)
    print(review_result)
    like_input = input("Do you like this review:")
    

def UserPage(user_id):
    inp = input("1: Write Review\n"
                "2: Follow Group / Topic \n"
                "3: Read Notification\n")
    if inp == "1":
        Review(user_id)
    elif inp == "2":
        Follow(user_id)
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
                    my_input = {'review_id': randomString(25), 'user_id': user_id, 'business_id': business_id,
                                'date': date.today()}

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
                    sql = "select review_count, business_id from Business where business_id = '{}'".format(business_id)
                    result = display_sql(sql)

                    update_sql("Business", "review_count", int(result["review_count"].values + 1), "business_id",
                               result["business_id"])

                    push_notification("friends", my_input['review_id'], my_input['user_id'],
                                      my_input['business_id'])
                    push_notification("groups", my_input['review_id'], my_input['user_id'],
                                      my_input['business_id'])

                return 0
        except emptyQuery:
            print("an Error happened: ")
            print("Maybe choose another Business ID From Following:")
            sql = "SELECT business_id FROM Business limit 5"
            result = display_sql(sql)
            print(result)


def follow_group(user_id):
    try:
        name = input("Please input the group name:")
        sql = "SELECT U.user_id " \
              "FROM Groups_info G INNER JOIN User_Group U ON G.group_id = U.group_id " \
              "WHERE G.name = '{}';".format(name)
        user_list = display_sql(sql)
        if not user_list.empty and user_id in user_list['user_id'].values:
            print("You already in the group {}".format(name))
            return
        elif not user_list.empty and user_id not in user_list['user_id'].values:
            sql = "SELECT group_id FROM Groups_info WHERE name = '{name}';".format(name=name)
            result = display_sql(sql)
            my_input = {'group_id': result.values[0][0], 'user_id': user_id}
            insert_data("User_Group", my_input)
        else:
            inp = input("The group {} is not exist, do you want to create this group(Y/N): ".format(name))
            if inp == "Y":
                my_input1 = {'name': name}
                insert_data("Groups_info", my_input1)
                sql = "SELECT group_id FROM Groups_info WHERE name = '{name}';".format(name=name)
                result = display_sql(sql)
                my_input2 = {'group_id': result.values[0][0], 'user_id': user_id}
                insert_data("User_Group", my_input2)
            else:
                return
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)


def follow_topic(user_id):
    try:
        name = input("Please input the topic name:")
        sql = "SELECT business_id FROM Business WHERE name = '{}';".format(name)
        result = display_sql(sql)
        if not result.empty:
            sql = "SELECT F.user_id " \
                  "FROM Business B INNER JOIN Follow F ON B.business_id = F.business_id " \
                  "WHERE B.name = '{}'; ".format(name)
            user_list = display_sql(sql)
            if not user_list.empty and user_id in user_list['user_id'].values:
                print("You already follow the topic {}".format(name))
                return
            else:
                sql = "SELECT business_id FROM Business WHERE name = '{name}';".format(name=name)
                result = display_sql(sql)
                my_input = {'business_id': result.values[0][0], 'user_id': user_id}
                insert_data("Follow", my_input)
        else:
            print("Do not have this topic")
    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)


def Follow(user_id):
    inp = input("1: Follow a group\n"
                "2: Follow a topic\n")
    if inp == "1":
        follow_group(user_id)
    elif inp == "2":
        follow_topic(user_id)
    else:
        print("Wrong Input Try Again")


def push_notification(relation, review_id, review_user, review_business):
    if relation.lower() == "friends":
        sql = "SELECT friend_id as user_id FROM Friends WHERE user_id = '{}'".format(review_user)
        result = display_sql(sql)
        result.insert(1, "review_id", review_id, allow_duplicates=False)
        result.insert(1, "reviewbusiness_id", review_business, allow_duplicates=False)
        result.insert(1, "reviewuser_id", review_user, allow_duplicates=False)
        result.insert(1, "is_read", 0, allow_duplicates=False)
        result.insert(1, "relation", relation, allow_duplicates=False)
        insert_pandas("Notification", result)

    elif relation.lower() == "groups":
        sql = "select group_id from User_Group where user_id = '{}'".format(review_user)
        result = display_sql(sql)
        for group in result['group_id']:
            sql = "select user_id from User_Group where group_id = {} and user_id <> '{}'".format(group, review_user)
            result = display_sql(sql)
            result.insert(1, "review_id", review_id, allow_duplicates=False)
            result.insert(1, "reviewbusiness_id", review_business, allow_duplicates=False)
            result.insert(1, "reviewuser_id", review_user, allow_duplicates=False)
            result.insert(1, "is_read", 0, allow_duplicates=False)
            result.insert(1, "relation", relation, allow_duplicates=False)
            insert_pandas("Notification", result)
    print("Notification send complete\n")


def Notification(user_id):
    while True:
        try:
            sql = "select count(notification_id) as 'count' " \
                  "from Notification N " \
                  "where N.user_id = '{}' and N.is_read = 0".format(user_id)
            result = display_sql(sql)
            if result.empty:
                raise emptyQuery
            elif result["count"].values == 0:
                print("There is no new notification\n")
                break
            else:
                print("You have {} new messages\n".format(result["count"].values))
                user_choice = input("type 1 to read reviews or quit to exit \n")
                if user_choice == "1":
                    sql = "select N.notification_id,R.review_id,B.name as business_name, R.stars, R.date, R.text, R.useful, R.funny, R.cool " \
                          "from Notification N " \
                          "inner join Review R on N.review_id = R.review_id " \
                          "inner join Business B on R.business_id = B.business_id " \
                          "where N.user_id = '{}' and N.is_read = 0".format(user_id)
                    result = display_sql(sql)
                    count = 0
                    my_id = []
                    while count < len(result):
                        temp = result.loc[count]
                        print(temp)
                        my_id.append(temp["notification_id"])
                        inp = input("type next to read another post, like to like the current post, or quit to exit\n")
                        if inp.lower() == "next":
                            count += 1
                        elif inp.lower() == "quit":
                            break
                        elif inp.lower() == "like":
                            like(user_id, temp["review_id"])
                        else:
                            print("invalid input\n")
                            continue
                    read_id = pd.DataFrame(data=my_id, columns=["notification_id"])
                    update_sql("Notification", "is_read", 1, "notification_id", read_id["notification_id"])
                elif user_choice == "quit":
                    break
        except emptyQuery:
            print("an Error happened: \n")
            print("Maybe choose another Business ID From Following: \n")
            sql = "SELECT business_id FROM Business limit 5"
            result = display_sql(sql)
            print(result)


def like(user_id, review_id):
    sql = "select count(*) as 'count' from like_review where user_id = '{}' and review_id = '{}'".format(user_id,
                                                                                                         review_id)
    like_result = display_sql(sql)
    if like_result["count"].values == 0:
        my_input = {'review_id': review_id, 'user_id': user_id}
        insert_data("like_review", my_input)
        print("You liked this post\n")
    elif like_result["count"].values != 0:
        print("You already liked this post\n")


def HomePage(user_name, user_id):
    print("Hi {}".format(user_name))
    inp = input("1:Search\n"
                "2:User Home\n"
                "3:Sign Out\n")
    if inp == "1":
        BusinessPage(user_id)
    elif inp == "2":
        UserPage(user_id)
    elif inp == "3":
        login()
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
            print("ID do not exist, choose another User ID From Following: \n")
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


# insert data as dictionary
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

    except pymysql.InternalError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    except pymysql.err.ProgrammingError as error:
        code, message = error.args
        print(">>>>>>>>>>>>>", code, message)
    finally:
        connection.close()


# display selected data
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


# update existing data
def update_sql(table, update_column, update_value, clause_column, clause_value):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'], local_infile=1)
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE {} set {} = {} where {} = ".format(table, update_column, update_value, clause_column)
            sql += "%s"
            records = clause_value.tolist()
            # print(type(records))
            cursor.executemany(sql, records)
            connection.commit()
    except pymysql.err.OperationalError as error:
        print(">>>>>>>>>>>>>", error)
    finally:
        connection.close()


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    print("Welcome to Yelp!")
    result = login()
    user_name = result[0]
    user_id = result[1]
    while True:
        HomePage(user_name, user_id)


if __name__ == '__main__':
    main()
