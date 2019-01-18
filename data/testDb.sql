-- sqlite3 testing.db < createdb.sql

create table "Children" (
	"ChildId" integer not null primary key,
	"Name" string not null,
	"NaughtyOrNice" string not null
);

create table "Gifts" (
	"GiftId" integer not null primary key,
	"Name" string not null,
	"Delivered" integer not null,
	"ChildId" integer not null,
	foreign key ("ChildId")
	References "Children" ("ChildId")
	On delete cascade
);