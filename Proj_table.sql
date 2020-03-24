DROP TABLE IF EXISTS Group_info;
CREATE TABLE Groups_info(
	`group_id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(255) DEFAULT NULL,
	PRIMARY KEY (`group_id`)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS User_Group;
CREATE TABLE User_Group(
	`user_id` VARCHAR(255) NOT NULL,
	`group_id` INT NOT NULL,
	PRIMARY KEY (`user_id`,`group_id`)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS Friends;
CREATE TABLE Friends(
	`user_id` VARCHAR(255) DEFAULT NULL,
	`friend_id` VARCHAR(255) DEFAULT NULL
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS temp_Category;
CREATE TABLE temp_Category(
	`business_id` VARCHAR(255) NOT NULL,
	`category` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`business_id`, `category`)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

INSERT INTO temp_Category(business_id,category) SELECT * FROM Category GROUP BY business_id, category;

DROP TABLE Category;

RENAME TABLE temp_Category TO Category;

DROP TABLE IF EXISTS temp_Friends;
CREATE TABLE temp_Friends(
	`user_id` VARCHAR(255) NOT NULL,
	`friend_id` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`user_id`, `friend_id`)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS temp2_Friends;
CREATE TABLE temp2_Friends(
	`user_id` VARCHAR(255) DEFAULT NULL,
	`friend_id` VARCHAR(255) DEFAULT NULL
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


INSERT INTO temp_Friends(user_id,friend_id) SELECT F.user_id, F.friend_id FROM Friends F INNER JOIN User U ON F.friend_id = U.user_id GROUP BY F.user_id, F.friend_id;

DROP TABLE IF EXISTS Friends;
CREATE TABLE Friends(
	`user_id` VARCHAR(255) DEFAULT NULL,
	`friend_id` VARCHAR(255) DEFAULT NULL
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS Notification;
CREATE TABLE Notification(
	`notification_id` INT NOT NULL AUTO_INCREMENT,
	`review_id` VARCHAR(128) DEFAULT NULL,
	`reviewbusiness_id` VARCHAR(128) DEFAULT NULL,
	`reviewuser_id` VARCHAR(128) DEFAULT NULL,
	`user_id` VARCHAR(128) DEFAULT NULL,
	`is_read` BOOLEAN DEFAULT NULL,
	PRIMARY KEY (`notification_id`)
)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;


DROP TABLE IF EXISTS temp_Review;
CREATE TABLE temp_Review(
    `review_id` VARCHAR(128) NOT NULL,
    `user_id` VARCHAR(128) DEFAULT NULL,
    `business_id` VARCHAR(128) DEFAULT NULL,
    `stars` INT DEFAULT NULL,
    `date` DATE,
    `text` TEXT DEFAULT NULL,
    `useful` INT DEFAULT NULL,
    `funny` INT DEFAULT NULL,
    `cool` INT DEFAULT NULL,
    PRIMARY KEY (`review_id`)
    )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

INSERT INTO temp_Review(review_id,user_id,business_id,stars,useful,funny,cool,text,date) 
SELECT R.review_id,R.user_id,R.business_id,R.stars,R.useful,R.funny,R.cool,R.text,R.date FROM Review R INNER JOIN User U ON R.user_id = U.user_id;


ALTER TABLE Checkin ADD `Checkin_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Tips ADD `tip_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;


ALTER TABLE Business_hours ADD CONSTRAINT Business_hours_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Business_attributes ADD CONSTRAINT Business_attribute_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Category ADD CONSTRAINT Business_category_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Checkin ADD CONSTRAINT Business_checkin_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Friends ADD CONSTRAINT User_friend_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Elite ADD CONSTRAINT User_elite_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE User_Group ADD CONSTRAINT User_Group_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE User_Group ADD CONSTRAINT Group_User_FK FOREIGN KEY (group_id) REFERENCES Groups_info(group_id) on delete restrict on update restrict;

ALTER TABLE Tips ADD CONSTRAINT Tips_Business_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Tips ADD CONSTRAINT Tips_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Review ADD CONSTRAINT Review_Business_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Review ADD CONSTRAINT Review_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_Review_FK FOREIGN KEY (review_id) REFERENCES Review(review_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_ReviewBusiness_FK FOREIGN KEY (reviewbusiness_id) REFERENCES Review(business_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_ReviewUser_FK FOREIGN KEY (reviewuser_id) REFERENCES Review(user_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;




