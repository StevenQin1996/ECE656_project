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
                      'database': 'Test'}
    return connection_key


def get_data_from_csv(myfile):
    df = pd.read_csv(myfile, delimiter=',')
    return df


def create_tables():
    # Open database connection
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])

    try:
        with connection.cursor() as cursor:

            # create table
            sql = 'DROP TABLE IF EXISTS Business'
            cursor.execute(sql)
            sql = 'CREATE TABLE Business(\
                `business_id` VARCHAR(32) NOT NULL,\
                `name` VARCHAR(32) DEFAULT NULL,\
                `neighborhood` VARCHAR(32) DEFAULT NULL,\
                `address` VARCHAR(32) DEFAULT NULL,\
                `city` VARCHAR(32) DEFAULT NULL,\
                `state` VARCHAR(32) DEFAULT NULL,\
                `postal_code` VARCHAR(10) DEFAULT NULL,\
                `latitude` DOUBLE DEFAULT NULL,\
                `longitude` DOUBLE DEFAULT NULL,\
                `stars` FLOAT DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `is_open` VARCHAR(32) DEFAULT NULL,\
                `categories` VARCHAR(128) DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_attributes'
            cursor.execute(sql)
            sql = "CREATE TABLE Business_attributes(\
                `business_id` VARCHAR(32) NOT NULL,\
                `AcceptsInsurance` VARCHAR(32) DEFAULT NULL,\
                `ByAppointmentOnly` VARCHAR(32) DEFAULT NULL,\
                `BusinessAcceptsCreditCards` VARCHAR(32) DEFAULT NULL,\
                `BusinessParking_garage` VARCHAR(32) DEFAULT NULL,\
                `BusinessParking_street` VARCHAR(32) DEFAULT NULL,\
                `BusinessParking_validated` VARCHAR(32) DEFAULT NULL,\
                `BusinessParking_lot` VARCHAR(32) DEFAULT NULL,\
                `BusinessParking_valet` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_coloring` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_africanamerican` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_curly` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_perms` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_kids` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_extensions` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_asian` VARCHAR(32) DEFAULT NULL,\
                `HairSpecializesIn_straightperms` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsPriceRange2` VARCHAR(32) DEFAULT NULL,\
                `GoodForKids` VARCHAR(32) DEFAULT NULL,\
                `WheelchairAccessible` VARCHAR(32) DEFAULT NULL,\
                `BikeParking` VARCHAR(32) DEFAULT NULL,\
                `Alcohol` VARCHAR(32) DEFAULT NULL,\
                `HasTV` VARCHAR(32) DEFAULT NULL,\
                `NoiseLevel` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsAttire` VARCHAR(32) DEFAULT NULL,\
                `Music_dj` VARCHAR(32) DEFAULT NULL,\
                `Music_background_music` VARCHAR(32) DEFAULT NULL,\
                `Music_no_music` VARCHAR(32) DEFAULT NULL,\
                `Music_karaoke` VARCHAR(32) DEFAULT NULL,\
                `Music_live` VARCHAR(32) DEFAULT NULL,\
                `Music_video` VARCHAR(32) DEFAULT NULL,\
                `Music_jukebox` VARCHAR(32) DEFAULT NULL,\
                `Ambience_romantic` VARCHAR(32) DEFAULT NULL,\
                `Ambience_intimate` VARCHAR(32) DEFAULT NULL,\
                `Ambience_classy` VARCHAR(32) DEFAULT NULL,\
                `Ambience_hipster` VARCHAR(32) DEFAULT NULL,\
                `Ambience_divey` VARCHAR(32) DEFAULT NULL,\
                `Ambience_touristy` VARCHAR(32) DEFAULT NULL,\
                `Ambience_trendy` VARCHAR(32) DEFAULT NULL,\
                `Ambience_upscale` VARCHAR(32) DEFAULT NULL,\
                `Ambience_casual` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsGoodForGroups` VARCHAR(32) DEFAULT NULL,\
                `Caters` VARCHAR(32) DEFAULT NULL,\
                `WiFi` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsReservations` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsTakeOut` VARCHAR(32) DEFAULT NULL,\
                `HappyHour` VARCHAR(32) DEFAULT NULL,\
                `GoodForDancing` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsTableService` VARCHAR(32) DEFAULT NULL,\
                `OutdoorSeating` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsDelivery` VARCHAR(32) DEFAULT NULL,\
                `BestNights_monday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_tuesday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_friday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_wednesday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_thursday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_sunday` VARCHAR(32) DEFAULT NULL,\
                `BestNights_saturday` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_dessert` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_latenight` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_lunch` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_dinner` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_breakfast` VARCHAR(32) DEFAULT NULL,\
                `GoodForMeal_brunch` VARCHAR(32) DEFAULT NULL,\
                `CoatCheck` VARCHAR(32) DEFAULT NULL,\
                `Smoking` VARCHAR(32) DEFAULT NULL,\
                `DriveThru` VARCHAR(32) DEFAULT NULL,\
                `DogsAllowed` VARCHAR(32) DEFAULT NULL,\
                `BusinessAcceptsBitcoin` VARCHAR(32) DEFAULT NULL,\
                `Open24Hours` VARCHAR(32) DEFAULT NULL,\
                `BYOBCorkage` VARCHAR(32) DEFAULT NULL,\
                `BYOB` VARCHAR(32) DEFAULT NULL,\
                `Corkage` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_dairy` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_gluten` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_vegan` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_kosher` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_halal` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_soy` VARCHAR(32) DEFAULT NULL,\
                `DietaryRestrictions_vegetarian` VARCHAR(32) DEFAULT NULL,\
                `AgesAllowed` VARCHAR(32) DEFAULT NULL,\
                `RestaurantsCounterService` VARCHAR(32) DEFAULT NULL,\
                PRIMARY KEY(`business_id`) \
                )ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;"
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_hours'
            cursor.execute(sql)
            sql = 'CREATE TABLE Business_hours(\
                `business_id` VARCHAR(32) NOT NULL,\
                `Monday` VARCHAR(32) DEFAULT NULL,\
                `Wednesday` VARCHAR(32) DEFAULT NULL,\
                `Tuesday` VARCHAR(32) DEFAULT NULL,\
                `Friday` VARCHAR(32) DEFAULT NULL,\
                `Thursday` VARCHAR(32) DEFAULT NULL,\
                `Saturday` VARCHAR(32) DEFAULT NULL,\
                `Sunday` VARCHAR(32) DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Checkin'
            cursor.execute(sql)
            sql = 'CREATE TABLE Checkin(\
                `business_id` VARCHAR(32) NOT NULL,\
                `weekday` VARCHAR(32) DEFAULT NULL,\
                `hour` TIME DEFAULT NULL,\
                `checkins` INT DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Review'
            cursor.execute(sql)
            sql = 'CREATE TABLE Review(\
                `review_id` VARCHAR(32) NOT NULL,\
                `user_id` VARCHAR(32) DEFAULT NULL,\
                `business_id` VARCHAR(32) DEFAULT NULL,\
                `stars` INT DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                `text` VARCHAR(500) DEFAULT NULL,\
                `date` DATE,\
                PRIMARY KEY (`review_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Tips'
            cursor.execute(sql)
            sql = "CREATE TABLE Tips(\
                `tips_id` INT NOT NULL AUTO_INCREMENT,\
                `text` VARCHAR(500) DEFAULT NULL,\
                `date` DATE DEFAULT NULL,\
                `likes` INT DEFAULT NULL,\
                `business_id` VARCHAR(32) NOT NULL,\
                `user_id` VARCHAR(32) NOT NULL,\
                PRIMARY KEY (`tips_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;"
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS User'
            cursor.execute(sql)
            sql = "CREATE TABLE User(\
                `user_id` VARCHAR(32) NOT NULL,\
                `name` VARCHAR(32) DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `yelping_since` DATE DEFAULT NULL,\
                `friends` VARCHAR(500) DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                `fans` INT DEFAULT NULL,\
                `elite` VARCHAR(32) DEFAULT NULL,\
                `average_stars` FLOAT DEFAULT NULL,\
                `compliment_hot` INT DEFAULT NULL,\
                `compliment_more` INT DEFAULT NULL,\
                `compliment_profile` INT DEFAULT NULL,\
                `compliment_cute` INT DEFAULT NULL,\
                `compliment_list` INT DEFAULT NULL,\
                `compliment_note` INT DEFAULT NULL,\
                `compliment_plain` INT DEFAULT NULL,\
                `compliment_cool` INT DEFAULT NULL,\
                `compliment_funny` INT DEFAULT NULL,\
                PRIMARY KEY (`user_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;"
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Review'
            cursor.execute(sql)
            sql = 'CREATE TABLE Review(\
                `review_id` VARCHAR(32) NOT NULL,\
                `user_id` VARCHAR(32) DEFAULT NULL,\
                `business_id` VARCHAR(32) DEFAULT NULL,\
                `stars` INT DEFAULT NULL,\
                `date` DATE DEFAULT NULL,\
                `text` TEXT DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                PRIMARY KEY (`review_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)
    finally:
        connection.close()


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

            parameter = []
            for count in range(len(mydata.values)):
                # print(tuple(mydata.values[count]))
                parameter.append(tuple(mydata.values[count]))

            cursor.executemany(sql, parameter)
            connection.commit()
    finally:
        print("{}: update complete".format(table_name))
        connection.close()


