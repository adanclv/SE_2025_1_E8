const { getConnection } = require("./conexion");
const sql = require("mssql");

const insertRecord = async (id_device, current_value) =>{
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_device", sql.Int, id_device)
            .input("current_value", sql.Int, current_value)
            .execute('SP_Insert_Record')

        return {
            status: "success",
            message: "Inserción exitosa"
        }
    } catch(error) {
        return {
            status: "error",
            message: `Error al insertar: ${error}`
        }
    }
}

const getAllRecords = async() => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .execute("SP_GetAll_DevicesRecords")

        return result.recordset
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

const getLastRecordById = async(id_device) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_device", sql.Int, id_device)
            .execute("SP_Get_LastRecord_ByID")

        return result.recordset[0]
    } catch(error) {
        return {
            status: "error",
            message: `Error al obtener: ${error}`
        }
    }
}

const updateRecord = async (id_record, id_device, current_value) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_record", sql.Int, id_record)
            .input("id_device", sql.Int, id_device)
            .input("current_value", sql.Int, current_value)
            .execute("SP_Update_DeviceRecords")

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

const deleteRecord = async (id_record) => {
    try {
        const conn = await getConnection()
        const result = await conn
            .request()
            .input("id_record", sql.Int, id_record)
            .execute("SP_Delete_DevicesRecord")

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

const Sp_SelecLastDecision = async function(){
    const conexion = await getConnection()
    const result = await conexion
    .request().execute('Sp_SelecLastDecision')
    return result.recordset[0]
}


//  Servir de intermedario para dispositivos que no pueden
const Sp_Insert_Decision = async function(velocidad, distancia, decision){

    console.log("velocidad: ", velocidad, " distancia:", distancia, " decision:",  decision)

    const conexion = await getConnection()
    const result = await conexion
    .request()
         .input("velocidad", sql.Int, velocidad  )
         .input("distancia", sql.Int, distancia )
         .input("decision", sql.Int, decision )
         .execute('Sp_Insert_Decision')
    //console.log(result)
    return "{\"Resultado\": \"Insercion Correcta\"}"
}

///////////////////////////////////////////////////////////////////////////////////////////////////
//EXPORTA LAS FUNCIONES PARA HACER POSIBLE SU POSTERIOR IMPORTANCION Y USO EN OTROS MODULOS
module.exports = {
    SP_Insert_Record: insertRecord,
    SP_GetAll_Records: getAllRecords,
    SP_GetLast_Record: getLastRecordById,
    SP_Update_Record: updateRecord,
    SP_DeleteRecord: deleteRecord
}