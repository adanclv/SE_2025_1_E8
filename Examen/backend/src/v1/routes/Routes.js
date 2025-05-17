const express = require('express')

const controller = require('../../controllers/lecturasController')

//RUTAS
const router = express.Router()

// /api/v1-actuators/actuators
router
    // http://localhost:3000/api/v1/lectura/
    .get("/lectura", controller.getAllLecturas)

    // http://localhost:3000/api/v1/lectura/last
    .get("/lectura/last", controller.getLastLectura)

    // http://localhost:3000/api/v1/lectura
    .post("/lectura", controller.insertLecura)

module.exports = router;