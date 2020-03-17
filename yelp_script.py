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
                      'database': 'Project'}
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
                `business_id` VARCHAR(25) NOT NULL,\
                `name` VARCHAR(25) DEFAULT NULL,\
                `neighborhood` VARCHAR(128) DEFAULT NULL,\
                `address` VARCHAR(128) DEFAULT NULL,\
                `city` VARCHAR(25) DEFAULT NULL,\
                `state` VARCHAR(25) DEFAULT NULL,\
                `postal_code` VARCHAR(10) DEFAULT NULL,\
                `latitude` DOUBLE DEFAULT NULL,\
                `longitude` DOUBLE DEFAULT NULL,\
                `stars` FLOAT DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `is_open` VARCHAR(25) DEFAULT NULL,\
                `categories` TEXT DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_attributes'
            cursor.execute(sql)
            sql = "CREATE TABLE Business_attributes(\
                `business_id` VARCHAR(25) NOT NULL,\
                `AcceptsInsurance` VARCHAR(5) DEFAULT NULL,\
                `ByAppointmentOnly` VARCHAR(5) DEFAULT NULL,\
                `BusinessAcceptsCreditCards` VARCHAR(5) DEFAULT NULL,\
                `BusinessParking_garage` VARCHAR(5) DEFAULT NULL,\
                `BusinessParking_street` VARCHAR(5) DEFAULT NULL,\
                `BusinessParking_validated` VARCHAR(5) DEFAULT NULL,\
                `BusinessParking_lot` VARCHAR(5) DEFAULT NULL,\
                `BusinessParking_valet` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_coloring` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_africanamerican` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_curly` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_perms` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_kids` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_extensions` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_asian` VARCHAR(5) DEFAULT NULL,\
                `HairSpecializesIn_straightperms` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsPriceRange2` VARCHAR(5) DEFAULT NULL,\
                `GoodForKids` VARCHAR(5) DEFAULT NULL,\
                `WheelchairAccessible` VARCHAR(5) DEFAULT NULL,\
                `BikeParking` VARCHAR(5) DEFAULT NULL,\
                `Alcohol` VARCHAR(5) DEFAULT NULL,\
                `HasTV` VARCHAR(5) DEFAULT NULL,\
                `NoiseLevel` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsAttire` VARCHAR(5) DEFAULT NULL,\
                `Music_dj` VARCHAR(5) DEFAULT NULL,\
                `Music_background_music` VARCHAR(5) DEFAULT NULL,\
                `Music_no_music` VARCHAR(5) DEFAULT NULL,\
                `Music_karaoke` VARCHAR(5) DEFAULT NULL,\
                `Music_live` VARCHAR(5) DEFAULT NULL,\
                `Music_video` VARCHAR(5) DEFAULT NULL,\
                `Music_jukebox` VARCHAR(5) DEFAULT NULL,\
                `Ambience_romantic` VARCHAR(5) DEFAULT NULL,\
                `Ambience_intimate` VARCHAR(5) DEFAULT NULL,\
                `Ambience_classy` VARCHAR(5) DEFAULT NULL,\
                `Ambience_hipster` VARCHAR(5) DEFAULT NULL,\
                `Ambience_divey` VARCHAR(5) DEFAULT NULL,\
                `Ambience_touristy` VARCHAR(5) DEFAULT NULL,\
                `Ambience_trendy` VARCHAR(5) DEFAULT NULL,\
                `Ambience_upscale` VARCHAR(5) DEFAULT NULL,\
                `Ambience_casual` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsGoodForGroups` VARCHAR(5) DEFAULT NULL,\
                `Caters` VARCHAR(5) DEFAULT NULL,\
                `WiFi` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsReservations` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsTakeOut` VARCHAR(5) DEFAULT NULL,\
                `HappyHour` VARCHAR(5) DEFAULT NULL,\
                `GoodForDancing` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsTableService` VARCHAR(5) DEFAULT NULL,\
                `OutdoorSeating` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsDelivery` VARCHAR(5) DEFAULT NULL,\
                `BestNights_monday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_tuesday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_friday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_wednesday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_thursday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_sunday` VARCHAR(5) DEFAULT NULL,\
                `BestNights_saturday` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_dessert` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_latenight` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_lunch` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_dinner` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_breakfast` VARCHAR(5) DEFAULT NULL,\
                `GoodForMeal_brunch` VARCHAR(5) DEFAULT NULL,\
                `CoatCheck` VARCHAR(5) DEFAULT NULL,\
                `Smoking` VARCHAR(5) DEFAULT NULL,\
                `DriveThru` VARCHAR(5) DEFAULT NULL,\
                `DogsAllowed` VARCHAR(5) DEFAULT NULL,\
                `BusinessAcceptsBitcoin` VARCHAR(5) DEFAULT NULL,\
                `Open24Hours` VARCHAR(5) DEFAULT NULL,\
                `BYOBCorkage` VARCHAR(5) DEFAULT NULL,\
                `BYOB` VARCHAR(5) DEFAULT NULL,\
                `Corkage` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_dairy` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_gluten` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_vegan` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_kosher` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_halal` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_soy` VARCHAR(5) DEFAULT NULL,\
                `DietaryRestrictions_vegetarian` VARCHAR(5) DEFAULT NULL,\
                `AgesAllowed` VARCHAR(5) DEFAULT NULL,\
                `RestaurantsCounterService` VARCHAR(5) DEFAULT NULL,\
                PRIMARY KEY(`business_id`) \
                )ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;"
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_hours'
            cursor.execute(sql)
            sql = 'CREATE TABLE Business_hours(\
                `business_id` VARCHAR(25) NOT NULL,\
                `Monday` VARCHAR(25) DEFAULT NULL,\
                `Wednesday` VARCHAR(25) DEFAULT NULL,\
                `Tuesday` VARCHAR(25) DEFAULT NULL,\
                `Friday` VARCHAR(25) DEFAULT NULL,\
                `Thursday` VARCHAR(25) DEFAULT NULL,\
                `Saturday` VARCHAR(25) DEFAULT NULL,\
                `Sunday` VARCHAR(25) DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Checkin'
            cursor.execute(sql)
            sql = 'CREATE TABLE Checkin(\
                `business_id` VARCHAR(25) NOT NULL,\
                `weekday` VARCHAR(25) DEFAULT NULL,\
                `hour` TIME DEFAULT NULL,\
                `checkins` INT DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Review'
            cursor.execute(sql)
            sql = 'CREATE TABLE Review(\
                `review_id` VARCHAR(25) NOT NULL,\
                `user_id` VARCHAR(25) DEFAULT NULL,\
                `business_id` VARCHAR(25) DEFAULT NULL,\
                `stars` INT DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                `text` TEXT DEFAULT NULL,\
                `date` DATE,\
                PRIMARY KEY (`review_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)


            sql = 'DROP TABLE IF EXISTS Tips'
            cursor.execute(sql)
            sql = 'CREATE TABLE Tips(\
                `text` TEXT DEFAULT NULL,\
                `date` DATE DEFAULT NULL,\
                `likes` INT DEFAULT NULL,\
                `business_id` VARCHAR(25) NOT NULL,\
                `user_id` VARCHAR(25) NOT NULL,\
                PRIMARY KEY (`business_id`,`user_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS User'
            cursor.execute(sql)
            sql = "CREATE TABLE User(\
                `user_id` VARCHAR(25) NOT NULL,\
                `name` VARCHAR(25) DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `yelping_since` DATE DEFAULT NULL,\
                `friends` TEXT DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                `fans` INT DEFAULT NULL,\
                `elite` VARCHAR(25) DEFAULT NULL,\
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
                `review_id` VARCHAR(25) NOT NULL,\
                `user_id` VARCHAR(25) DEFAULT NULL,\
                `business_id` VARCHAR(25) DEFAULT NULL,\
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
            sql = "INSERT INTO {} VALUES (".format(table_name)
            for count in range(len(mydata.columns) - 1):
                sql += ("%s,")
            sql += ("%s)")

            parameter = []
            for count in range(len(mydata.values)):
                parameter.append(tuple(mydata.values[count]))

            cursor.executemany(sql, parameter)
            connection.commit()
    finally:
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


