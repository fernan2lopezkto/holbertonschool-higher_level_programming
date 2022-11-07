-- tv shows

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.genre_id = genre_id;