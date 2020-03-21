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
                      'database': 'Test3'}
    return connection_key

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
                `business_id` VARCHAR(128) NOT NULL,\
                `name` VARCHAR(128) DEFAULT NULL,\
                `neighborhood` VARCHAR(128) DEFAULT NULL,\
                `address` VARCHAR(128) DEFAULT NULL,\
                `city` VARCHAR(128) DEFAULT NULL,\
                `state` VARCHAR(128) DEFAULT NULL,\
                `postal_code` VARCHAR(10) DEFAULT NULL,\
                `latitude` VARCHAR(128) DEFAULT NULL,\
                `longitude` VARCHAR(128) DEFAULT NULL,\
                `stars` FLOAT DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `is_open` VARCHAR(128) DEFAULT NULL,\
                `categories` TEXT DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_attributes'
            cursor.execute(sql)

            sql = 'CREATE TABLE Business_attributes(\
                `business_id` VARCHAR(128) NOT NULL,\
                `AcceptsInsurance` VARCHAR(128) DEFAULT NULL,\
                `ByAppointmentOnly` VARCHAR(128) DEFAULT NULL,\
                `BusinessAcceptsCreditCards` VARCHAR(128) DEFAULT NULL,\
                `BusinessParking_garage` VARCHAR(128) DEFAULT NULL,\
                `BusinessParking_street` VARCHAR(128) DEFAULT NULL,\
                `BusinessParking_validated` VARCHAR(128) DEFAULT NULL,\
                `BusinessParking_lot` VARCHAR(128) DEFAULT NULL,\
                `BusinessParking_valet` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_coloring` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_africanamerican` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_curly` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_perms` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_kids` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_extensions` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_asian` VARCHAR(128) DEFAULT NULL,\
                `HairSpecializesIn_straightperms` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsPriceRange2` VARCHAR(128) DEFAULT NULL,\
                `GoodForKids` VARCHAR(128) DEFAULT NULL,\
                `WheelchairAccessible` VARCHAR(128) DEFAULT NULL,\
                `BikeParking` VARCHAR(128) DEFAULT NULL,\
                `Alcohol` VARCHAR(128) DEFAULT NULL,\
                `HasTV` VARCHAR(128) DEFAULT NULL,\
                `NoiseLevel` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsAttire` VARCHAR(128) DEFAULT NULL,\
                `Music_dj` VARCHAR(128) DEFAULT NULL,\
                `Music_background_music` VARCHAR(128) DEFAULT NULL,\
                `Music_no_music` VARCHAR(128) DEFAULT NULL,\
                `Music_karaoke` VARCHAR(128) DEFAULT NULL,\
                `Music_live` VARCHAR(128) DEFAULT NULL,\
                `Music_video` VARCHAR(128) DEFAULT NULL,\
                `Music_jukebox` VARCHAR(128) DEFAULT NULL,\
                `Ambience_romantic` VARCHAR(128) DEFAULT NULL,\
                `Ambience_intimate` VARCHAR(128) DEFAULT NULL,\
                `Ambience_classy` VARCHAR(128) DEFAULT NULL,\
                `Ambience_hipster` VARCHAR(128) DEFAULT NULL,\
                `Ambience_divey` VARCHAR(128) DEFAULT NULL,\
                `Ambience_touristy` VARCHAR(128) DEFAULT NULL,\
                `Ambience_trendy` VARCHAR(128) DEFAULT NULL,\
                `Ambience_upscale` VARCHAR(128) DEFAULT NULL,\
                `Ambience_casual` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsGoodForGroups` VARCHAR(128) DEFAULT NULL,\
                `Caters` VARCHAR(128) DEFAULT NULL,\
                `WiFi` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsReservations` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsTakeOut` VARCHAR(128) DEFAULT NULL,\
                `HappyHour` VARCHAR(128) DEFAULT NULL,\
                `GoodForDancing` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsTableService` VARCHAR(128) DEFAULT NULL,\
                `OutdoorSeating` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsDelivery` VARCHAR(128) DEFAULT NULL,\
                `BestNights_monday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_tuesday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_friday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_wednesday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_thursday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_sunday` VARCHAR(128) DEFAULT NULL,\
                `BestNights_saturday` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_dessert` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_latenight` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_lunch` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_dinner` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_breakfast` VARCHAR(128) DEFAULT NULL,\
                `GoodForMeal_brunch` VARCHAR(128) DEFAULT NULL,\
                `CoatCheck` VARCHAR(128) DEFAULT NULL,\
                `Smoking` VARCHAR(128) DEFAULT NULL,\
                `DriveThru` VARCHAR(128) DEFAULT NULL,\
                `DogsAllowed` VARCHAR(128) DEFAULT NULL,\
                `BusinessAcceptsBitcoin` VARCHAR(128) DEFAULT NULL,\
                `Open24Hours` VARCHAR(128) DEFAULT NULL,\
                `BYOBCorkage` VARCHAR(128) DEFAULT NULL,\
                `BYOB` VARCHAR(128) DEFAULT NULL,\
                `Corkage` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_dairy` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_gluten` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_vegan` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_kosher` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_halal` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_soy` VARCHAR(128) DEFAULT NULL,\
                `DietaryRestrictions_vegetarian` VARCHAR(128) DEFAULT NULL,\
                `AgesAllowed` VARCHAR(128) DEFAULT NULL,\
                `RestaurantsCounterService` VARCHAR(128) DEFAULT NULL,\
                PRIMARY KEY(`business_id`) \
                )ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Business_hours'
            cursor.execute(sql)

            sql = 'CREATE TABLE Business_hours(\
                `business_id` VARCHAR(128) NOT NULL,\
                `Monday` VARCHAR(128) DEFAULT NULL,\
                `Wednesday` VARCHAR(128) DEFAULT NULL,\
                `Tuesday` VARCHAR(128) DEFAULT NULL,\
                `Friday` VARCHAR(128) DEFAULT NULL,\
                `Thursday` VARCHAR(128) DEFAULT NULL,\
                `Saturday` VARCHAR(128) DEFAULT NULL,\
                `Sunday` VARCHAR(128) DEFAULT NULL,\
                PRIMARY KEY (`business_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Checkin'
            cursor.execute(sql)

            sql = 'CREATE TABLE Checkin(\
                `business_id` VARCHAR(128) NOT NULL,\
                `weekday` VARCHAR(128) DEFAULT NULL,\
                `hour` TIME DEFAULT NULL,\
                `checkins` INT DEFAULT NULL\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Review'
            cursor.execute(sql)

            sql = 'CREATE TABLE Review(\
                `review_id` VARCHAR(128) NOT NULL,\
                `user_id` VARCHAR(128) DEFAULT NULL,\
                `business_id` VARCHAR(128) DEFAULT NULL,\
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
                `text` TEXT DEFAULT NULL,\
                `date` DATE DEFAULT NULL,\
                `likes` INT DEFAULT NULL,\
                `business_id` VARCHAR(128) NOT NULL,\
                `user_id` VARCHAR(128) NOT NULL\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;"
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS User'
            cursor.execute(sql)
            sql = 'CREATE TABLE User(\
                `user_id` VARCHAR(128) NOT NULL,\
                `name` VARCHAR(128) DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `yelping_since` DATE DEFAULT NULL,\
                `friends` LONGTEXT DEFAULT NULL,\
                `useful` INT DEFAULT NULL,\
                `funny` INT DEFAULT NULL,\
                `cool` INT DEFAULT NULL,\
                `fans` INT DEFAULT NULL,\
                `elite` VARCHAR(128) DEFAULT NULL,\
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
                `compliment_writer` INT DEFAULT NULL,\
                `compliment_photos` INT DEFAULT NULL,\
                PRIMARY KEY (`user_id`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

            sql = 'DROP TABLE IF EXISTS Elite'
            cursor.execute(sql)

            sql = 'CREATE TABLE Elite(\
                `user_id` VARCHAR(128) NOT NULL,\
                `elite` INT NOT NULL,\
                PRIMARY KEY (`user_id`,`elite`)\
                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;'
            cursor.execute(sql)

    finally:
        print("create table complete")
        connection.close()

# set up python on server
def main():
    # create tables
    create_tables()

if __name__ == '__main__':
    main()
