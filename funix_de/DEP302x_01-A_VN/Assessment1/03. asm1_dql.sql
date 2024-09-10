USE [asm1-petfinder];

-- 1. Có bao nhiêu vật nuôi chưa được kiểm tra sức khỏe?
SELECT Count(*) so_vat_nuoi_khong_ro_suc_khoe FROM [Pet_Fact] pf
INNER JOIN [Health_DIM] hDIM ON hDIM.HealthID = pf.HealthID
WHERE hDIM.HealthName = 'Not Specified'
GO

-- 2. Có bao nhiêu vật nuôi không rõ kích cỡ trưởng thành?
SELECT Count(*) so_vat_nuoi_ko_ro_kichco_truongthanh FROM [Pet_Fact] pf
INNER JOIN [Size_DIM] sDIM ON sDIM.SizeID = pf.MaturitySizeID
WHERE sDIM.SizeName = 'Not Specified'
GO

-- 3. Có bao nhiêu vật nuôi thuần chủng?
SELECT Count(*) so_vat_nuoi_thuan_chung FROM [Pet_Fact] pf
INNER JOIN [Breed_DIM] bDIM ON bDIM.BreedID = pf.Breed2ID
WHERE bDIM.BreedName = 'None'
GO
