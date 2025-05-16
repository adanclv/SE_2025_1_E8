const db = require("../models/DeviceTypeSP")

const insertDeviceType = async (body) => {
    const { name } =  body
    const res = await db.SP_InsertDeviceType(name)
    return res
}

const getAllDeviceType = async () => {
    const res = await db.SP_GetAll_DeviceType()
    return res
}

const getDeviceType = async (id) => {
    const res = await db.SP_Get_DeviceType_ById(id)
    return res
}

const updateDeviceType = async (body) => {
    const { id, name } = body

    const res = await db.SP_Update_DeviceType(id, name)
    return res
}

const deleteDeviceType = async (id) => {
    const res = await db.SP_Delete_DeviceType(id)
    return res
}

module.exports = {
    insertDeviceType,
    getAllDeviceType,
    getDeviceType,
    updateDeviceType,
    deleteDeviceType
}