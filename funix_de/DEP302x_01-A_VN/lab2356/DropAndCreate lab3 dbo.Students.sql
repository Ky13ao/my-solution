CREATE DATABASE [lab3-ssis]
GO

USE [lab3-ssis]
GO

/****** Object: Table [dbo].[Students] Script Date: 11/20/2023 1:00:12 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE [dbo].[Students];


GO
CREATE TABLE [dbo].[Students] (
    [Last Name]       VARCHAR (40) NULL,
    [First Name]      VARCHAR (25) NULL,
    [Academic Status] VARCHAR (3)  NULL
);


