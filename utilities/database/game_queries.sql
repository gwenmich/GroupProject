SELECT * FROM players;
SELECT * FROM scores;

SELECT sc.game_final_time, sc.game_score, pl.user_name
FROM scores sc
JOIN players pl ON sc.player_id = pl.player_id
ORDER BY sc.game_final_time ASC
LIMIT 10;