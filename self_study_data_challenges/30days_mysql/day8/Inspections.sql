
CREATE TABLE inspections (
    owner_name VARCHAR(255),
    vehicle VARCHAR(255),
    minor_issues INT,
    critical_issues INT
);

INSERT INTO inspections (owner_name, vehicle, minor_issues, critical_issues) VALUES
('Jim', '2012 Ford Fusion', 3, 0),
('Mikaela', '2021 Dodge Stratus', 2, 0),
('Karen', '2008 Ford Escape', 5, 0),
('Michael', '2021 Kia Telluride', 2, 1),
('Sally', '2023 Tesla Model S', 0, 0),
('Joseph', '2015 Toyota Highlander', 2, 0),
('David', '1998 Ford F-150', 2, 0),
('Lauren', '2004 Honda Pilot', 4, 0),
('Chuck', '2016 Buick Enclave', 0, 1),
('Caleb', '2007 Toyota Forerunner', 4, 0),
('Hannah', '2018 Honda Accord', 2, 0);
