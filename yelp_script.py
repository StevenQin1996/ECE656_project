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
                `AcceptsInsurance` Boolean DEFAULT NULL,\
                `ByAppointmentOnly` Boolean DEFAULT NULL,\
                `BusinessAcceptsCreditCards` Boolean DEFAULT NULL,\
                `BusinessParking_garage` Boolean DEFAULT NULL,\
                `BusinessParking_street` Boolean DEFAULT NULL,\
                `BusinessParking_validated` Boolean DEFAULT NULL,\
                `BusinessParking_lot` Boolean DEFAULT NULL,\
                `BusinessParking_valet` Boolean DEFAULT NULL,\
                `HairSpecializesIn_coloring` Boolean DEFAULT NULL,\
                `HairSpecializesIn_africanamerican` Boolean DEFAULT NULL,\
                `HairSpecializesIn_curly` Boolean DEFAULT NULL,\
                `HairSpecializesIn_perms` Boolean DEFAULT NULL,\
                `HairSpecializesIn_kids` Boolean DEFAULT NULL,\
                `HairSpecializesIn_extensions` Boolean DEFAULT NULL,\
                `HairSpecializesIn_asian` Boolean DEFAULT NULL,\
                `HairSpecializesIn_straightperms` Boolean DEFAULT NULL,\
                `RestaurantsPriceRange2` Boolean DEFAULT NULL,\
                `GoodForKids` Boolean DEFAULT NULL,\
                `WheelchairAccessible` Boolean DEFAULT NULL,\
                `BikeParking` Boolean DEFAULT NULL,\
                `Alcohol` Boolean DEFAULT NULL,\
                `HasTV` Boolean DEFAULT NULL,\
                `NoiseLevel` Boolean DEFAULT NULL,\
                `RestaurantsAttire` Boolean DEFAULT NULL,\
                `Music_dj` Boolean DEFAULT NULL,\
                `Music_background_music` Boolean DEFAULT NULL,\
                `Music_no_music` Boolean DEFAULT NULL,\
                `Music_karaoke` Boolean DEFAULT NULL,\
                `Music_live` Boolean DEFAULT NULL,\
                `Music_video` Boolean DEFAULT NULL,\
                `Music_jukebox` Boolean DEFAULT NULL,\
                `Ambience_romantic` Boolean DEFAULT NULL,\
                `Ambience_intimate` Boolean DEFAULT NULL,\
                `Ambience_classy` Boolean DEFAULT NULL,\
                `Ambience_hipster` Boolean DEFAULT NULL,\
                `Ambience_divey` Boolean DEFAULT NULL,\
                `Ambience_touristy` Boolean DEFAULT NULL,\
                `Ambience_trendy` Boolean DEFAULT NULL,\
                `Ambience_upscale` Boolean DEFAULT NULL,\
                `Ambience_casual` Boolean DEFAULT NULL,\
                `RestaurantsGoodForGroups` Boolean DEFAULT NULL,\
                `Caters` Boolean DEFAULT NULL,\
                `WiFi` Boolean DEFAULT NULL,\
                `RestaurantsReservations` Boolean DEFAULT NULL,\
                `RestaurantsTakeOut` Boolean DEFAULT NULL,\
                `HappyHour` Boolean DEFAULT NULL,\
                `GoodForDancing` Boolean DEFAULT NULL,\
                `RestaurantsTableService` Boolean DEFAULT NULL,\
                `OutdoorSeating` Boolean DEFAULT NULL,\
                `RestaurantsDelivery` Boolean DEFAULT NULL,\
                `BestNights_monday` Boolean DEFAULT NULL,\
                `BestNights_tuesday` Boolean DEFAULT NULL,\
                `BestNights_friday` Boolean DEFAULT NULL,\
                `BestNights_wednesday` Boolean DEFAULT NULL,\
                `BestNights_thursday` Boolean DEFAULT NULL,\
                `BestNights_sunday` Boolean DEFAULT NULL,\
                `BestNights_saturday` Boolean DEFAULT NULL,\
                `GoodForMeal_dessert` Boolean DEFAULT NULL,\
                `GoodForMeal_latenight` Boolean DEFAULT NULL,\
                `GoodForMeal_lunch` Boolean DEFAULT NULL,\
                `GoodForMeal_dinner` Boolean DEFAULT NULL,\
                `GoodForMeal_breakfast` Boolean DEFAULT NULL,\
                `GoodForMeal_brunch` Boolean DEFAULT NULL,\
                `CoatCheck` Boolean DEFAULT NULL,\
                `Smoking` Boolean DEFAULT NULL,\
                `DriveThru` Boolean DEFAULT NULL,\
                `DogsAllowed` Boolean DEFAULT NULL,\
                `BusinessAcceptsBitcoin` Boolean DEFAULT NULL,\
                `Open24Hours` Boolean DEFAULT NULL,\
                `BYOBCorkage` Boolean DEFAULT NULL,\
                `BYOB` Boolean DEFAULT NULL,\
                `Corkage` Boolean DEFAULT NULL,\
                `DietaryRestrictions_dairy` Boolean DEFAULT NULL,\
                `DietaryRestrictions_gluten` Boolean DEFAULT NULL,\
                `DietaryRestrictions_vegan` Boolean DEFAULT NULL,\
                `DietaryRestrictions_kosher` Boolean DEFAULT NULL,\
                `DietaryRestrictions_halal` Boolean DEFAULT NULL,\
                `DietaryRestrictions_soy` Boolean DEFAULT NULL,\
                `DietaryRestrictions_vegetarian` Boolean DEFAULT NULL,\
                `AgesAllowed` Boolean DEFAULT NULL,\
                `RestaurantsCounterService` Boolean DEFAULT NULL,\
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

    # retrieve data
    file_business_attributes = "/var/lib/mysql/Project/yelp_business_attributes.csv"
    file_business_hours = "/var/lib/mysql/Project/yelp_business_hours.csv"
    file_business = "/var/lib/mysql/Project/yelp_business.csv"
    file_checkin = "/var/lib/mysql/Project/yelp_checkin.csv"
    file_review = "/var/lib/mysql/Project/yelp_review.csv"
    file_tip = "/var/lib/mysql/Project/yelp_tip.csv"
    file_user = "/var/lib/mysql/Project/yelp_user.csv"

    business_attributes = get_data_from_csv(file_business_attributes)
    business_hours = get_data_from_csv(file_business_hours)
    business = get_data_from_csv(file_business)
    checkin = get_data_from_csv(file_checkin)
    review = get_data_from_csv(file_review)
    tips = get_data_from_csv(file_tip)
    user = get_data_from_csv(file_user)

    insert_data("Business_attributes", business_attributes)
#     insert_data("Business_hours", business_hours)
#     insert_data("Business", business)
#     insert_data("Checkin", checkin)
#     insert_data("Tips", tips)
#     insert_data("User", user)
#     insert_data("Review", review)

if __name__ == '__main__':
    main()
