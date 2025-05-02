const {getConnection} = require('./conexion')
const sql = require('mssql')

const Sp_SelectALL_records  = async function(){    
    const conexion = await getConnection()
    const result = await conexion
    .request().execute('Sp_SelectALL_records')
    //console.log(result.recordset)
    return result.recordset
}

const Sp_SelecLastRecordByID = async function(id_sensor){    
    const conexion = await getConnection()
    const result = await conexion
    .request()                      
         .input("id_sensor", sql.Int, id_sensor )        
         .execute('Sp_SelecLastRecordByID')
    return result.recordset[0]
}

const Sp_SelecLastDecision = async function(){    
    const conexion = await getConnection()
    const result = await conexion
    .request().execute('Sp_SelecLastDecision')
    return result.recordset[0]
}

const Sp_Insert_SensorRecords = async function(id_sensor, current_value){

    console.log("id_sensor: ", id_sensor, " current_value:", current_value)

    const conexion = await getConnection()
    const result = await conexion
    .request()                
         .input("id_sensor", sql.Int, id_sensor )        
         .input("current_value", sql.Int, current_value  )        
         .execute('Sp_Insert_SensorRecords')
    //console.log(result)
    return "{\"Resultado\": \"Insercion Correcta\"}"
}

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
    Sp_SelectALL_records, 
    Sp_SelecLastRecordByID,
    Sp_SelecLastDecision,  

    Sp_Insert_SensorRecords,
    Sp_Insert_Decision,  

}