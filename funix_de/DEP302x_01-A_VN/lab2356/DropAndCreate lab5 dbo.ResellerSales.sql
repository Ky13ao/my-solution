CREATE DATABASE [lab5-ssis]
GO

USE [lab5-ssis]
GO

/****** Object: Table [dbo].[FactResellerSales] Script Date: 11/20/2023 12:59:05 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE [dbo].[ResellerSales];


GO
CREATE TABLE [dbo].[ResellerSales] (
    [ProductKey]           INT,
    [OrderDateKey]         VARCHAR (50) NULL,
    [SalesTerritoryKey]    VARCHAR (50) NULL,
    [SalesOrderNumber]     VARCHAR (50) NULL,
    [SalesOrderLineNumber] INT,
    [RevisionNumber]       INT,
    [OrderQuantity]        INT,
    [UnitPrice]            NUMERIC,
    [ExtendedAmount]       NUMERIC,
    [Start_Date] DATETIME,
    [End_Date] DATETIME
);


