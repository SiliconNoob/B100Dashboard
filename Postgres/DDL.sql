CREATE TABLE song(
	position INT,
	title VARCHAR(50),
	authors VARCHAR(100),
	last_week_position INT,
	peak_position INT,
	num_weeks_on_chart INT,
	chart_date DATE,
    PRIMARY KEY(title, authors, chart_date)
);

CREATE TABLE dates_on_chart(
	title VARCHAR(50),
	authors VARCHAR(100),
    chart_date DATE,
    FOREIGN KEY (title, authors) REFERENCES song(title, authors),
    PRIMARY KEY(title, authors,chart_date)
);

CREATE TABLE song_author(
	author_name VARCHAR(100) UNIQUE
);