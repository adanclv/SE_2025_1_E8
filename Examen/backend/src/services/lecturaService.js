const db = require("../models/LecturaSP")

const insertLectura = async (body) => {
    const { valor, estado } = body
    const res = await db.SP_Insert_Lectura(valor, estado)
    return res
}

const getAllLecturas = async () => {
    const res = await db.SP_GetAll_Lecturas()
    return res
}

const getLastLectura = async (id) => {
    const res = await db.SP_Last_Lectura()
    return res
}

module.exports = {
    insertLectura,
    getAllLecturas,
    getLastLectura
}