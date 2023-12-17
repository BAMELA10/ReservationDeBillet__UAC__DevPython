import mysql.connector as myc

connector = myc.connect( host="localhost",
                        port="3306",
                        user="root",
                        database="",
                        password="")
curseur = connector.cursor()
curseur.execute("create database if not exists data2 ")
curseur.execute("use data2")
curseur.execute("create table if not exists Users (id int AUTO_INCREMENT primary key, username varchar(32), email varchar(32), password varchar(256), phone int , status varchar(32))")
curseur.execute("create table if not exists Event (id int AUTO_INCREMENT primary key, code varchar(10) unique, intitulé varchar(32), date_event date, number_place int)")
curseur.execute("create table if not exists Reservation (id int AUTO_INCREMENT primary key, code varchar(10) unique, date_reservation date, status_reservation varchar(10) NOT NULL DEFAULT 'considéré', id_event int, foreign key(id_event) references Event(id), id_users int, foreign key(id_users) references Users(id))")
