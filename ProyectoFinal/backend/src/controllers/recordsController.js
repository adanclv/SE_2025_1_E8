const service = require('../services/recordService')

const insertRecord = async(req, res) => {
    const { body } = req
    if (!body.id_device || !body.current_value || isNaN(body.id_device)) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await service.insertRecord(body)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllRecords = async (req, res) => {
    const result = await service.getAllRecords()
    res.status(200).send(result)
}

const getLastRecord = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await service.getLastRecord(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

const updateRecord = async (req, res) => {
    const { body } = req

    if (!body.id_record || !body.id_device || !body.current_value) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await service.updateRecord(body)
    res.setHeader('content-type', "application/json").status(200).send(result)
}

const deleteRecord = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await service.deleteRecord(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

module.exports = {
    insertRecord,
    getAllRecords,
    getLastRecord,
    updateRecord,
    deleteRecord
}
