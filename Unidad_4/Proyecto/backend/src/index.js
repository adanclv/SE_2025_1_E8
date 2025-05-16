const express = require('express') // importacion de modulo para crear la api
const v1 = require('./v1/routes/Routes')

const app = express();
const PORT = process.env.PORT || 3000;
app.use(express.json()) //json parser

app.use("/api/v1", v1)

app.get("/",(req,res)=>{
    res.send(`<h1>API RESTful en NodeJS para Servicios Embebidos</h1>`)
})
//////////////////

// Actividad 3
// Iniciar
// Conectar
// Mandar a llamar

//inicia la api y ejecuta una funcion callback que retroalimenta el estado en la consola/terminal
app.listen(PORT, () => {
    console.log(`Servidor escuchando en el Puerto: ${PORT}`);
})