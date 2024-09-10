CREATE DATABASE [lab6-ssis]
GO

USE [lab6-ssis]
GO

/****** Object: Table [dbo].[Name_DIM] Script Date: 11/20/2023 1:43:23 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE [dbo].[Name_DIM];


GO
CREATE TABLE [dbo].[Name_DIM] (
	[NameId] INT IDENTITY(1,1),
    [Name] VARCHAR (50) NULL
);

CREATE TABLE [dbo].[User_Fact] (
    [UserId] int,
    [Age] int,
    [NameId] int
);



