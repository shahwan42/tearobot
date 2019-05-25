BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `User` (
	`id`	INTEGER NOT NULL UNIQUE,
	`is_bot`	INTEGER NOT NULL DEFAULT 0,
	`is_admin`	INTEGER NOT NULL DEFAULT 0,
	`first_name`	TEXT NOT NULL,
	`last_name`	TEXT,
	`username`	TEXT UNIQUE,
	`language_code`	TEXT NOT NULL,
	`active`	INTEGER NOT NULL DEFAULT 1,
	`created`	INTEGER NOT NULL,
	`updated`	INTEGER NOT NULL,
	`last_command`	TEXT,
	`chat_id`	INTEGER DEFAULT NULL UNIQUE,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `Schedule` (
	`id`	INTEGER NOT NULL UNIQUE,
	`time`	VARCHAR NOT NULL,
	`subject`	VARCHAR NOT NULL,
	`day`	VARCHAR NOT NULL,
	PRIMARY KEY(`id`)
);
DELETE FROM `Schedule`;
INSERT INTO `Schedule` (id,time,subject,day) VALUES (1,'12:30','DSP Lecture','saturday'),
 (2,'10:10','Communications Lecture','saturday'),
 (3,'08:30','Communications Section','saturday'),
 (4,'14:10','Labs','sunday'),
 (5,'10:55','power electronics section','sunday'),
 (6,'10:10','OS section','sunday'),
 (7,'08:30','DSP Lecture','sunday'),
 (8,'10:55','computer organisation section','wednesday'),
 (9,'08:30','computer organisation lecture','wednesday'),
 (10,'10:10','power electronics lecture','tuesday'),
 (11,'08:30','os lecture','tuesday'),
 (12,'14:10','dsp section','monday'),
 (13,'12:30','communications lecture','monday'),
 (14,'10:10','measurements lecture','monday');
CREATE TABLE IF NOT EXISTS `Message` (
	`id`	INTEGER NOT NULL UNIQUE,
	`update_id`	INTEGER NOT NULL UNIQUE,
	`user_id`	INTEGER NOT NULL,
	`chat_id`	INTEGER NOT NULL,
	`date`	INTEGER NOT NULL,
	`text`	TEXT,
	PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `Announcement` (
	"id"			INTEGER PRIMARY KEY AUTOINCREMENT,
	"time"			VARCHAR NOT NULL,
	"description" 	TEXT,
	"done"			VARCHAR
);
COMMIT;
