CREATE DATABASE IF NOT EXISTS thesis_quest_game;

USE thesis_quest_game; 

CREATE TABLE IF NOT EXISTS player_table (
	player_id INT PRIMARY KEY AUTO_INCREMENT,
    player_name VARCHAR(250) NOT NULL
);


CREATE TABLE IF NOT EXISTS high_scores (
	game_score_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,
    game_final_time TIME NOT NULL,
    game_score VARCHAR(250) NOT NULL,
    game_date DATETIME NOT NULL,
    FOREIGN KEY (player_id) REFERENCES player_table(player_id)
);


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

