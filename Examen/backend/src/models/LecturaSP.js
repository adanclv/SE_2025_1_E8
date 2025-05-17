const { getConnection } = require('./conexion')
const sql = require('mssql')

const insertLectura = async (valor, estado) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("valor", sql.Int, valor)
            .input("estado", sql.VarChar(50), estado)
            .execute("sp_InsertarLectura")

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

const getAllLecturas = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .execute("sp_ObtenerTodasLecturas")

        return result.recordset
    } catch {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

const getLastLectura = async () => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .execute("sp_ObtenerUltimaLectura")

        return result.recordset
    } catch {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

module.exports = {
    SP_GetAll_Lecturas: getAllLecturas,
    SP_Last_Lectura: getLastLectura,
    SP_Insert_Lectura: insertLectura,
}