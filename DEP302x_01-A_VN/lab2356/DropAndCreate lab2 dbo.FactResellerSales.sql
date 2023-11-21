CREATE DATABASE [lab2-ssis]
GO

USE [lab2-ssis]
GO

/****** Object: Table [dbo].[FactResellerSales] Script Date: 11/20/2023 12:59:05 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE [dbo].[FactResellerSales];


GO
CREATE TABLE [dbo].[FactResellerSales] (
    [ProductKey]           VARCHAR (50) NULL,
    [OrderDateKey]         VARCHAR (50) NULL,
    [SalesTerritoryKey]    VARCHAR (50) NULL,
    [SalesOrderNumber]     VARCHAR (50) NULL,
    [SalesOrderLineNumber] VARCHAR (50) NULL,
    [RevisionNumber]       VARCHAR (50) NULL,
    [OrderQuantity]        VARCHAR (50) NULL,
    [UnitPrice]            VARCHAR (50) NULL,
    [ExtendedAmount]       VARCHAR (50) NULL
);


