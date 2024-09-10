USE [master];

IF DB_ID('asm1-petfinder') IS NOT NULL
BEGIN
    ALTER DATABASE [asm1-petfinder] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE [asm1-petfinder];
END
GO

CREATE DATABASE [asm1-petfinder]
GO

USE [asm1-petfinder];


CREATE TABLE [PetType_DIM] (
    [PetTypeID] int not null identity(1,1),
    [PetTypeName] varchar(50)
)
GO

CREATE TABLE [Breed_DIM] (
    [BreedID] int not null identity(1,1),
    [BreedName] varchar(255)
)
GO

CREATE TABLE [Gender_DIM] (
    [GenderID] int not null identity(1,1),
    [GenderName] varchar(6)
)
GO

CREATE TABLE [Color_DIM] (
    [ColorID] int not null identity(1,1),
    [ColorName] varchar(255)
)
GO

CREATE TABLE [Size_DIM] (
    [SizeID] int not null identity(1,1),
    [SizeName] varchar(13)
)
GO

CREATE TABLE [Length_DIM] (
    [LengthID] int not null identity(1,1),
    [LengthName] varchar(13)
)
GO

CREATE TABLE [Confirmation_DIM] (
    [ConfirmationID] int not null identity(1,1),
    [ConfirmationName] varchar(8)
)
GO

CREATE TABLE [Health_DIM] (
    [HealthID] int not null identity(1,1),
    [HealthName] varchar(14)
)
GO

CREATE TABLE [State_DIM] (
    [StateID] int not null identity(1,1),
    [StateName] varchar(255)
)
GO

CREATE TABLE [Pet_Fact] (
    [TypeID] int,
    [PetID] int NOT NULL,
    [Age] int,
    [Breed1ID] int,
    [Breed2ID] int,
    [GenderID] int,
    [Color1ID] int,
    [Color2ID] int,
    [Color3ID] int,
    [MaturitySizeID] int,
    [FurLengthID] int,
    [VaccinatedID] int,
    [DewormedID] int,
    [SterilizedID] int,
    [HealthID] int,
    [Quantity] int,
    [Fee] int,
    [StateID] int,
    [RescuerID] int,
    CONSTRAINT pk_Pet_Fact PRIMARY KEY ([PetID])
)
GO


CREATE TABLE [PetFinder_CDC] (
    [Type] varchar(3),
    [PetID] int not null,    
    [Age] int,
    [Breed1] varchar(255),
    [Breed2] varchar(255),
    [Gender] varchar(6),
    [Color1] varchar(255),
    [Color2] varchar(255),
    [Color3] varchar(255),
    [MaturitySize] varchar(13),
    [FurLength] varchar(13),
    [Vaccinated] varchar(8),
    [Dewormed] varchar(8),
    [Sterilized] varchar(8),
    [Health] varchar(14),
    [Quantity] int,
    [Fee] int,
    [State] varchar(255),
    [RescuerID] int,
    CONSTRAINT pk_PetFinder_CDC PRIMARY KEY ([PetID])
)
GO

EXEC sys.sp_cdc_enable_db
GO

EXEC sys.sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = 'PetFinder_CDC',
    @role_name = NULL,
    @supports_net_changes = 1;
GO

CREATE TABLE [dbo].[petfinder_cdc_states] 
 ([name] [nvarchar](256) NOT NULL, 
 [state] [nvarchar](256) NOT NULL) ON [PRIMARY]
GO
CREATE UNIQUE NONCLUSTERED INDEX [cdc_states_name] ON 
 [dbo].[petfinder_cdc_states] 
 ( [name] ASC ) 
 WITH (PAD_INDEX  = OFF) ON [PRIMARY]
GO

SELECT * FROM cdc.change_tables;