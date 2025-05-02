
const services = require('../services/devicesService')

//SELECT * FROM ... ALL
const getAll_records = async function(req,res){

    const resultado = await services.getAll_records()    
        res.status(201).send(resultado)
}

//SELECT * FROM .. WHERE ... ID
const getLast_Record = async function(req,res){ 
    const {params:{idSensor}} = req 
    //console.log(typeof idSensor)
    if (!isNaN(idSensor)){
        const resultado = await services.getLast_Record(idSensor)
        res.status(200).send(resultado)
    }
    else{
        res.status(501).send("Error")
    }
}

//SELECT * FROM .. INNER JOIN WHERE ... ID
const getLastDecision = async function(req,res){    
    const resultado = await services.getLastDecision()
    res.status(200).send(resultado)
}

//INSERT RECORD
//Ejemplo de body ->
/*
{
    "Id_sensor": 1,
    "Current_value":155
}
*/
const insertRecord = async function(req,res){
    const { body } = req; //objeto a ser creado

    console.log(body)
    // COMPRUEBA QUE TODOS LOS CAMPOS TENGA VALORES
    if (
        body.Id_sensor==""         
    ) {        
        res.status(400)
           .send({
            status:"Error", data:{
                error:"Faltan datos"}
            })
        return 
    }
    // *** OBJETO QUE CONTIENE LA INFORMACION DEL NUEVO SENSOR ***
    const newSensor = {
        Id_sensor: body.Id_sensor,
        Current_value: body.Current_value,        
    };

    const resultado = await services.insertRecord(newSensor)
    
    res
    .setHeader('content-type', "application/json") //'text/plain')
    .status(201)
    .send(resultado)

}

//INSERT NEW 
//Ejemplo de body ->
/*
{
    "Velocidad": 50,
    "Distancia":25,
    "Decision":5
}
*/

const insertDecision = async function(req,res){
    
    const { body } = req; //objeto a ser creado

    // COMPRUEBA QUE TODOS LOS CAMPOS TENGA VALORES
    if (
        !body.Velocidad ||
        !body.Distancia ||
        !body.Decision       
    ) {        
        res.status(400)
           .send({
            status:"Error", data:{
                error:"Faltan datos"}
            })
        return 
    }
    // *** OBJETO QUE CONTIENE LA INFORMACION DEL NUEVO SENSOR ***
    const newSensor = {
        Velocidad: body.Velocidad,
        Distancia: body.Distancia,   
        Decision: body.Decision     
    };

    const resultado = await services.insertDecision(newSensor)
    
    res
    .setHeader('content-type', "application/json") //'text/plain')
    .status(201)
    .send(resultado)


}


module.exports = {
    getAll_records,
    getLast_Record,
    getLastDecision,

    insertRecord,
    insertDecision,
}
