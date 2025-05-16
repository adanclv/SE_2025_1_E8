const services = require('../services/devicesService')

const insertDevice = async (req, res) => {
    const { body } = req
    if (!body.id_type || !body.id_signal_type || !body.name || !body.vendor) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await services.insertDevice(body)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllDevices = async(req, res) => {
    const result = await services.getAllDevices()
    res.status(200).send(result)
}

const getDevice = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.getDevice(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

const updateDevice = async (req, res) => {
    const { body } = req

    if (!body.id_device || !body.id_type || !body.id_signal_type || !body.name || !body.vendor) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await services.updateDevice(body)
    res.setHeader('content-type', "application/json").status(200).send(result)
}

const deleteDevice = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await services.deleteDevice(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

module.exports = {
    insertDevice,
    getAllDevices,
    getDevice,
    updateDevice,
    deleteDevice
}