def test():
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])

    try:
        with connection.cursor() as cursor:
            sql = "show tables;"

            cursor.executemany(sql)
            connection.commit()
    finally:
        connection.close()


def load_from_csv(table_name, mydata):
    my_key = get_connection_key()
    connection = pymysql.connect(host=my_key['host'], user=my_key['username'], password=my_key['password'],
                                 database=my_key['database'])

    try:
        with connection.cursor() as cursor:
            sql = "LOAD DATA local INFILE {}\
                        INTO TABLE {} \
                        FIELDS TERMINATED BY ',' \
                        ENCLOSED BY ""\
                        LINES TERMINATED BY '\n'\
                        IGNORE 1 ROWS".format(mydata, table_name)

            cursor.executemany(sql)
            connection.commit()
    finally:
        connection.close()




# set up python on server
def main():
    # create tables
    create_tables()

    # retrieve data ubuntu
    file_business_attributes = "/var/lib/mysql/Project/yelp_business_attributes.csv"
    file_business_hours = "/var/lib/mysql/Project/yelp_business_hours.csv"
    file_business = "/var/lib/mysql/Project/yelp_business.csv"
    file_checkin = "/var/lib/mysql/Project/yelp_checkin.csv"
    file_review = "/var/lib/mysql/Project/yelp_review.csv"
    file_tip = "/var/lib/mysql/Project/yelp_tip.csv"
    file_user = "/var/lib/mysql/Project/yelp_user.csv"

    # retrieve data local
    # file_business_attributes = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_attributes.csv"
    # file_business_hours = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_hours.csv"
    # file_business = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business.csv"
    # file_checkin = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_checkin.csv"
    # file_review = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_review.csv"
    # file_tip = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_tip.csv"
    # file_user = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_user.csv"

    business_attributes = get_data_from_csv(file_business_attributes)
    load_from_csv("Business_attributes", business_attributes)
    # insert_data("Business_attributes", business_attributes)

    business_hours = get_data_from_csv(file_business_hours)
    load_from_csv("Business_hours", business_hours)
    # insert_data("Business_hours", business_hours)

    business = get_data_from_csv(file_business)
    load_from_csv("Business", business)
    # insert_data("Business", business)

    checkin = get_data_from_csv(file_checkin)
    load_from_csv("Checkin", checkin)
    # insert_data("Checkin", checkin)

    user = get_data_from_csv(file_user)
    load_from_csv("User", user)
    # insert_data("User", user)

    review = get_data_from_csv(file_review)
    load_from_csv("Review", review)
    # insert_data("Review", review)

    tips = get_data_from_csv(file_tip)
    load_from_csv("Tips", tips)
    # insert_data("Tips", tips)


if __name__ == '__main__':
    main()
