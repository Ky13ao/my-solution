-- Data Cleaning
use project1;
select * from worldlifexpectancy_staging; 
 /* 1. **Handling Missing Values**:
   - Identify missing values in the dataset.
   - Decide on strategies to handle missing values. */ 
-- Đối với Status: 
	-- Xác định được ở cột status có các giá trị bị trống, ta sẽ tiến hành biến đổi chúng thành giá trị NULL để dễ dùng các hàm trong sql phục vụ cho giá trị NULL 
	UPDATE worldlifexpectancy 
	SET Status = NULL 
	WHERE status = ''; 
	-- Sau đó tiến hành biến đổi các giá trị NULL bằng hàm COALESCE và kết hợp với các hàm Lag Lead. Mục đích của 2 hàm LAG và LEAD là sẽ lấy giá trị gần nhất của giá trị NULL để điền vào. 

	UPDATE worldlifexpectancy AS w
	LEFT JOIN worldlifexpectancy AS prev_year
	ON w.Country = prev_year.Country AND w.Year = prev_year.Year + 1
	LEFT JOIN worldlifexpectancy AS next_year
	ON w.Country = next_year.Country AND w.Year = next_year.Year - 1
	SET w.Status = COALESCE(w.Status, prev_year.Status, next_year.Status)
	WHERE w.Status IS NULL; 

-- Đối với Lifeexpectancy: 
	-- Biến đổi các giá trị blank thành NULL
	UPDATE worldlifexpectancy 
	SET Lifeexpectancy = NULL 
	WHERE Lifeexpectancy = ''; 
-- Nhận thấy giá trị lifeexpectancy của 2 missing values đều tăng dần theo từng năm vì thế, ta quyết định sẽ lấy trung bình cộng của 2 năm gần giá trị null nhất. 
	
    UPDATE worldlifexpectancy as w 
	LEFT JOIN worldlifexpectancy as prev_year_le
		ON w.Country = prev_year_le.Country AND w.Year = prev_year_le.Year + 1
	LEFT JOIN worldlifexpectancy AS next_year_le
		ON w.Country = next_year_le.Country AND w.Year = next_year_le.Year - 1
	SET w.Lifeexpectancy = COALESCE(w.Lifeexpectancy, ROUND((prev_year_le.Lifeexpectancy + next_year_le.Lifeexpectancy) /2 ,2))
		WHERE w.Lifeexpectancy IS NULL; 
-- Đối với GDP, xuất hiện nhiều bản ghi có GDP bằng 0, ta sẽ tiến hành biến đổi nó thành NULL 
UPDATE worldlifexpectancy 
	SET GDP = NULL 
	WHERE GDP = 0; 


/* 2. **Data Consistency**:
   - Check for and correct inconsistencies in categorical columns like `Country` and `Status`. */

-- Đổi kiểu dữ liệu của Lifeexpectancy thành double 
ALTER TABLE worldlifexpectancy
ADD COLUMN Lifeexpectancy_double DOUBLE;

-- Cập nhật giá trị trong cột mới từ cột cũ
UPDATE worldlifexpectancy
SET Lifeexpectancy_double = CAST(Lifeexpectancy AS DOUBLE);

-- Xóa cột cũ
ALTER TABLE worldlifexpectancy
DROP COLUMN Lifeexpectancy;

-- Đổi tên cột mới thành tên cột cũ
ALTER TABLE worldlifexpectancy
CHANGE COLUMN Lifeexpectancy_double Lifeexpectancy DOUBLE;

/* 3. **Removing Duplicates**:
   - Identify and remove duplicate rows if any. */
   
-- Để xác định các outliers, ta sẽ dùng hàm COUNT và GROUP BY 2 cột là Country và Year. 
SELECT country, year, count(*) from worldlifexpectancy
group by country, year 
having count(*) > 1; 

-- Sau khi xác định có 3 giá trị bị duplicated, ta sẽ tiến hành loại bỏ 3 giá trị đó sử dụng SUBQUERY và hàm ROW_NUMBER 
DELETE FROM worldlifexpectancy 
WHERE row_id IN (SELECT row_id FROM (SELECT row_id, row_number() OVER (PARTITION BY country, year) as row_num  FROM worldlifexpectancy) as table1
WHERE row_num > 1);  

