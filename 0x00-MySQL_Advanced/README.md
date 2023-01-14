# Advanced MySQL features

- `0-uniq_users.sql`: contains a SQL script that creates a table users with the attributes:
id, integer, never null, auto increment and primary key.
email, string (255 characters), never null and unique.
name, string (255 characters).
- `1-country_users.sql`: contains a SQL script that creates a table users with the attributes:
id, integer, never null, auto increment and primary key.
email, string (255 characters), never null and unique.
name, string (255 characters).
country, enumeration of countries: US, CO and TN, never null (default value will be the first element of the enumeration, which is US).
- `2-fans.sql`: contains a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.
- `3-glam_rock.sql`: contains a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.
- `4-store.sql`: contains a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
- `5-valid_email.sql`: contains a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
- `6-bonus.sql`: contains a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
- `7-average_score.sql`: contains a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
- `8-index_my_names.sql`: contains a SQL script that creates an index idx_name_first on the table names and the first letter of name. Only the first letter of name must be indexed.
- `9-index_name_score.sql`: contains a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score. Only the first letter of name AND score must be indexed.
- `10-div.sql`: contains a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
- `11-need_meeting.sql`: contains a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
- `100-average_weighted_score.sql`: contains a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.
- `101-average_weighted_score.sql`: contains a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
