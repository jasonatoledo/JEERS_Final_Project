CREATE TABLE fighters(
	fighter_id int primary key,
	fighter_name varchar,
	fighter_stance varchar,
	height_cms float,
	reach_cms float,
	weight_lbs int
)

SELECT * FROM fighters

CREATE TABLE fights (
    fight_id varchar PRIMARY KEY NOT NULL,
    winner char(4)   NOT NULL,
    title_bout char(5),
    weight_class varchar,
    no_of_rounds int,
    r_fighter varchar   NOT NULL,
    r_fighter_id int   NOT NULL,
	r_fighter_stance varchar,
    b_fighter varchar   NOT NULL,
    b_fighter_id int   NOT NULL,
	b_fighter_stance varchar,
    date date   NOT NULL,
    referee varchar,
    referee_id varchar
);

--DROP TABLE fights CASCADE;

-- Add foreign keys to the red and blue fighters columns
ALTER TABLE fights
	ADD CONSTRAINT fk_r_fighter_id
		FOREIGN KEY (r_fighter_id)
			REFERENCES fighters(fighter_id),
	ADD CONSTRAINT fk_b_fighter_id
		FOREIGN KEY (b_fighter_id)
			REFERENCES fighters(fighter_id);
-- Check fights table
SELECT * FROM fights

CREATE TABLE referees (
    referee_id varchar PRIMARY KEY  NOT NULL,
    referee_name varchar   NOT NULL
);

SELECT * FROM referees

CREATE TABLE records (
    records_id varchar(20) PRIMARY KEY  NOT NULL,
    fight_id varchar(20) NOT NULL,
    B_current_lose_streak INT,
    B_current_win_streak INT,
    B_draw INT,
    B_longest_win_streak INT,
    B_losses INT,
    B_total_title_bouts INT,
    B_win_by_Decision_Majority INT,
    B_win_by_Decision_Split INT,
    B_win_by_Decision_Unanimous INT,
    B_win_by_KO_TKO INT,
    B_win_by_Submission INT,
    B_win_by_TKO_Doctor_Stoppage INT,
    B_wins INT,
    B_total_rounds_fought INT,
    B_total_time_fought_seconds float,
    R_current_lose_streak INT,
    R_current_win_streak INT,
    R_draw INT,
    R_longest_win_streak INT,
    R_losses INT,
    R_total_rounds_fought INT,
    R_total_time_fought_seconds float,
    R_total_title_bouts INT,
    R_win_by_Decision_Majority INT,
    R_win_by_Decision_Split INT,
    R_win_by_Decision_Unanimous INT ,
    R_win_by_KO_TKO INT,
    R_win_by_Submission INT,
    R_win_by_TKO_Doctor_Stoppage INT,
    R_wins INT,
	CONSTRAINT fk_fight_id
		FOREIGN KEY (fight_id)
			REFERENCES fights(fight_id)
			ON DELETE SET NULL
);

-- Add foreign key to the records table fight id column
ALTER TABLE records
	ADD CONSTRAINT fk_records_fighter_id
		FOREIGN KEY (fight_id)
			REFERENCES fights(fight_id);

SELECT * FROM records

-- Table join with fights and fighters
SELECT DISTINCT(fight_id), 
	   winner, 
	   title_bout, 
	   weight_class,
	   no_of_rounds, 
	   r_fighter, 
	   r_fighter_id,
	   r_fighter_stance,
       b_fighter, 
       b_fighter_id,
	   b_fighter_stance,
       date, 
       Referee, 
       referee_id,
	   (SELECT height_cms
			  FROM fighters
			  WHERE fighters.fighter_id = fights.b_fighter_id
	   ) AS b_fighter_height,
	   (SELECT height_cms
			  FROM fighters
			  WHERE fighters.fighter_id = fights.r_fighter_id
	   ) AS r_fighter_height,
	   (SELECT reach_cms
			  FROM fighters
			  WHERE fighters.fighter_id = fights.b_fighter_id
	   ) AS b_fighter_reach,
	   (SELECT reach_cms
			  FROM fighters
			  WHERE fighters.fighter_id = fights.r_fighter_id
	   ) AS r_fighter_reach,
	   (SELECT weight_lbs
			  FROM fighters
			  WHERE fighters.fighter_id = fights.b_fighter_id
	   ) AS b_fighter_weight,
	   (SELECT weight_lbs
			  FROM fighters
			  WHERE fighters.fighter_id = fights.r_fighter_id
	   ) AS r_fighter_weight
FROM fighters
JOIN fights ON fights.b_fighter_id = fighters.fighter_id
ORDER BY date, r_fighter_id