/* 4. **Outlier Detection and Treatment**:
 -  Identify and treat outliers in columns like `Lifeexpectancy`, `AdultMortality`, and `GDP`.
 - 	Decide on strategies to handle outlier (eg. avg) */

/* Đối với cách xác định outlier thì ta sẽ dùng chung 1 phương pháp đó là phương pháp phi tham số. 
Phương pháp này có thể được mô tả ngắn gọn như sau: 
• Tìm giá trị 25th percentile của biến X. Gọi trị số này là Q1. 
• Tìm giá trị 75th percentile của biến X.Gọi trị số này là Q3 
• Tính độ khác biệt giữa Q1 và Q3 bằng công thức: IQR = Q3 – Q1. 
• Tính giá trị thấp của biến và gọi đó là L (tức lower): L = Q1 - 1.5 x IQR
• Tính giá trị cao của biến và gọi đó là U (upper): U = Q3+ 1.5 × IQR . 
• Nếu trong dãy số x1, x2, x3,…., x100 có số nào thấp hơn L hay cao hơn U, thì 
có thể xem đó là outlier. */


-- Đối với Lifeexpectancy
	-- tạo bảng cte để tìm các giá trị q1 q2 q3

WITH ntiles_table AS (
    SELECT 
        MAX(CASE WHEN quartiles = 1 THEN Lifeexpectancy END) as Q1,
        MAX(CASE WHEN quartiles = 2 THEN Lifeexpectancy END) as Q2,
        MAX(CASE WHEN quartiles = 3 THEN Lifeexpectancy END) as Q3 
    FROM (
        SELECT 
            Lifeexpectancy, 
            NTILE(4) OVER (ORDER BY Lifeexpectancy) as quartiles
        FROM worldlifexpectancy
    ) as ntiles_table 
),
	quartiles_table AS (
    SELECT 
		ROUND(Q3 - Q1, 2) as IQR, 
		ROUND(Q1 - 1.5 * (Q3 - Q1), 2) as L,  
		ROUND(Q3 + 1.5 * (Q3 - Q1), 2) as U
	FROM ntiles_table
						)
	-- Thay thế các giá trị outliers bằng giá trị upper hoặc lower. 
UPDATE worldlifexpectancy 
SET Lifeexpectancy = (select U from quartiles_table)
WHERE Lifeexpectancy > ( select U from quartiles_table); 

UPDATE worldlifexpectancy 
SET Lifeexpectancy = (select L from quartiles_table)
WHERE Lifeexpectancy < ( select L from quartiles_table); 





-- Đối với AdultMortality
	-- tạo bảng cte để tìm các giá trị q1 q2 q3
select distinct AdultMortality FROM worldlifexpectancy
ORDER BY AdultMortality desc ; 

WITH ntiles_table AS (
    SELECT 
        MAX(CASE WHEN quartiles = 1 THEN AdultMortality END) as Q1,
        MAX(CASE WHEN quartiles = 2 THEN AdultMortality END) as Q2,
        MAX(CASE WHEN quartiles = 3 THEN AdultMortality END) as Q3 
    FROM (
        SELECT 
            AdultMortality, 
            NTILE(4) OVER (ORDER BY AdultMortality) as quartiles
        FROM worldlifexpectancy
    ) as ntiles_table 
),
	quartiles_table AS (
    SELECT 
		ROUND(Q3 - Q1, 2) as IQR, 
		ROUND(Q1 - 1.5 * (Q3 - Q1), 2) as L,  
		ROUND(Q3 + 1.5 * (Q3 - Q1), 2) as U
	FROM ntiles_table
						)
	-- Thay thế các giá trị outliers bằng giá trị upper hoặc lower. 

UPDATE worldlifexpectancy 
SET AdultMortality = (select U from quartiles_table)
WHERE AdultMortality > ( select U from quartiles_table); 

UPDATE worldlifexpectancy 
SET AdultMortality = (select L from quartiles_table)
WHERE AdultMortality < ( select L from quartiles_table); 


