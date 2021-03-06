<h1 align="center">0x0E. SQL - More queries</h1>


## General

Concepts to learn in this project about SQL - More queries:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Task Project
---
File Name|Task Name|Task Description
---|---|---
[0-privileges.sql](...)|0. My privileges! |Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
[1-create_user.sql](...)|1. Root user|Script that creates the MySQL server user user_0d_1.
[2-create_read_user.sql](...)|2. Read user|Script that creates the database hbtn_0d_2 and the user user_0d_2.
[3-force_name.sql](...)|3. Always a name|Script that creates the table force_name on your MySQL server.
[4-never_empty.sql](...)|4. ID can't be null|Script that creates the table id_not_null on your MySQL server.
[5-unique_id.sql](...)|5. Unique ID|Script that creates the table unique_id on your MySQL server.
[6-states.sql](...)|6. States table|Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
[7-cities.sql](...)|7. Cities table|Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
[8-cities_of_california_subquery.sql](...)|8. Cities of California|Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
[9-cities_by_state_join.sql](...)|9. Cities by States|Script that lists all cities contained in the database hbtn_0d_usa.
[10-genre_id_by_show.sql](...)|10. Genre ID by show|Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
[11-genre_id_all_shows.sql](...)|11. Genre ID for all shows|Write a script that lists all shows contained in the database hbtn_0d_tvshows.
[12-no_genre.sql](...)|12. No genre|Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
[13-count_shows_by_genre.sql](...)|13. Number of shows by genre|Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
[14-my_genres.sql](...)|14. My genres|Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
[15-comedy_only.sql]()|15-comedy_only.sql|Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
[16-shows_by_genre.sql]()|16. List shows and genres|Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
