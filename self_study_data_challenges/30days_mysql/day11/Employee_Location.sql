
CREATE TABLE employee_location (
    employee_id INT,
    city VARCHAR(255),
    state VARCHAR(255),
    state_id VARCHAR(2)
);

INSERT INTO employee_location (employee_id, city, state, state_id) VALUES
(1, 'Charlotte', 'North Carolina', 'NC'),
(3, 'Austin', 'Texas', 'TX'),
(4, 'New York', 'New York', 'NY');
