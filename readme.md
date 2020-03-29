# Project Title

ECE656 Final project
Team: Weng Yu & Steven Qin

## Getting Started
This project contains a total of 4 major program scripts, each contain unique functionality.
table.py creates all table inside the database
yelp_script.py reads from dataset originated in csv, split and store fetched data into created tables properly 
Pro_table.sql elimiates duplicate and error entrys from csv, also adds necessary primary key to reinforce database structure.
API.py contain the API of the program.

### Prerequisites

What things you need to install the software and how to install them

Due to the size of the CSV files, this program is running on a remote server. 

### Server connection
```
IP address: 149.248.53.217
Password: $9Cjv}%z6}-5F$bB
```
### Running instruction 
Once inside the API, follow the steps to get a brief understanding. 
First enter you user Id, user id must exist in the database. If unknow, press enter to see an example user id.

As a user, you have 2 main function, Search and User home. 
Enter each function by enter the index (ex. 1 or 2) in the terminal.


## Search 

## User Home
Inside the home page, you can write review, follow group/topic, or read notification send from other users.
Once a review is posted by user, a notification will be sent to all the user's friend and group members who are in the same group with user. 

### Example

```
Post a review as user zYagTYoClQeP-7JxiTa7jw who is in group 6 and has friends 1T1x_58P-As_rB1mGITklw
Sign out and log back in as user 1T1x_58P-As_rB1mGITklw.
Press 3 the read 
new Post are shown one at a time and you can like each post by enter like. One user can Only like a post once. 
```

## Deployment

Original CSV can be found here https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6

## Built With

MySQL 8.0 + 
Python 3.7 +

## Authors

Weng Yu & Steven Qin


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
