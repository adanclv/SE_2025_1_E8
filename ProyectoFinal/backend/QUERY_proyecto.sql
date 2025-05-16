---> Create Database
CREATE DATABASE SE_ProyectoIntegrador_E8;

---> Use Database
USE SE_ProyectoIntegrador_E8;

---> Create Table
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

CREATE TABLE toma_decisiones (
	id_decision NUMERIC(18, 0) IDENTITY(1, 1) PRIMARY KEY NOT NULL,
	current_value NUMERIC(18, 0) NOT NULL,
	decision NUMERIC(18, 0) NOT NULL,
	date_decision DATETIME NOT NULL
);
GO

---> Stored Procedures
-- Tabla Device Type
CREATE OR ALTER PROCEDURE SP_Insert_DeviceType
	@name as varchar(100)
AS
BEGIN
	INSERT INTO device_type([name])
	VALUES(@name);
END
GO

CREATE OR ALTER PROCEDURE SP_GetAll_DeviceType
AS
BEGIN
	SELECT id_type, [name]
	FROM device_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Get_DeviceType_ById
	@id_type AS NUMERIC(18, 0)
AS
BEGIN
	SELECT id_type, [name]
	FROM device_type
	WHERE id_type = @id_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Update_DeviceType
	@id_type AS NUMERIC(18, 0),
	@name AS VARCHAR(100)
AS
BEGIN
	UPDATE device_type
	SET [name] = @name
	WHERE id_type = @id_type;
END
GO

CREATE OR ALTER PROCEDURE SP_Delete_DeviceType
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
	FROM signal_type;
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
CREATE OR ALTER PROCEDURE SP_Insert_Record
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

CREATE OR ALTER PROCEDURE SP_Get_LastRecord_ById
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

-- Tabla Toma Decisiones
CREATE OR ALTER PROCEDURE SP_Insert_TomaDecisiones
    @current_value AS NUMERIC(18, 0),
    @decision AS NUMERIC(18, 0)
AS
BEGIN
    INSERT INTO toma_decisiones(current_value, decision, date_decision)
    VALUES(@current_value, @decision, GETDATE());
END
GO

CREATE OR ALTER PROCEDURE SP_GetAll_TomaDecisiones
AS
BEGIN
    SELECT id_decision, current_value, decision, date_decision
    FROM toma_decisiones;
END
GO

CREATE OR ALTER PROCEDURE SP_Get_LastDecision
AS
BEGIN
    SELECT TOP 1 id_decision, current_value, decision, date_decision
    FROM toma_decisiones
    ORDER BY date_decision DESC;
END
GO

CREATE OR ALTER PROCEDURE SP_Update_TomaDecisiones
    @id_decision AS NUMERIC(18, 0),
    @current_value AS NUMERIC(18, 0),
    @decision AS NUMERIC(18, 0)
AS
BEGIN
    UPDATE toma_decisiones
    SET current_value = @current_value, decision = @decision
    WHERE id_decision = @id_decision;
END
GO

CREATE OR ALTER PROCEDURE SP_Delete_TomaDecisiones
    @id_decision AS NUMERIC(18, 0)
AS
BEGIN
    DELETE FROM toma_decisiones
    WHERE id_decision = @id_decision;
END
GO


---> Exec Procedures
EXEC SP_Insert_DeviceType 'Sensor';
EXEC SP_Insert_DeviceType 'Actuador';

EXEC SP_Insert_SignalType 'Digital';
EXEC SP_Insert_SignalType 'Analogico';

EXEC SP_Insert_DevicesInfo 2, 1, 'Foco 6,3 V', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 2, 1, 'Foco 6,3 V', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 2, 1, 'Foco 6,3 V', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 1, 2, 'Fotorresistor', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 1, 2, 'Fotorresistor', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 1, 2, 'Fotorresistor', 'SE_Clase';
EXEC SP_Insert_DevicesInfo 1, 2, 'Fotorresistor', 'SE_Clase';

