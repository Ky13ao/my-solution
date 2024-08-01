
CREATE TABLE desserts (
    date_sold DATE,
    product VARCHAR(255),
    amount_sold INT
);

INSERT INTO desserts (date_sold, product, amount_sold) VALUES
('2022-06-01', 'Cake', 6),
('2022-06-01', 'Pie', 18),
('2022-06-02', 'Pie', 3),
('2022-06-02', 'Cake', 2),
('2022-06-03', 'Pie', 14),
('2022-06-03', 'Cake', 15),
('2022-06-04', 'Pie', 15),
('2022-06-04', 'Cake', 6),
('2022-06-05', 'Cake', 16),
('2022-06-05', 'Pie', NULL);
