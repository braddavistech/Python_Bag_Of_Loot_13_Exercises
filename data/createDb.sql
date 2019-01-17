-- sqlite3 santa.db < createdb.sql

create table "Children" (
	"ChildId" integer not null primary key autoincrement,
	"Name" string not null,
	"NaughtyOrNice" string not null
);

create table "Gifts" (
	"GiftId" integer not null primary key autoincrement,
	"Name" string not null,
	"Delivered" integer not null,
	"Month" string not null,
	"Day" string not null,
	"Year" string not null,
	"ChildId" integer not null,
	foreign key ("ChildId")
	References "Children" ("ChildId")
	On delete cascade
);