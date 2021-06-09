# Cristian Javier Benavides Morales
# Prueba practica Ralop

import requests
import pandas as pd
import json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=PSDnlPGCpYbq3i3zasWIMHL1DkN2wIlF5bx4ovjS'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    listaId =[]
    listaImg=[]
    listaCam=[]
    listaRover=[]
    
    for el in data['photos']:
        listaId.append(el['id'])
        listaImg.append(el['img_src'])
        listaCam.append(el['camera']['full_name'])
        listaRover.append(el['rover'])



    # salida formato json
    output = json.dumps(data,indent=1)
    print(output)

    table = pd.DataFrame({'Id': listaId,'Img':listaImg,'Camara': listaCam,'Rover':listaRover}, index=list(range(1,len(listaId)+1))) 
    # salida como una tabla 
    # print(table)

    # archivo con informacion puntual
    table.to_csv('Informe_Mars-photos.csv')

    # si se desea ver completamente toda la informacion
    # print(data)