-- Đối với GDP
	-- tạo bảng cte để tìm các giá trị q1 q2 q3
select gdp from worldlifexpectancy; 


WITH ntiles_table AS (
    SELECT 
        MAX(CASE WHEN quartiles = 1 THEN GDP END) as Q1,
        MAX(CASE WHEN quartiles = 2 THEN GDP END) as Q2,
        MAX(CASE WHEN quartiles = 3 THEN GDP END) as Q3 
    FROM (
        SELECT 
            GDP, 
            NTILE(4) OVER (ORDER BY GDP) as quartiles
        FROM worldlifexpectancy
        WHERE GDP is not null
    ) as ntiles_table 
),
	quartiles_table AS (
    SELECT 
		ROUND(Q3 - Q1, 2) as IQR, 
		ROUND(Q1 - 1.5 * (Q3 - Q1), 2) as L,  
		ROUND(Q3 + 1.5 * (Q3 - Q1), 2) as U
	FROM ntiles_table
						)
                 
	-- Thay thế các giá trị outliers bằng giá trị upper hoặc lower. 

UPDATE worldlifexpectancy 
SET GDP = (select U from quartiles_table)
WHERE GDP > ( select U from quartiles_table); 

UPDATE worldlifexpectancy 
SET GDP = (select L from quartiles_table)
WHERE GDP < ( select L from quartiles_table); 

-- vì Lower limit có giá trị âm cho nên không thể thay thế cho các giá trị bị thiếu, vì thế ta sẽ dùng giá trị trung bình để gán vào các NULL value. 
WITH avg_gdp AS (SELECT avg(GDP) as avg_gdp FROM worldlifexpectancy )
 
UPDATE worldlifexpectancy
SET GDP = (SELECT avg_gdp FROM avg_gdp ) 
WHERE GDP IS NULL;


-- EDA
select * from worldlifexpectancy;

-- 1. **Basic Descriptive Statistics**: 
SELECT 
	ROUND(AVG(Lifeexpectancy),2) as avg,  
    min(Lifeexpectancy) as min, 
    max(Lifeexpectancy) as max,
	IF(count(Lifeexpectancy) % 2 = 1, 
		MAX(CASE WHEN twotiles = 1 THEN Lifeexpectancy END), 
		(MAX(CASE WHEN twotiles = 1 THEN Lifeexpectancy END) + MIN(CASE WHEN twotiles = 2 THEN Lifeexpectancy END)) / 2)
        as median 
		-- Nếu số bản ghi là số lẻ thì: ta sẽ lấy max của tile 1
        -- Nếu số bản ghi là số chẵn thì: ta sẽ lấy max của tile 1 và min của tile 2, sau đó lấy trung bình cộng của 2 giá trị này. 
FROM (  SELECT Lifeexpectancy, NTILE(2) OVER ( ORDER BY Lifeexpectancy) as twotiles FROM worldlifexpectancy ) as twotiles_table 

-- 2.**Trend Analysis**

select year, Lifeexpectancy, (Lifeexpectancy - lag(Lifeexpectancy) over (order by year ))/ lag(Lifeexpectancy) over (order by year ) *100.00 as growth_over_year   from worldlifexpectancy 
where country = 'Viet Nam'
order by year;
	-- Query sử dụng 2 cột là year và Lifeexpectancy để xác định xu hướng, order by year để thấy xu hướng tăng giảm qua từng năm, growth_over_year cho thấy phần trăm tăng giảm so với năm trước. 

-- 3. **Comparative Analysis**:

SELECT 
	status,
	avg(Lifeexpectancy) 
FROM worldlifexpectancy
WHERE year = (SELECT max(year) from worldlifexpectancy)
GROUP BY status;

-- 4. **Mortality Analysis**:

SELECT 
    (SUM(xy) - SUM(x) * SUM(y) / n) / 
    SQRT((SUM(xx) - SUM(x) * SUM(x) / n) * (SUM(yy) - SUM(y) * SUM(y) / n)) AS correlation -- công thức tính hệ số tương quan pearson 
