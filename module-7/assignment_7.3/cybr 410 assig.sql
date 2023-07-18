/*
Pysports Database Tables
Author: Rick McArdle
Assignment: 7.3
*/
use pysports;

create table team (
	team_id int not null auto_increment,
    team_name varchar (255) not null, 
    mascot varchar (255) not null,
    constraint pk_team primary key (team_id)
);

create table player (
	player_Id int not null,
    first_name varchar (255) not null,
    last_name varchar (255) not null,
    team_id int null, 
    constraint pk_player primary key (player_id), 
    constraint fk_player_team foreign key (team_id) references team (team_id)
);


    
    