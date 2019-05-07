BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Message" (
	"id"	INTEGER NOT NULL UNIQUE,
	"update_id"	INTEGER NOT NULL UNIQUE,
	"user_id"	INTEGER NOT NULL,
	"chat_id"	INTEGER NOT NULL,
	"date"	INTEGER NOT NULL,
	"text"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "User" (
	"id"	INTEGER NOT NULL UNIQUE,
	"is_bot"	INTEGER NOT NULL DEFAULT 0,
	"is_admin"	INTEGER NOT NULL DEFAULT 0,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT,
	"username"	TEXT UNIQUE,
	"language_code"	TEXT NOT NULL,
	"active"	INTEGER NOT NULL DEFAULT 1,
	"created"	INTEGER NOT NULL,
	"updated"	INTEGER NOT NULL,
	"last_command"	TEXT,
	"chat_id"	INTEGER,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Schedule" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"time"	INTEGER NOT NULL,
	"saturday"	TEXT,
	"sunday"	TEXT,
	"monday"	TEXT,
	"tuesday"	TEXT,
	"wednesday"	TEXT,
	"thursday"	TEXT
);
CREATE TABLE IF NOT EXISTS "Announcement" (
	"id"			INTEGER PRIMARY KEY AUTOINCREMENT,
	"time"			INTEGER,
	"description" 	TEXT,
	"cancelled"		INTEGER
);
COMMIT;
