const service = require('../services/decisionService')

const insertDecision = async(req, res) => {
    const { body } = req
    if (!body.current_value || !body.decision) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await service.insertDecision(body)
    res.setHeader('content-type', "application/json").status(201).send(result)
}

const getAllDecisiones = async (req, res) => {
    const result = await service.getAllDecisiones()
    res.status(200).send(result)
}

const getLastDecision = async (req, res) => {
    const result = await service.getLastDecision
    res.status(200).send(result)
}

const updateDecision = async (req, res) => {
    const { body } = req

    if (!body.id_decision || !body.current_value || !body.decision) {
        res.status(400).send(
            { status: "error", message: "Faltan datos" }
        )
        return
    }

    const result = await service.updateDecision(body)
    res.setHeader('content-type', "application/json").status(200).send(result)
}

const deleteDecision = async (req, res) => {
    const { id } = req.params
    if (!isNaN(id)) {
        const result = await service.deleteDecision(id)
        res.status(200).send(result)
    } else {
        res.status(400).json({ status: "error", message: "ID inválido" });
    }
}

module.exports = {
    insertDecision,
    getAllDecisiones,
    getLastDecision,
    updateDecision,
    deleteDecision
}
