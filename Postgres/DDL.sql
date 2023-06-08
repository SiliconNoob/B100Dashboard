CREATE TABLE song(
	Title VARCHAR(50),
	Author VARCHAR(100),
	peak_pos INT,
	PRIMARY KEY (Title, Author)
);

CREATE TABLE weeklyChartDate(
	chart_week DATE PRIMARY KEY
);

CREATE TABLE appearsIn(
	Title VARCHAR(50),
	Author VARCHAR(100),
	chart_week DATE,
	position INT,
	num_weeks INT,
	FOREIGN KEY (Title, Author) REFERENCES song(Title,Author),
	PRIMARY KEY (Title, Author, chart_week)
);