-- This script lists all shows contained in the database 'hbtn_0d_tvshows'.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- If a show doesn’t have a genre, it displays NULL.
-- The database name will be provided as an argument to the mysql command.

SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
