const { getConnection } = require('./conexion')
const sql = require('mssql')

const insertSignalType = async (name) => {
    try {
        const conn = await getConnection();
        const result = await conn
            .request()
            .input("name", sql.VarChar(100), name)
            .execute("SP_Insert_SignalType");

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

const getAllSignalType = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request().execute("Sp_GetAll_SignalType")
        return result.recordset
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const getSignalTypeById = async (id_signal_type) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_signal_type", sql.Int, id_signal_type)
            .execute("SP_Get_SignalType_ById")

        return result.recordset[0]
    } catch (error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const updateSignalType = async (id_signal_type, name) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_signal_type", slq.Int, id_signal_type)
            .input("name", sql.VarChar(100), name)
            .execute("SP_Update_SignalType")
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

const deleteSignalType = async (id_signal_type) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_signal_type", sql.Int, id_signal_type)
            .execute("SP_Delete_SignalType")

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
    SP_Insert_SignalType: insertSignalType,
    SP_GetAll_SignalType: getAllSignalType,
    SP_Get_SignalType_ById: getSignalTypeById,
    SP_Update_SignalType: updateSignalType,
    SP_Delete_SignalType: deleteSignalType
}