FROM (
    SELECT 
        AdultMortality  AS x,  -- sử dụng alias để tiện dùng cho công thức. 
        Lifeexpectancy AS y,
        AdultMortality * Lifeexpectancy AS xy,
        AdultMortality  * AdultMortality  AS xx,
        Lifeexpectancy * Lifeexpectancy AS yy,
        COUNT(*) OVER () AS n
    FROM 
        worldlifexpectancy
) AS pearson_corr
GROUP BY n;
 
-- 5. **Impact of GDP**:
	-- Dùng Ntile để chia thành 3 phần bằng nhau theo gdp để xác định khoảng hợp lý
	SELECT country,year, gdp as avg_gdp, ntile(3) OVER (ORDER BY gdp) as ntile_gdp from worldlifexpectancy
    order by ntile_gdp;
    -- Sau query trên thì thấy rằng GDP được cho là thấp khi GDP thấp hơn 1000, Trung bình khi GDP lớn hơn 1000 và thấp hơn 4000. Và trên 4000 là Cao. 
 SELECT 
  CASE 
    WHEN GDP < 1000 THEN 'Low'
    WHEN GDP BETWEEN 1000 AND 8000 THEN 'Medium'
    ELSE 'High'
  END AS gdp_group,
  AVG(Lifeexpectancy) AS Avg_Lifeexpectancy
FROM 
  worldlifexpectancy
GROUP BY 
  gdp_group;
  
-- Có thể thấy quốc gia thuộc nhóm GDP cao sẽ có Trung bình tuổi thọ cao hơn. 

-- 6. **Disease Impact**:

-- Tính tuổi thọ trung bình cho các quốc gia với tỷ lệ mắc bệnh Measles cao và thấp -trên 1000 được cho là cao
SELECT 
  CASE 
    WHEN Measles > 1000 THEN 'High'
    ELSE 'Low'
  END AS Measles_Incidence,
  AVG(Lifeexpectancy) AS Avg_Lifeexpectancy
FROM 
  worldlifexpectancy
GROUP BY 
  Measles_Incidence;

-- Tính tuổi thọ trung bình cho các quốc gia với tỷ lệ mắc bệnh Polio cao và thấp - trên 90 được cho là cao
SELECT 
  CASE 
    WHEN Polio > 90 THEN 'High'
    ELSE 'Low'
  END AS Polio_Incidence,
  AVG(Lifeexpectancy) AS Avg_Lifeexpectancy
FROM 
  worldlifexpectancy
GROUP BY 
  Polio_Incidence;

-- 7. **Schooling and Health**:

-- 8. **BMI Trends**:
SELECT year, BMI, (BMI - LAG(BMI) OVER (ORDER BY year) )/  LAG(BMI) OVER (ORDER BY year) * 100.00 as growth_over_year FROM worldlifexpectancy 
WHERE country = 'Afghanistan'
order by year; 

-- 9. **Infant Mortality**:
	-- Đưa ra 2 nhóm tuổi thọ trung bình cao và thấp và tính trung bình under_fivedeaths và infantdeaths của từng nhóm
SELECT 
  CASE 
    WHEN Lifeexpectancy = (SELECT MAX(Lifeexpectancy) FROM worldlifexpectancy) THEN 'High'
    ELSE 'Low'
  END AS le_group,
  AVG('under_fivedeaths') AS Avg_UnderFiveDeaths,
  AVG(infantdeaths) AS Avg_InfantDeaths
FROM 
  worldlifexpectancy
GROUP BY 
  le_group;

-- 10. **Rolling Average of Adult Mortality**:
SELECT country, year, ROUND(AVG(AdultMortality) OVER (PARTITION BY Country ORDER BY year asc),2) FROM worldlifexpectancy
WHERE year IN (SELECT * FROM ( SELECT distinct year from worldlifexpectancy order by year desc limit 5) as year_table )
;

-- 11. **Impact of Healthcare Expenditure**:

SELECT (SUM(xy) - SUM(x) * SUM(y) / n) / 
    SQRT((SUM(xx) - SUM(x) * SUM(x) / n) * (SUM(yy) - SUM(y) * SUM(y) / n)) AS correlation -- công thức tính hệ số tương quan pearson 
