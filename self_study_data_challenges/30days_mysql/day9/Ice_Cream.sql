
CREATE TABLE ice_cream (
    `rank` INT,
    flavor VARCHAR(255),
    official_rating FLOAT,
    community_rating FLOAT
);

INSERT INTO ice_cream (`rank`, flavor, official_rating, community_rating) VALUES
(1, 'Vanilla', 9.5, 8),
(2, 'Mint Chocolate Chip', 9.4, 7),
(3, 'Chocolate', 9.3, 9.8),
(4, 'Pistachio', 8.7, 4.2),
(5, 'Cake Batter', 8.6, 9.1),
(6, 'Rocky Road', 8.4, 9.5),
(7, 'Moose Tracks', 8.4, 8.4),
(8, 'Cookie Dough', 8.2, 8.2),
(9, 'Salted Caramel', 8, 6.8),
(10, 'Cookies n'' Cream', 8, 8.8),
(11, 'Chocolate Swirl', 8, 7.7),
(12, 'Pistachio', 7.6, 7.6),
(13, 'Chocolate Chip', 7.2, 7.2),
(14, 'Cotton Candy', 7, 6.5),
(15, 'Strawberry Cheesecake', 7, 7.1),
(16, 'Matcha Green Tea', 7, 7),
(17, 'Bubblegum', 6.8, 6.8),
(18, 'Strawberry', 6.7, 7.2),
(19, 'Neapolitan', 6, 6),
(20, 'Butter Pecan', 3, 3);
