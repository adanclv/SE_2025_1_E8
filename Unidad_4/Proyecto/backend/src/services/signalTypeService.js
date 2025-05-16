const db = require("../models/SignalTypeSP")

const insertSignalType = async (body) => {
    const { name } = body
    const res = await db.SP_Insert_SignalType(name)
    return res
}

const getAllSignalType = async () => {
    const res = await db.SP_GetAll_SignalType()
    return res
}

const getSignalType = async (id) => {
    const res = await db.SP_Get_SignalType_ById(id)
    return res
}

const updateSignalType = async (body) => {
    const { id, name } = body

    const res = await db.SP_Update_SignalType(id, name)
    return res
}

const deleteSignalType = async (id) => {
    const res = await db.SP_Delete_SignalType(id)
    return res
}

module.exports = {
    insertSignalType,
    getAllSignalType,
    getSignalType,
    updateSignalType,
    deleteSignalType
}