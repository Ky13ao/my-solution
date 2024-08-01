
CREATE TABLE sessions (
    user_id INT,
    session_id INT,
    minutes_per_session INT,
    activity VARCHAR(255)
);

INSERT INTO sessions (user_id, session_id, minutes_per_session, activity) VALUES
(1, 1, 44, 'Gaming'),
(1, 1, 27, 'Homework'),
(1, 1, 25, 'YouTube'),
(2, 7, 37, 'Gaming'),
(2, 6, 23, 'Gaming'),
(3, 5, 88, 'Homework'),
(3, 5, 85, 'Homework'),
(3, 4, 76, 'Homework'),
(4, 3, 88, 'YouTube'),
(4, 3, 57, 'Gaming'),
(4, 2, 32, 'Gaming'),
(4, 2, 98, 'YouTube');
