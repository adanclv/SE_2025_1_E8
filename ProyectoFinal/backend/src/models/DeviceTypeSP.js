const { getConnection } = require('./conexion')
const sql = require('mssql')

const insertDeviceType = async (name) => {
    try {
        const conn = await getConnection();
        const result = await conn
            .request()
            .input("name", sql.VarChar(100), name)
            .execute("SP_Insert_DeviceType");

        return {
            status: "success",
            message: "Inserción exitosa"
        };
    } catch (error) {
        return {
            status: "error",
            message: `Error al insertar: ${error}`
        };
    }
};

const getAllDeviceType = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request().execute("Sp_GetAll_DeviceType")
        return result.recordset
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const getDeviceTypeById = async (id_type) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_type", sql.Int, id_type)
            .execute("SP_Get_DeviceType_ById")

        return result.recordset[0]
    } catch (error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const updateDeviceType = async (id_type, name) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_type", sql.Int, id_type)
            .input("name", sql.VarChar(100), name)
            .execute("SP_Update_DeviceType")
        return {
            status: "success",
            message: "Actualización exitosa"
        };
    } catch(error) {
        return {
            status: "error",
            message: `Error al actualizar: ${error}`
        };
    }
}

const deleteDeviceType = async (id_type) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_type", sql.Int, id_type)
            .execute("SP_Delete_DeviceType")

        return {
            status: "success",
            message: "Eliminación exitosa"
        }
    } catch {
        return {
            status: "error",
            message: `Error al eliminar: ${error}`
        }
    }
}

module.exports = {
    SP_InsertDeviceType: insertDeviceType,
    SP_GetAll_DeviceType: getAllDeviceType,
    SP_Get_DeviceType_ById: getDeviceTypeById,
    SP_Update_DeviceType: updateDeviceType,
    SP_Delete_DeviceType: deleteDeviceType
}