const db = require('../models/DecisionSP')

const insertDecision = async (body) => {
    const { current_value, decision } = body
    const res = await db.SP_Insert_Decision(current_value, decision)
    return res
}

const getAllDecisiones = async () => {
    const res = await db.SP_GetAll_Decision()
    return res
}

const getLastDecision = async () => {
    const res = await db.SP_Get_LastDecision()
    return res
}

const updateDecision = async (body) => {
    const { id_decision, current_value, decision } = body
    const res = await db.SP_Update_Decision(id_decision, current_value, decision)
    return res
}

const deleteDecision = async (id) => {
    const res = await db.SP_Delete_Decision(id)
    return res
}

module.exports = {
    insertDecision,
    getAllDecisiones,
    getLastDecision,
    updateDecision,
    deleteDecision
}
