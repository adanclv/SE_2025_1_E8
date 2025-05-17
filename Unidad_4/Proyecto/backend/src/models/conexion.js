const sql = require('mssql')

const config = {
    user:'adan',
    password:'adan12',
    server:'localhost',
    database:'BD_UNIDAD_4_SE_2025_1',
    options: {
        encrypt: true,
        trustServerCertificate: true
      }
}

const getConnection = async function (){
    try{
        const conexion = await sql.connect(config)
        return conexion
    }
    catch(error){
        console.log(error)
    }    
}

module.exports = {
    getConnection
}