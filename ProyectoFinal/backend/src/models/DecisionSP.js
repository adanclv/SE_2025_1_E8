const { getConnection } = require('./conexion')
const sql = require('mssql')

const insertDecision = async (current_value, decision) => {
    try {
        const conn = await getConnection();
        const result = await conn
            .request()
            .input("current_value", sql.Int, current_value)
            .input("decision", sql.Int, decision)
            .execute("SP_Insert_TomaDecisiones");

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

const getAllDecisiones = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request().execute("SP_GetAll_TomaDecisiones")
        return result.recordset
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const getLastDecision = async (id_signal_type) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request().execute("SP_Get_LastDecision")
        return result.recordset[0]
    } catch (error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        };
    }
}

const updateDecision = async (id_decision, current_value, decision) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_decision", slq.Int, id_decision)
            .input("current_value", slq.Int, current_value)
            .input("decision", slq.Int, decision)
            .execute("SP_Update_TomaDecisiones")
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

const deleteDecision = async (id_decision) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_decision", sql.Int, id_decision)
            .execute("SP_Delete_TomaDecisiones")

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
    SP_Insert_Decision: insertDecision,
    SP_GetAll_Decision: getAllDecisiones,
    SP_Get_LastDecision: getLastDecision,
    SP_Update_Decision: updateDecision,
    SP_Delete_Decision: deleteDecision
}