# set up python on server
def main():
    # create tables
    create_tables()

    # retrieve data ubuntu
    # file_business_attributes = "/var/lib/mysql/Project/yelp_business_attributes.csv"
    # file_business_hours = "/var/lib/mysql/Project/yelp_business_hours.csv"
    # file_business = "/var/lib/mysql/Project/yelp_business.csv"
    # file_checkin = "/var/lib/mysql/Project/yelp_checkin.csv"
    # file_review = "/var/lib/mysql/Project/yelp_review.csv"
    # file_tip = "/var/lib/mysql/Project/yelp_tip.csv"
    # file_user = "/var/lib/mysql/Project/yelp_user.csv"

    # retrieve data
    file_business_attributes = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_attributes.csv"
    file_business_hours = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business_hours.csv"
    file_business = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_business.csv"
    file_checkin = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_checkin.csv"
    file_review = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_review.csv"
    file_tip = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_tip.csv"
    file_user = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/csv/yelp_user.csv"

    business_attributes = get_data_from_csv(file_business_attributes)
    print(business_attributes.head())
    insert_data("Business_attributes", business_attributes)

    # business_hours = get_data_from_csv(file_business_hours)
    # business = get_data_from_csv(file_business)
    # checkin = get_data_from_csv(file_checkin)
    # review = get_data_from_csv(file_review)
    # tips = get_data_from_csv(file_tip)
    # user = get_data_from_csv(file_user)
    #
    #
    # insert_data("Business_hours", business_hours)
    # insert_data("Business", business)
    # insert_data("Checkin", checkin)
    # insert_data("Tips", tips)
    # insert_data("User", user)
    # insert_data("Review", review)

if __name__ == '__main__':
    main()
