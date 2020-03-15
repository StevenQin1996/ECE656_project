import pymysql
import csv
import sys

csv.field_size_limit(sys.maxsize)


# change to be made later:
# 1. CML to control user name, password, and database
# 2. check if validation and handle wrong username/password
# 3. check database existance, create new database if need(if mistyped, then recommend an existing database similar to the entry)

def get_connection_key():
    connection_key = {'host': '149.248.59.2', 'port': 3306, 'username': 'steven', 'password': '00000000',
                      'database': 'Project'}
    return connection_key


def get_data_from_csv(myfile):
    with open(myfile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        my_data = []
        for row in enumerate(spamreader):
            my_data.append(row)
        # for row in spamreader:
        #     print(', '.join(row))
        return my_data


def setup_connection():
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
                `state` VARCHAR(5) DEFAULT NULL,\
                `postal_code` VARCHAR(10) DEFAULT NULL,\
                `latitude` DOUBLE DEFAULT NULL,\
                `longitude` DOUBLE DEFAULT NULL,\
                `stars` FLOAT DEFAULT NULL,\
                `review_count` INT DEFAULT NULL,\
                `is_open` Boolean DEFAULT NULL,\
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
                `DietaryRestrictions_vegetarian` Boolean DEFAULT ,\
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
    finally:
        connection.close()


# set up python on server
def main():
    # retrieve data
    file_business = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/yelp_dataset/csv/business.csv"
    file_checkin = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/yelp_dataset/csv/checkin.csv"
    file_review = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/yelp_dataset/csv/review.csv"
    file_tip = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/yelp_dataset/csv/tip.csv"
    file_user = "/Users/shiyunqin/Desktop/Homework/graduate/ece656/project/yelp_dataset/csv/user.csv"

    business = get_data_from_csv(file_business)

    # for count1, count2 in zip(business[0][1], business[1][1]):
    #     print("{}:     {}".format(count1, count2))

    # setup connection
    setup_connection()


if __name__ == '__main__':
    main()
