
CREATE TABLE transactions (
    transaction_id INT,
    country VARCHAR(255),
    state VARCHAR(255),
    amount INT,
    transaction_date DATE
);

INSERT INTO transactions (transaction_id, country, state, amount, transaction_date) VALUES
(1, 'Canada', 'Approved', 100000, '2012-05-25'),
(2, 'Canada', 'Declined', 87000, '2019-06-18'),
(3, 'Canada', 'Approved', 250000, '2011-10-25'),
(4, 'Canada', 'Approved', 45000, '2019-09-19'),
(5, 'Canada', 'Approved', 1500, '1995-06-16'),
(6, 'Canada', 'Declined', 10000000, '2020-09-25'),
(7, 'Canada', 'Approved', 15000, '2022-01-01'),
(8, 'Canada', 'Approved', 20000, '2012-05-25'),
(9, 'Canada', 'Declined', 34000, '2019-03-18'),
(10, 'Canada', 'Approved', 75000, '2011-05-25'),
(11, 'Canada', 'Approved', 540000, '2019-09-19'),
(12, 'Canada', 'Approved', 4100, '1995-08-16'),
(13, 'Canada', 'Declined', 1000, '2020-09-25'),
(14, 'Canada', 'Approved', 420000, '2022-01-01'),
(15, 'Canada', 'Declined', 123000, '2020-09-25'),
(16, 'Canada', 'Approved', 708500, '2021-01-01'),
(17, 'Canada', 'Approved', 4000, '2012-05-25'),
(18, 'Canada', 'Declined', 3000, '2019-03-18'),
(19, 'Canada', 'Approved', 63300, '2011-04-25'),
(20, 'Canada', 'Approved', 63000, '2019-07-19'),
(21, 'Canada', 'Approved', 2000, '1995-08-16'),
(22, 'Canada', 'Approved', 630000, '2011-11-25');
