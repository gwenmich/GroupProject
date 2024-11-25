SELECT * FROM players;
SELECT * FROM scores;

-- query to show top 10 high scores  ordered by time
SELECT sc.game_final_time, sc.game_score, pl.user_name
FROM scores sc
JOIN players pl ON sc.player_id = pl.player_id
ORDER BY sc.game_final_time ASC
-- limit 10 to show top 10 scores 
LIMIT 10;


-- procedure containing a transaction to save a game score 
DELIMITER //
CREATE PROCEDURE Save_High_Score(IN new_user_name VARCHAR(255), IN game_final_time VARCHAR(255), IN game_score VARCHAR(255)
)
	BEGIN
    START TRANSACTION;
-- Insert the user into the players table if they do not exist
        IF NOT EXISTS (SELECT user_name FROM players WHERE user_name = new_user_name) THEN
            INSERT INTO players (user_name)
            VALUES 
            (new_user_name);
        END IF;

	INSERT INTO scores (player_id, game_final_time, game_score, game_date)
	VALUES
    -- this will dynamically insert the correct Foreign Key ID that matched the user_name
	-- DEFAULT gives it the current timestamp as that's the setting on table creation
	((SELECT player_id FROM players WHERE user_name = new_user_name), game_final_time, game_score, DEFAULT);

	COMMIT;

END //

DELIMITER ;

-- Calling the procedure and passing the player name, star score and time
CALL Save_High_Score('TEST_PERSON_2', '00:00', 'test Stars');

-- DROP PROCEDURE Save_High_Score;

SELECT sc.game_final_time, sc.game_score, sc.game_date, pl.user_name
FROM scores sc
JOIN players pl ON sc.player_id = pl.player_id
ORDER BY sc.game_final_time ASC;
