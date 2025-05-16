import json
import requests

url_base = "http://localhost:3000/api/v1"

def getAll_DeviceType():
    print('ALL TYPE OF DEVICES')
    route = "/devicetype"
    url = url_base + route
    response = requests.get(url)
    result = response.json()
    for register in result:
        for key in register:
            print("Attribute: ", key, " Value: ", register[key])

def getAll_Devices(route = "/device"):
    print('ALL DEVICES')
    url = url_base + route
    response = requests.get(url)
    result = response.json()
    for register in result:
        for key in register:
            print("Attribute: ", key, " Value: ", register[key])

def insertDevice(id_type, id_signal_type, name, vendor, route="/device"):
    print('INSERT DEVICE')
    url = url_base + route
    headers = {"Content-Type": "application/json"}
    body = {
        "id_type": id_type,
        "id_signal_type": id_signal_type,
        "name": name,
        "vendor": vendor
    }
    response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
    print(response.json())


def updateDevice(id_device, id_type, id_signal_type, name, vendor, route="/device"):
    print('UPDATE DEVICE')
    url = url_base + route
    headers = {"Content-Type": "application/json"}
    body = {
        "id_device": id_device,
        "id_type": id_type,
        "id_signal_type": id_signal_type,
        "name": name,
        "vendor": vendor
    }
    response = requests.put(url, data=json.dumps(body), headers=headers, verify=False)
    print(response.json())

def insertRecord(id_device, current_value, route='/record'):
    url = url_base + route
    headers = {"Content-Type": "application/json"}
    body = {
        "id_device": id_device,
        "current_value": current_value,
    }

    try:
        response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
        print(response.json())
    except requests.RequestException as err:
        print(f"Error al realizar la solicitud: {err}")

def insertDecision(current_value, decision, route='/decision'):
    url = url_base + route
    headers = {"Content-Type": "application/json"}
    body = {
        "current_value": current_value,
        "decision": decision
    }
    try:
        response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
        print(response.json())
    except requests.RequestException as err:
        print(f"Error al realizar la solicitud: {err}")

if __name__ == '__main__':
    # getAll_DeviceType()
    # insertDevice(1, 2, "SENSOR DE INTENSIDAD DE LUZ", "SE_CLASE")
    getAll_Devices()
    # updateDevice(5, 1, 2, "SENSOR DE INTENSIDAD DE LUZ", "SE_CLASE")