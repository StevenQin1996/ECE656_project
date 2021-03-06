
INSERT INTO temp_Category(business_id,category) SELECT * FROM Category GROUP BY business_id, category;
DROP TABLE Category;
RENAME TABLE temp_Category TO Category;

INSERT INTO temp_Friends(user_id,friend_id) SELECT F.user_id, F.friend_id FROM Friends F INNER JOIN User U ON F.friend_id = U.user_id GROUP BY F.user_id, F.friend_id;
DROP TABLE Friends;
RENAME TABLE temp_Friends TO Friends;


INSERT INTO temp_Review(review_id,user_id,business_id,stars,useful,funny,cool,text,date) SELECT R.review_id,R.user_id,R.business_id,R.stars,R.useful,R.funny,R.cool,R.text,R.date FROM Review R INNER JOIN User U ON R.user_id = U.user_id;
DROP TABLE Review;
RENAME TABLE temp_Review TO Review;

INSERT INTO Follow(business_id) SELECT business_id FROM Business;

ALTER TABLE Checkin ADD `Checkin_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Tips ADD `tip_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Business_hours ADD CONSTRAINT Business_hours_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Business_attributes ADD CONSTRAINT Business_attribute_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Category ADD CONSTRAINT Business_category_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Checkin ADD CONSTRAINT Business_checkin_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Friends ADD CONSTRAINT User_friend_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Elite ADD CONSTRAINT User_elite_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE User_Group ADD CONSTRAINT User_Group_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE User_Group ADD CONSTRAINT Group_User_FK FOREIGN KEY (group_id) REFERENCES Group_info(group_id) on delete restrict on update restrict;

ALTER TABLE Follow ADD CONSTRAINT Follow_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Follow ADD CONSTRAINT Follow_Business_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Tips ADD CONSTRAINT Tips_Business_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Tips ADD CONSTRAINT Tips_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Review ADD CONSTRAINT Review_Business_FK FOREIGN KEY (business_id) REFERENCES Business(business_id) on delete restrict on update restrict;

ALTER TABLE Review ADD CONSTRAINT Review_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_Review_FK FOREIGN KEY (review_id) REFERENCES Review(review_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_ReviewBusiness_FK FOREIGN KEY (reviewbusiness_id) REFERENCES Review(business_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_ReviewUser_FK FOREIGN KEY (reviewuser_id) REFERENCES Review(user_id) on delete restrict on update restrict;

ALTER TABLE Notification ADD CONSTRAINT Note_User_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;

ALTER TABLE like_review ADD CONSTRAINT like_review_FK FOREIGN KEY (review_id) REFERENCES Review(review_id) on delete restrict on update restrict;

ALTER TABLE like_review ADD CONSTRAINT like_user_FK FOREIGN KEY (user_id) REFERENCES User(user_id) on delete restrict on update restrict;




