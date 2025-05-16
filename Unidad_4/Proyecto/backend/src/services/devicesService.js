const db = require("../models/DevicesSP")

const insertDevice = async (body) => {
    const { id_type, id_signal_type, name, vendor } = body
    const res = await db.SP_Insert_Device(id_type, id_signal_type, name, vendor)
    return res
}

const getAllDevices = async () => {
    const res = await db.SP_GetAll_Devices()
    return res
}

const getDevice = async (id) => {
    const res = await db.SP_Get_Device_ById(id)
    return res
}

const updateDevice = async (body) => {
    const { id_device, id_type, id_signal_type, name, vendor } = body

    const res = await db.SP_Update_Device(id_device, id_type, id_signal_type, name, vendor)
    return res
}

const deleteDevice = async (id) => {
    const res = await db.SP_Delete_Device(id)
    return res
}

module.exports = {
    insertDevice,
    getAllDevices,
    getDevice,
    updateDevice,
    deleteDevice
}