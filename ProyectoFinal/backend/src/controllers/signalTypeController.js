const services = require("../services/signalTypeService")

const insertSignalType = async (req, res) => {
    const { body } = req;

    console.log(body)
    if (!body.name || body.name.trim() === "") {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const newType = {
        name: body.name
    };

    const result = await services.insertSignalType(newType)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllSignalType = async (req, res) => {
    const result = await services.getAllSignalType()
    res.status(200).send(result)
}

const getSignalType = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.getSignalType(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
        return;
    }
}

const updateSignalType = async (req, res) => {
    const { body } = req

    if (!body.id_type || !body.name || body.name.trim() === "") {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const newType = {
        id: body.id_type,
        name: body.name
    };

    const result = await services.updateSignalType(newType)
    res.setHeader('content-type', "application/json").status(200).send(result)
}

const deleteSignalType = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.deleteSignalType(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
        return;
    }
}

module.exports = {
    insertSignalType,
    getAllSignalType,
    getSignalType,
    updateSignalType,
    deleteSignalType
}