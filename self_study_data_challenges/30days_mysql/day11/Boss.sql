
CREATE TABLE boss (
    employee_id INT,
    employee_name VARCHAR(255),
    boss_id VARCHAR(255) -- using VARCHAR to accommodate NULL values
);

INSERT INTO boss (employee_id, employee_name, boss_id) VALUES
(1, 'Josh Harper', NULL),
(2, 'Carolina Fancis', NULL),
(3, 'Gerald Butler', '2'),
(4, 'Richie Rich', '3'),
(5, 'Carol Danvers', NULL),
(6, 'Peter McMillan', '2'),
(7, 'Sarah Burdauch', '5'),
(8, 'Donald Glover', NULL);
