const express = require('express')
const v1 = require('./v1/routes/Routes')

const app = express();
const PORT = process.env.PORT || 3000;
app.use(express.json()) //json parser

app.use("/api/v1", v1)

app.get("/",(req,res)=>{
    res.send(`<h1>API RESTful en NodeJS para Servicios Embebidos</h1>`)
})

app.listen(PORT, () => {
    console.log(`Servidor escuchando en el Puerto: ${PORT}`);
})