const bd = require("../models/DevicesSP")

//SELECT * FROM ... ALL
const getAll_records = async function(){    
    //return " GARUCO IS REAL!!"
    const resp = await bd.Sp_SelectALL_records()
    //console.log("resp from service->", resp)
    return resp
}

//SELECT * FROM .. WHERE ... ID
const getLast_Record = async function(id){
    const resp = await bd.Sp_SelecLastRecordByID(id)
    return resp
}

//SELECT * FROM .. INNER JOIN WHERE
const getLastDecision = async function(){
    const resp = await bd.Sp_SelecLastDecision()
    return resp
}

//INSERT
const insertRecord = async function(JsonObj){
    id = JsonObj.Id_sensor
    current_value  = JsonObj.Current_value
    //console.log("Res: ", JsonObj)
    const resp = await bd.Sp_Insert_SensorRecords(id, current_value)
    return resp
}

//INSERT
const insertDecision = async function(JsonObj){
    Velocidad = JsonObj.Velocidad
    Distancia  = JsonObj.Distancia
    Decision = JsonObj.Decision
    //console.log("Res: ", JsonObj)
    const resp = await bd.Sp_Insert_Decision(Velocidad, Distancia, Decision)
    return resp
}

module.exports = {
    getAll_records,
    getLast_Record,
    getLastDecision,

    insertRecord,
    insertDecision,
    
}
