const sql = require('mssql')

const config = {
    user:'adan',
    password:'adan12',
    server:'localhost',
    database:'BD_PROY_INTEGRADO_SE',
    options: {
        encrypt: true, // for azure
        trustServerCertificate: true // change to true for local dev / self-signed certs
      }
}

const getConnection = async function (){
    try{
        const conexion = await sql.connect(config) //conexion es el objeto que representa la conexion logica con la base de datos
        return conexion
    }
    catch(error){
        console.log(error)
    }    
}

module.exports = {
    getConnection
}