FROM (
	SELECT 
		Lifeexpectancy as x,
        percentageexpenditure as y, 
        Lifeexpectancy * Lifeexpectancy as xx,
        percentageexpenditure * percentageexpenditure as yy,
        Lifeexpectancy * percentageexpenditure as xy,
        count(*) over() as n 
	FROM worldlifexpectancy
		) as pearson_corr
GROUP BY n; 

-- 12. **BMI and Health Indicators**:

	-- correlation between BMI and lifeexpectancy
SELECT (SUM(xy) - SUM(x) * SUM(y) / n) / 
    SQRT((SUM(xx) - SUM(x) * SUM(x) / n) * (SUM(yy) - SUM(y) * SUM(y) / n)) AS correlation -- công thức tính hệ số tương quan pearson 
FROM (
	SELECT 
		Lifeexpectancy as x,
        BMI as y, 
        Lifeexpectancy * Lifeexpectancy as xx,
        BMI * BMI as yy,
        Lifeexpectancy * BMI as xy,
        count(*) over() as n 
	FROM worldlifexpectancy
		) as pearson_corr
GROUP BY n; 
	-- Hệ số tương quan dương cho thấy có một mối quan hệ thuận đạt giữa BMI và tuổi thọ. 
    -- Điều này ngụ ý rằng khi BMI tăng, tuổi thọ có thể tăng và ngược lại.
    
	-- correlation between BMI and AdultMortality
SELECT (SUM(xy) - SUM(x) * SUM(y) / n) / 
    SQRT((SUM(xx) - SUM(x) * SUM(x) / n) * (SUM(yy) - SUM(y) * SUM(y) / n)) AS correlation -- công thức tính hệ số tương quan pearson 
FROM (
	SELECT 
		AdultMortality as x,
        BMI as y, 
        AdultMortality * AdultMortality as xx,
        BMI * BMI as yy,
        AdultMortality * BMI as xy,
        count(*) over() as n 
	FROM worldlifexpectancy
		) as pearson_corr
GROUP BY n; 
	-- Hệ số tương quan âm cho thấy có một mối quan hệ nghịch đảo giữa BMI và tỷ lệ tử vong ở người trưởng thành. 
    -- Điều này ngụ ý rằng khi BMI tăng, tỷ lệ tử vong ở người trưởng thành có thể giảm và ngược lại.
		-- Qua đó, ta có thế đưa ra kết luận BMI cao có thể sẽ giúp tăng tuổi thọ trung bình và giảm tỷ lệ tử vong ở người trưởng thành.

-- 13. **GDP and Health Outcomes**:
 
-- Thông qua truy vấn dưới có thể thấy sơ bộ rằng các quốc gia có GDP cao sẽ có tuổi thọ trung bình cao hơn, tỉ lệ tử vong của người trưởng thành thấp hơn và tỉ lệ trẻ sơ sinh tử vong thấp hơn so với quốc gia có GDP thấp. 
SELECT country, avg(gdp), avg(Lifeexpectancy), avg(AdultMortality), avg(infantdeaths) FROM worldlifexpectancy
GROUP BY country;

	-- Tính trung bình tuổi thọ, tỉ lệ người trưởng thành tử viong và tỉ lệ trẻ sơ sinh tử vong giữa 2 nhóm để có cái nhìn tổng quát hơn

SELECT 
    GDP_group,
    AVG(Lifeexpectancy) AS Avg_Lifeexpectancy,
    AVG(AdultMortality) AS Avg_AdultMortality,
    AVG(infantdeaths) AS Avg_InfantDeaths
FROM (
    SELECT 
        Country,
        Year,
        Lifeexpectancy,
        AdultMortality,
        infantdeaths,
        CASE WHEN GDP > 8000 THEN 'High GDP Group' ELSE 'Low GDP Group' END AS GDP_group
    FROM 
        worldlifexpectancy
) AS subquery
GROUP BY 
    GDP_group;

-- 14. **Subgroup Analysis of Life Expectancy**:

