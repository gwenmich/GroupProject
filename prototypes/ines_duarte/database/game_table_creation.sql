-- create a Database
CREATE DATABASE IF NOT EXISTS thesis_quest_game;

-- DROP DATABASE thesis_quest_game;

-- Selected a the database being used
USE thesis_quest_game; 

-- Create a player table and make the player user name unique to simplify player identification
CREATE TABLE IF NOT EXISTS players (
	player_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(250) NOT NULL UNIQUE
);

-- scores table connects to player ID via the Foreign Key and saves the time, and stars as well as the date 
CREATE TABLE IF NOT EXISTS scores (
	game_score_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,
    game_final_time VARCHAR(250) NOT NULL,
    game_score VARCHAR(250) NOT NULL,
    game_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

-- Not sure if we'll implement this, but this will save the necessary variables to load the game, 
-- such as sprite position and meter values at the time of the save
CREATE TABLE IF NOT EXISTS game_saves (
	game_save_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,
    game_time TIME NOT NULL,
    hero_sprite_position_x INT NOT NULL,
    hero_sprite_position_y INT NOT NULL,
    challenges_won INT NOT NULL,
    stress_level INT NOT NULL,
    game_date DATETIME NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);


-- Inserting values to populate tables
INSERT INTO players
-- stating the field each value is suppose to go into 
(user_name)
VALUES
('inesD'),
('SuperGM'),
('just_GRACE'),
('Em_B'),
('JMG'),
('tiGGy'),
('PinkEmma'),
('Fatihah'),
('Jedi_Luke'),
('wizard_HAMED'),
('Arianne_40K');


INSERT INTO scores (player_id, game_final_time, game_score, game_date)
VALUES
((SELECT player_id FROM players WHERE user_name = 'inesD'), '18:30', '4 Stars', '2024-11-01 14:30:00'),
((SELECT player_id FROM players WHERE user_name = 'SuperGM'), '13:45', '4 Stars', '2024-11-02 15:00:00'),
((SELECT player_id FROM players WHERE user_name = 'just_GRACE'), '09:10', '5 Stars', '2024-11-03 16:00:00'),
((SELECT player_id FROM players WHERE user_name = 'Em_B'), '28:50', '3 Stars', '2024-11-04 17:00:00'),
((SELECT player_id FROM players WHERE user_name = 'JMG'), '08:55', '5 Stars', '2024-11-05 18:00:00'),
((SELECT player_id FROM players WHERE user_name = 'tiGGy'), '16:40', '4 Stars', '2024-11-06 19:00:00'),
((SELECT player_id FROM players WHERE user_name = 'PinkEmma'), '22:00', '3 Stars', '2024-11-07 20:00:00'),
((SELECT player_id FROM players WHERE user_name = 'Fatihah'), '11:50', '4 Stars', '2024-11-04 17:00:00'),
((SELECT player_id FROM players WHERE user_name = 'Jedi_Luke'), '21:55', '3 Stars', '2024-11-05 18:00:00'),
((SELECT player_id FROM players WHERE user_name = 'wizard_HAMED'), '07:40', '5 Stars', '2024-11-06 19:00:00'),
((SELECT player_id FROM players WHERE user_name = 'Arianne_40K'), '17:00', '4 Stars', '2024-11-07 20:00:00');


