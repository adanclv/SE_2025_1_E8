const express = require('express')

const devicesController = require('../../controllers/devicesController')
const deviceTypeController = require("../../controllers/deviceTypeController")
const signalTypeController = require("../../controllers/signalTypeController")
const recordController = require("../../controllers/recordsController")
const decisionController = require("../../controllers/decisionController")

//RUTAS
const router = express.Router()

// /api/v1-actuators/actuators
router
    // DEVICE TYPE
    // http://localhost:3000/api/v1/devicetype/
    .get("/devicetype", deviceTypeController.getAllDeviceTypes)

    // http://localhost:3000/api/v1/devicetype/1
    .get("/devicetype/:id", deviceTypeController.getDeviceType)

    // http://localhost:3000/api/v1/devicetype
    .post("/devicetype", deviceTypeController.insertDeviceType)

    // http://localhost:3000/api/v1/devicetype
    .put("/devicetype", deviceTypeController.updateDeviceType)

    // http://localhost:3000/api/v1/devicetype/1
    .delete("/devicetype/:id", deviceTypeController.deleteDeviceType)

    // SIGNAL TYPE
    // http://localhost:3000/api/v1/signaltype/
    .get("/signaltype", signalTypeController.getAllSignalType)

    // http://localhost:3000/api/v1/signaltype/1
    .get("/signaltype/:id", signalTypeController.getSignalType)

    // http://localhost:3000/api/v1/signaltype
    .post("/signaltype", signalTypeController.insertSignalType)

    // http://localhost:3000/api/v1/signaltype
    .put("/signaltype", signalTypeController.updateSignalType)

    // http://localhost:3000/api/v1/signaltype/1
    .delete("/signaltype/:id", signalTypeController.deleteSignalType)

    // DEVICE INFO
    // http://localhost:3000/api/v1/device/
    .get("/device", devicesController.getAllDevices)

    // http://localhost:3000/api/v1/device/1
    .get("/device/:id", devicesController.getDevice)

    // http://localhost:3000/api/v1/device
    .post("/device", devicesController.insertDevice)

    // http://localhost:3000/api/v1/device
    .put("/device", devicesController.updateDevice)

    // http://localhost:3000/api/v1/device/19
    .delete("/device/:id", devicesController.deleteDevice)

    // DEVICE RECORD
    // http://localhost:3000/api/v1/record/
    .get("/record", recordController.getAllRecords)

    // http://localhost:3000/api/v1/record/1
    .get("/record/:id", recordController.getLastRecord)

    // http://localhost:3000/api/v1/record
    .post("/record", recordController.insertRecord)

    // http://localhost:3000/api/v1/record
    .put("/record", recordController.updateRecord)

    // http://localhost:3000/api/v1/record/19
    .delete("/record/:id", recordController.deleteRecord)

    // DECISION
    // http://localhost:3000/api/v1/decision/
    .get("/decision", decisionController.getAllDecisiones)

    // http://localhost:3000/api/v1/decision/last
    .get("/decision/last", decisionController.getLastDecision)

    // http://localhost:3000/api/v1/decision
    .post("/decision", decisionController.insertDecision)

    // http://localhost:3000/api/v1/decision
    .put("/decision", decisionController.updateDecision)

    // http://localhost:3000/api/v1/decision/19
    .delete("/decision/:id", decisionController.deleteDecision)
module.exports = router;