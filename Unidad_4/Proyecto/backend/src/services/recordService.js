const db = require('../models/RecordsSP')

const insertRecord = async (body) => {
    const { id_device, current_value } = body
    const res = await db.SP_Insert_Record(id_device, current_value)
    return res
}

const getAllRecords = async () => {
    const res = await db.SP_GetAll_Records()
    return res
}

const getLastRecord = async (id) => {
    const res = await db.SP_GetLast_Record(id)
    return res
}

const updateRecord = async (body) => {
    const { id_record, id_device, current_value } = body
    const res = await db.SP_Update_Record(id_record, id_device, current_value)
    return res
}

const deleteRecord = async (id) => {
    const res = await db.SP_DeleteRecord(id)
    return res
}

module.exports = {
    insertRecord,
    getAllRecords,
    getLastRecord,
    updateRecord,
    deleteRecord
}
