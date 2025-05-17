const services = require('../services/lecturaService')

const insertLecura = async (req, res) => {
    const { body } = req
    if (!body.valor || !body.estado) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await services.insertLectura(body)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllLecturas = async(req, res) => {
    const result = await services.getAllLecturas()
    res.status(200).send(result)
}

const getLastLectura = async(req, res) => {
    const result = await services.getLastLectura()
    res.status(200).send(result)
}

module.exports = {
    getLastLectura,
    insertLecura,
    getAllLecturas
}