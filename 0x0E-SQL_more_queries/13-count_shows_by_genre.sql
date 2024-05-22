-- The script lists all genres contained in the 'hbtn_0d' database and the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- Results are sorted in descending order by the number of shows linked to each genre.
-- The database name will be provided as an argument to the mysql command.

SELECT name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
