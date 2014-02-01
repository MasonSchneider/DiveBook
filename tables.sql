CREATE TABLE Divers (
	id SERIAL PRIMARY KEY,
	email VARCHAR(100) NOT NULL,
	hashpass CHAR(40) NOT NULL
);

CREATE TABLE Schools (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	division INT NOT NULL
);

CREATE TABLE DiveSheets (
	id SERIAL PRIMARY KEY,
	diverID INT REFERENCES Divers(id) ON DELETE CASCADE,
name VARCHAR(50) NOT NULL,
	meetID INT NULL, 
	finalScore NUMERIC(12,6) NULL
);

CREATE TABLE Profiles (
	diverID INT REFERENCES Divers(id) ON DELETE CASCADE,
	fName VARCHAR(50) NULL,
	lName VARCHAR(50) NULL,
	age INT NULL,
	favoriteDive INT NULL
);

CREATE TABLE Doable (
	diverID INT REFERENCES Divers(id) ON DELETE CASCADE,
	diveID INT REFERENCES Dives(id) ON DELETE CASCADE
);

CREATE TABLE Dives(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	number VARCHAR(5) NOT NULL,
	height INT NOT NULL,
	diveGroup VARCHAR(50) NOT NULL,
	position CHAR(1) NOT NULL,
	dd NUMERIC(6,3) NOT NULL
);


CREATE TABLE Meets (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	address VARCHAR(200) NULL,
	city VARCHAR(50) NOT NULL,
	state VARCHAR(2) NOT NULL,
	zip VARCHAR(5) NOT NULL,
	date DATE NOT NULL
);

CREATE TABLE Scores (
	sheetID INT REFERENCES DiveSheets(id) ON DELETE CASCADE,
	diveID INT REFERENCES Dives(id) ON DELETE CASCADE,
	score NUMERIC(12,6) NULL
);
