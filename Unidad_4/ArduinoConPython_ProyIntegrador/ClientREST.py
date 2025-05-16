## pip install requests   Fuente: https://pypi.org/project/requests/
import requests

url_base = "http://localhost:3000/api/v1"

def getAll_records():
    #Get
    print("\nGET ALL RECORDS: ")
    url = url_base + "/"
    response = requests.get(url, verify=False)
    result = response.json()
    print(result) #lista de diccionarios ...
    print(response.status_code)

    print("Table Info:")
    for register in result:
        for key in register:
            print("Attribute: ", key, " Value: ", register[key])
        print("\n")
###############################################################################################################################
def getLast_RecordById(id):
    # Get
    print("\nGET LAST RECORD: ")
    url = url_base + "/optimizar/" +str(id)
    response = requests.get(url, verify=False)
    result = response.json()
    print(result)  # diccionario ...
    print(response.status_code)

    print("Table Info:")
    for key in result:
        print("Attribute: ", key, " Value: ", result[key])
    print("\n")
###############################################################################################################################
def getLastDecision():
    #Get with parameters
    #print("GET LAST DECISION: ")
    url = url_base + "/decision"
    response = requests.get(url, verify=False)
    result = response.json()
    #print("Value of Device: ", result)
    #print(response.status_code)

    #for key in result:
    #    print("Attribute: ", key, " Value: ", result[key])
    #print("\n")

    return result["decision"]
###############################################################################################################################
def insertRecord(id_device, current_value):
    #Post
    #print("\n\nINSERT RECORD")
    import json
    Id_device = id_device
    Current_value = current_value
    url = url_base + "/registros"
    headers =  {"Content-Type":"application/json"}
    body = {
        "Id_device": Id_device,
        "Current_value": Current_value
    }
    response = requests.post(url, data=json.dumps(body), headers=headers, verify= False)
    print(response.json())
    print(response.status_code)
###############################################################################################################################
def insertDecision(velocidad, distancia, decision):
    #Post
    print("\n\nINSERT DECISION")
    import json
    Velocidad = velocidad
    Distancia = distancia
    Decision = decision
    url = url_base + "/decision"
    headers =  {"Content-Type":"application/json"}
    body = {
        "Velocidad": Velocidad,
        "Distancia": Distancia,
        "Decision": Decision
    }
    response = requests.post(url, data=json.dumps(body), headers=headers, verify= False)
    print(response.json())
    print(response.status_code)
###############################################################################################################################

#getAll_records()
getLast_RecordById(4)
#getLastDecision()

#insertRecord(4, 120)
#insertDecision(100, 900, 8)

###############################################################################################################################


