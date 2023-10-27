-- Nhuộm lông vật nuôi đỏ nếu là vật nuôi có phí và 1 là 1 màu
UPDATE [PetFinder_CDC] SET Color2='Red' WHERE Color2='None' AND Fee > 0
GO


SELECT Count(*) so_vat_co_long_mau_do FROM [Pet_Fact] pf
INNER JOIN [Color_DIM] cDIM ON cDIM.ColorID = pf.Color2ID
WHERE cDIM.ColorName = 'Red'
GO