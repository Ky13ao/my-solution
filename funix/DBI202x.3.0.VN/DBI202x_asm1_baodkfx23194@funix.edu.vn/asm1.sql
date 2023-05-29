-- https://courses.funix.edu.vn/courses/course-v1:FUNiX+DBI202x.3.0.VN+1122.SE/courseware/fdc6e8ea302049aaa4b26ecec067377d/751dd6bf9e0d414398fca43fe3675f48/?child=first

-- 1. Truy vấn first_name, last_name, job_id và salary của các nhân viên có tên bắt đầu bằng chữ “S”
SELECT first_name, last_name, job_id, salary
FROM employees
WHERE left(first_name,1)='S';

-- 2. 2. Viết truy vấn để tìm các nhân viên có số lương (salary) cao nhất
SELECT employee_id, first_name, last_name, job_id, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 3. Viết truy vấn để tìm các nhân viên có số lương lớn thứ hai. Ví dụ có 5 nhân viên có mức lương lần lượt là 4, 4, 3, 3, 2 thì kết quả  đúng của mức lương lớn thứ hai sẽ là 3,3
SELECT employee_id, first_name, last_name, job_id, salary
FROM employees
WHERE salary = (SELECT salary FROM employees GROUP BY salary ORDER BY salary DESC LIMIT 1, 1);

-- 4. Viết truy vấn để tìm các nhân viên có số lương lớn thứ ba. Tương tự như yêu cầu 3
SELECT employee_id, first_name, last_name, job_id, salary
FROM employees
WHERE salary = (SELECT salary FROM employees GROUP BY salary ORDER BY salary DESC LIMIT 2, 1);

-- 5. Viết truy vấn để hiển thị mức lương của nhân viên cùng với người quản lý tương ứng, tên nhân viên và quản lý kết hợp từ first_name và last_name
SELECT
CONCAT_WS(' ',e.first_name, e.last_name) employee,
e.salary emp_sal, 
CONCAT_WS(' ', m.first_name, m.last_name) manager, 
m.salary mgr_sal
FROM employees e
INNER JOIN employees m ON e.manager_id = m.employee_id;

-- 6. Viết truy vấn để tìm số lượng nhân viên cần quản lý của mỗi người quản lý, tên quản lý kết hợp từ first_name và last_name
SELECT
m.employee_id,
CONCAT_WS(' ', m.first_name, m.last_name) manager_name, 
COUNT(e.employee_id) number_of_reportees
FROM employees m
INNER JOIN employees e ON e.manager_id = m.employee_id
GROUP BY m.employee_id
ORDER BY number_of_reportees DESC;

-- 7. Viết truy vấn để tìm được số lượng nhân viên trong mỗi phòng ban sắp xếp theo thứ tự số nhân viên giảm dần
SELECT
d.department_name, 
COUNT(e.employee_id) number_of_reportees
FROM departments d
INNER JOIN employees e ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY number_of_reportees DESC;

-- 8. Viết truy vấn để tìm số lượng nhân viên được thuê trong mỗi năm sắp xếp theo thứ tự số lương nhân viên giảm dần và nếu số lượng nhân viên bằng nhau thì sắp xếp theo năm tăng dần
SELECT 
YEAR(hire_date) hired_year, 
COUNT(employee_id) employees_hired_count
FROM employees
GROUP BY hired_year
ORDER BY employees_hired_count DESC;

-- 9. 9. Viết truy vấn để lấy mức lương lớn nhất, nhỏ nhất và mức lương trung bình của các nhân viên (làm tròn mức lương trung bình về số nguyên)
SELECT 
MIN(salary) min_sal,
MAX(salary) max_sal,
ROUND(AVG(salary), 0) avg_sal
FROM employees;

-- 10. Viết truy vấn để chia nhân viên thành ba nhóm dựa vào mức lương, tên nhân viên được kết hợp từ first_name và last_name, kết quả sắp xếp theo tên thứ tự tăng dần
SELECT
CONCAT_WS(' ', first_name, last_name) employee,
salary,
CASE WHEN salary < 5000 THEN 'low'
    WHEN salary < 10000 THEN 'medium'
    ELSE 'high' END salary_level
FROM employees;

-- 11. Viết truy vấn hiển thị họ tên nhân viên và số điện thoại theo định dạng (_ _ _)-(_ _ _)-(_ _ _ _). Tên nhân viên kết hợp từ first_name và last_name, kết quả hiển thị như hình vẽ dưới đây
SELECT
CONCAT_WS(' ', first_name, last_name) employee,
REPLACE(phone_number, '.', '-') phone_number
FROM employees;

-- Viết truy vấn để tìm các nhân viên gia nhập vào tháng 08-1994, tên nhân viên kết hợp từ first_name và last_name
SELECT
CONCAT_WS(' ', first_name, last_name) employee,
hire_date
FROM employees
WHERE LEFT(hire_date, 7)='1994-08';

-- 13. Viết truy vấn để tìm những nhân viên có mức lương cao hơn mức lương trung bình của các nhân viên, kết quả sắp xếp theo thứ tự tăng dần của department_id
SELECT 
CONCAT(first_name, last_name) name, 
employee_id,
(SELECT d.department_name FROM departments d WHERE d.department_id=employees.department_id) department,
department_id,
salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC;

-- Viết truy vấn để tìm mức lương lớn nhất ở mỗi phòng ban, kết quả sắp xếp theo thứ tự tăng dần của department_id
SELECT
d.department_id,
d.department_name, 
MAX(e.salary) maximum_salary
FROM departments d
INNER JOIN employees e ON e.department_id = d.department_id
GROUP BY d.department_name
ORDER BY d.department_id ASC;

-- 15. Viết truy vấn để tìm 5 nhân viên có mức lương thấp nhất
SELECT first_name, last_name, employee_id, salary
FROM employees
ORDER BY salary ASC
LIMIT 5;

-- 16. Viết truy vấn để hiển thị tên nhân viên theo thứ tự ngược lại
SELECT LOWER(first_name) name, REVERSE(LOWER(first_name)) name_in_reverse
FROM employees;

-- 17. Viết truy vấn để tìm những nhân viên đã gia nhập vào sau ngày 15 của tháng
SELECT
employee_id,
CONCAT_WS(' ', first_name, last_name) employee,
hire_date
FROM employees
WHERE DAY(hire_date)>15;

-- 18. Viết truy vấn để tìm những quản lý và nhân viên làm trong các phòng ban khác nhau, kết quả sắp xếp theo thứ tự tăng dần của tên người quản lý (tên nhân viên và quản lý kết hợp từ first_name và last_name)
SELECT
CONCAT_WS(' ', m.first_name, m.last_name) manager, 
CONCAT_WS(' ', e.first_name, e.last_name) employee,
m.department_id mgr_dept,
e.department_id emp_dept
FROM employees m
INNER JOIN employees e ON e.manager_id = m.employee_id
WHERE m.department_id!=e.department_id
ORDER BY manager ASC;