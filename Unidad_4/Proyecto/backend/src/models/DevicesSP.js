const { getConnection } = require('./conexion')
const sql = require('mssql')

const insertDevice = async (id_type, id_signal_type, name, vendor) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_type", sql.Int, id_type)
            .input("id_signal_type", sql.Int, id_signal_type)
            .input("name", sql.VarChar(100), name)
            .input("vendor", sql.VarChar(100), vendor)
            .execute("SP_Insert_DevicesInfo")

        return {
            status: "success",
            message: "Inserción exitosa"
        }
    } catch(error) {
        return {
            status: "success",
            message: `Error al insertar: ${error}`
        }
    }
}

const getAllDevices = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .execute("SP_GetAll_DevicesInfo")

        return result.recordset
    } catch {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

const getDeviceById = async (id_device) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_device", sql.Int, id_device)
            .execute("SP_Get_DevicesInfo_ById")

        return result.recordset[0]
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

const updateDevice = async (id_device, id_type, id_signal_type, name, vendor) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_device", sql.Int, id_device)
            .input("id_type", sql.Int, id_type)
            .input("id_signal_type", sql.Int, id_signal_type)
            .input("name", sql.VarChar(100), name)
            .input("vendor", sql.VarChar(100), vendor)
            .execute("SP_Update_DevicesInfo")

        return {
            status: "success",
            message: "Actualización exitosa"
        }
    } catch(error) {
        return {
            status: "error",
            message: `Error al actualizar: ${error}`
        }
    }
}

const deleteDevice = async (id_device) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_device", sql.Int, id_device)
            .execute("SP_Delete_DevicesInfo")

        return {
            status: "success",
            message: "Eliminación exitosa"
        }
    } catch(error) {
        return {
            status: "error",
            message: `Error al eliminar: ${error}`
        }
    }
}

module.exports = {
    SP_Insert_Device: insertDevice,
    SP_GetAll_Devices: getAllDevices,
    SP_Get_Device_ById: getDeviceById,
    SP_Update_Device: updateDevice,
    SP_Delete_Device: deleteDevice
}