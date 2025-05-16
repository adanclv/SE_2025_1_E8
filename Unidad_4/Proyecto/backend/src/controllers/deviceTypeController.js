const services = require("../services/deviceTypeService")

const insertDeviceType = async (req, res) => {
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

    const result = await services.insertDeviceType(newType)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllDeviceTypes = async (req, res) => {
    const result = await services.getAllDeviceType()
    res.status(200).send(result)
}

const getDeviceType = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.getDeviceType(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

const updateDeviceType = async (req, res) => {
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

    const result = await services.updateDeviceType(newType)
    res.setHeader('content-type', "application/json").status(200).send(result)
}

const deleteDeviceType = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.deleteDeviceType(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

module.exports = {
    insertDeviceType,
    getAllDeviceTypes,
    getDeviceType,
    updateDeviceType,
    deleteDeviceType
}