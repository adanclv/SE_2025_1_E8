--PASO 1
CREATE DATABASE [BD_UNIDAD_4_SE_2025_1]

USE BD_UNIDAD_4_SE_2025_1
GO

--PASO 2
CREATE TABLE [dbo].[devices_info](
    [id_device] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
    [id_type] [numeric](18, 0) NOT NULL, --SENSOR O ACTUADOR
    [id_signal_type] [numeric](18, 0) NOT NULL, -- DIGITAL O ANALOGICO
    [name] [nvarchar](100) NOT NULL,     
    [vendor] [nvarchar](100) NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[devices_info] ADD PRIMARY KEY CLUSTERED 
(
    [id_device] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

BEGIN TRAN
INSERT INTO devices_info (NAME, VENDOR, id_type, id_signal_type) VALUES('SENSOR DE DISTANCIA','SE_CLASE', 1, 1)
INSERT INTO devices_info (NAME, VENDOR, id_type, id_signal_type) VALUES('SENSOR DE PROXIMIDAD','SE_CLASE', 1, 1)
SELECT * FROM devices_info
ROLLBACK TRAN

INSERT INTO devices_info (NAME, VENDOR, id_type, id_signal_type) VALUES('SENSOR DE PRESENCIA','SE_CLASE', 1, 1)
SELECT * FROM devices_info

GO

--PASO 3
CREATE TABLE [dbo].[devices_records]( -- HISTORICO ---> DW  ---> EDA (ANALISIS EXPLORATORIO DE DATOS)
	[id_record] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
	[id_device] [numeric](18, 0) NOT NULL,
	[current_value] [numeric](18, 0) NOT NULL,
	[date_record] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_record] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[devices_records]  WITH CHECK ADD FOREIGN KEY([id_device])
REFERENCES [dbo].[devices_info] ([id_device])
GO

--PASO 4 
CREATE OR ALTER PROCEDURE [dbo].[SP_Insert_DevicesRecords] 
    @id_device as numeric(18,0), 
    @current_value as numeric(18,0)  -- va (VALOR ACTUAL)
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO [dbo].[devices_records]
           ([id_device]
            ,[date_record]
            ,[current_value]
           )
     VALUES
           (@id_device
            ,GETDATE()
           ,@current_value
           )
END


---PASO 5
EXEC SP_Insert_DevicesRecords 3, 120
EXEC SP_Insert_DevicesRecords 3, 240
EXEC SP_Insert_DevicesRecords 3, 170
EXEC SP_Insert_DevicesRecords 3, 390
EXEC SP_Insert_DevicesRecords 4, 80
EXEC SP_Insert_DevicesRecords 4, 140
EXEC SP_Insert_DevicesRecords 4, 890

SELECT * FROM devices_records
SELECT * FROM devices_info

-- UPDATE devices_records SET id_device = 5 WHERE id_device = 2

GO

CREATE OR ALTER PROCEDURE [dbo].[SP_SelectAll_records]
    -- Add the parameters for the stored procedure here 
AS
BEGIN
    SET NOCOUNT ON;

    SELECT DI.id_device, DI.name "NAME", DR.current_value "CURRENT_VALUE", 
    DR.date_record "DATE_RECORD"
    FROM devices_records DR
    INNER JOIN devices_info DI ON DR.id_device = DI.id_device
           
END

EXEC SP_SelectAll_records

GO

CREATE PROCEDURE [dbo].[SP_SelecLastRecordByID]
    -- Add the parameters for the stored procedure here 
    @id_device as numeric(18,0)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT TOP 1 DI.id_device, DI.name "NAME", DR.current_value "CURRENT_VALUE", 
    DR.date_record "DATE_RECORD"
    FROM devices_records DR
    INNER JOIN devices_info DI ON DR.id_device = DI.id_device
    WHERE DI.id_device = @id_device
    ORDER BY DR.date_record DESC   
END

GO

EXEC SP_SelectALL_records
EXEC SP_SelecLastRecordByID 3

GO

--PASO 6 ******
CREATE TABLE [dbo].[toma_decisiones]( --"valores_optimizados"
    [id_decision] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
    [velocidad] [numeric](18, 0) NOT NULL,
    [distancia] [numeric](18, 0) NOT NULL,
    [decision] [numeric](18, 0) NOT NULL,
    [date_record] [datetime] NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[toma_decisiones] ADD PRIMARY KEY CLUSTERED 
(
    [id_decision] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO

--Paso 7
CREATE PROCEDURE [dbo].[SP_Insert_Decision]    
    @velocidad as numeric(18, 0),
    @distancia as numeric(18, 0),
    @decision as numeric(18, 0)  
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[toma_decisiones]
           ([velocidad]
            ,[distancia]
            ,[decision],
            [date_record]
           )
     VALUES
           (@velocidad,
           @distancia,
           @decision
            ,GETDATE()           
           )
    
END
GO

-- SP_Insert_Decision 10, 20, 1
-- SP_Insert_Decision 20, 40, 2
-- SP_Insert_Decision 60, 60, 3

select * from toma_decisiones
GO

--paso 8
CREATE PROCEDURE [dbo].[SP_SelecLastDecision]
    -- Add the parameters for the stored procedure here   
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT top 1 *
    FROM toma_decisiones        
    order by date_record desc
           
END
GO

--> Drop SP
-- DROP PROCEDURE IF EXISTS SP_Insert_DevicesRecords, SP_SelecLastRecordByID, SP_SelectAll_records;
-- DROP PROCEDURE IF EXISTS SP_Insert_DeviceType, SP_Delete_DeviceType, SP_Get_DeviceType_ById, SP_GetAll_DeviceType, SP_Update_DeviceType

--> Create Table
CREATE TABLE device_type (
	id_type NUMERIC(18, 0) IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	[name] NVARCHAR(100) NOT NULL
);
GO

CREATE TABLE signal_type(
	id_signal_type NUMERIC(18, 0) IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	[name] NVARCHAR(100) NOT NULL
);
GO

CREATE TABLE devices_info(
	id_device NUMERIC (18, 0) IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	id_type NUMERIC(18, 0) NOT NULL,
	id_signal_type NUMERIC(18, 0) NOT NULL,
	[name] NVARCHAR(100) NOT NULL,
	vendor NVARCHAR(100) NOT NULL,
	FOREIGN KEY (id_type) REFERENCES device_type(id_type),
	FOREIGN KEY (id_signal_type) REFERENCES signal_type(id_signal_type)
);
GO

CREATE TABLE devices_records(
	id_record NUMERIC(18, 0) IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	id_device NUMERIC(18, 0) NOT NULL,
	current_value NUMERIC(18, 0) NOT NULL,
	date_record DATETIME NOT NULL,
	FOREIGN KEY (id_device) REFERENCES devices_info(id_device)
);
GO

---> Stored Procedures
-- Tabla Device Type
CREATE PROCEDURE SP_Insert_DeviceType
	@name as varchar(100)
AS
BEGIN
	INSERT INTO device_type(name)
	VALUES(@name);
END
GO

CREATE PROCEDURE SP_GetAll_DeviceType
AS
BEGIN
	SELECT id_type, [name]
	FROM device_type;
END
GO

CREATE PROCEDURE SP_Get_DeviceType_ById
	@id_type AS NUMERIC(18, 0)
AS
BEGIN
	SELECT id_type, [name]
	FROM device_type
	WHERE id_type = @id_type;
END
GO

CREATE PROCEDURE SP_Update_DeviceType
	@id_type AS NUMERIC(18, 0),
	@name AS VARCHAR(100)
AS
BEGIN
	UPDATE device_type
	SET [name] = @name
	WHERE id_type = @id_type;
END
GO

CREATE PROCEDURE SP_Delete_DeviceType
	@id_type AS NUMERIC(18, 0)
AS
BEGIN
	DELETE FROM device_type
	WHERE id_type = @id_type;
END
GO

-- Tabla Signal Type
CREATE OR ALTER PROCEDURE SP_Insert_SignalType
	@name AS VARCHAR(100)
AS
BEGIN
	INSERT INTO signal_type(name)
	VALUES(@name);
END
GO

CREATE OR ALTER PROCEDURE SP_GetAll_SignalType
AS
BEGIN
	SELECT id_signal_type, [name]
	FROM signal_type
END
GO

CREATE OR ALTER PROCEDURE SP_Get_SignalType_ById
	@id_signal_type AS NUMERIC(18, 0)
AS
BEGIN
	SELECT id_signal_type, [name]
	FROM signal_type
	WHERE id_signal_type = @id_signal_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Update_SignalType
	@id_signal_type AS NUMERIC(18, 0),
	@name AS VARCHAR(100)
AS
BEGIN
	UPDATE signal_type
	SET [name] = @name
	WHERE id_signal_type = @id_signal_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Delete_SignalType
	@id_signal_type AS NUMERIC(18, 0)
AS
BEGIN
	DELETE FROM signal_type
	WHERE id_signal_type = @id_signal_type;
END
GO

-- Tabla Devices Info
CREATE OR ALTER PROCEDURE SP_Insert_DevicesInfo
	@id_type NUMERIC(18, 0),
	@id_signal_type NUMERIC(18, 0),
	@name NVARCHAR(100),
	@vendor NVARCHAR(100)
AS
BEGIN
	INSERT INTO devices_info(id_type,id_signal_type, [name], vendor)
	VALUES(@id_type, @id_signal_type, @name, @vendor);
END
GO

CREATE OR ALTER PROCEDURE SP_GetAll_DevicesInfo
AS
BEGIN
	SELECT DI.id_device, DT.[name] "DEVICE_TYPE", ST.[name] "SIGNAL_TYPE", DI.[name], DI.vendor
	FROM devices_info DI
		INNER JOIN device_type DT ON DI.id_type = DT.id_type
		INNER JOIN signal_type ST ON DI.id_signal_type = ST.id_signal_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Get_DevicesInfo_ById
	@id_device AS NUMERIC(18, 0)
AS
BEGIN
	SELECT DI.id_device, DT.[name] "DEVICE_TYPE", ST.[name] "SIGNAL_TYPE", DI.[name], DI.vendor
	FROM devices_info DI
		INNER JOIN device_type DT ON DI.id_type = DT.id_type
		INNER JOIN signal_type ST ON DI.id_signal_type = ST.id_signal_type
	WHERE DI.id_device = @id_device;
END
GO

CREATE OR ALTER PROCEDURE SP_Update_DevicesInfo
	@id_device NUMERIC (18, 0),
	@id_type NUMERIC(18, 0),
	@id_signal_type NUMERIC(18, 0),
	@name NVARCHAR(100),
	@vendor NVARCHAR(100)
AS
BEGIN
	UPDATE devices_info
	SET id_type = @id_type, id_signal_type = @id_signal_type, [name] = @name, vendor = @vendor
	WHERE id_device = @id_device;
END
GO

CREATE OR ALTER PROCEDURE SP_Delete_DevicesInfo
	@id_device AS NUMERIC(18, 0)
AS
BEGIN
	DELETE FROM devices_info
	WHERE id_device = @id_device;
END
GO

-- Tabla Device Record
CREATE OR ALTER PROCEDURE SP_Insert_DevicesRecords 
    @id_device as numeric(18,0), 
    @current_value as numeric(18,0)
AS
BEGIN
    INSERT INTO devices_records(id_device ,date_record, current_value)
    VALUES(@id_device, GETDATE(), @current_value);
END
GO

CREATE OR ALTER PROCEDURE SP_GetAll_DevicesRecords
AS
BEGIN
    SELECT DI.id_device, DI.[name] "DEVICE_NAME", DR.current_value "CURRENT_VALUE", 
    DR.date_record "DATE_RECORD"
    FROM devices_records DR
		INNER JOIN devices_info DI ON DR.id_device = DI.id_device;    
END
GO

CREATE OR ALTER PROCEDURE SP_Get_LastRecord_ByID
    @id_device AS NUMERIC(18,0)
AS
BEGIN
    SELECT TOP 1 DI.id_device, DI.name "DEVICE_NAME", DR.current_value "CURRENT_VALUE", 
    DR.date_record "DATE_RECORD"
    FROM devices_records DR
		INNER JOIN devices_info DI ON DR.id_device = DI.id_device
    WHERE DI.id_device = @id_device
    ORDER BY DR.date_record DESC;
END
GO

CREATE OR ALTER PROCEDURE SP_Update_DevicesRecords
	@id_record AS NUMERIC(18, 0),
	@id_device AS NUMERIC(18, 0),
	@current_value AS NUMERIC(18, 0)
AS
BEGIN
	UPDATE devices_records
	SET id_device = @id_device, current_value = @current_value
	WHERE id_record = @id_record;
END
GO

CREATE OR ALTER PROCEDURE SP_Delete_DevicesRecord
	@id_record AS NUMERIC(18, 0)
AS
BEGIN
	DELETE FROM devices_records
	WHERE id_record = @id_record;
END
GO