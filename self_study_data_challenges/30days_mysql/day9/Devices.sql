
CREATE TABLE devices (
    device_id INT,
    date_played DATE,
    game VARCHAR(255)
);

INSERT INTO devices (device_id, date_played, game) VALUES
(1, '2022-03-08', 'Dota2'),
(1, '2019-02-16', 'League of Legends'),
(1, '2021-01-27', 'Dota2'),
(1, '2020-09-05', 'League of Legends'),
(2, '2019-05-04', 'Dota2'),
(2, '2021-11-15', 'Dota2'),
(2, '2020-09-05', 'Dota2'),
(3, '2022-10-02', 'League of Legends'),
(3, '2019-06-15', 'Dota2');
