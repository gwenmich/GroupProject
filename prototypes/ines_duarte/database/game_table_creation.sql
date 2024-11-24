-- create a Database
CREATE DATABASE IF NOT EXISTS thesis_quest_game;

-- Selected a the database being used
USE thesis_quest_game; 

-- Create a player table and make the player user name unique to simplify player identification
CREATE TABLE IF NOT EXISTS player_table (
	player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_user_name VARCHAR(250) NOT NULL UNIQUE
);

-- scores table connects to player ID via the Foreign Key and saves the time, and stars as well as the date 
CREATE TABLE IF NOT EXISTS scores (
	game_score_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,
    game_final_time TIME NOT NULL,
    game_score VARCHAR(250) NOT NULL,
    game_date DATETIME NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player_table(player_id)
);


-- Not sure if we'll implement this, but this will save the necessary variables to load the game, such as sprite position and 
CREATE TABLE IF NOT EXISTS game_saves (
	game_save_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,
    game_time TIME NOT NULL,
    hero_sprite_position_x INT NOT NULL,
    hero_sprite_position_y INT NOT NULL,
    challenges_won INT NOT NULL,
    stress_level INT NOT NULL,
    game_date DATETIME NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player_table(player_id)
);

