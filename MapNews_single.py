#Codice parte 1 (funzionante le i sino estrazione via) manca ottimizazione, error handling e debugging di ultime cose).


from os import read
import urllib.request
import re


paragraph_vector = []
#creazione e apertura di un file di testo per semplificare il processo di scrittura delle stringhe dei paragrafi

file = open("extracted_paragraphs.txt", "w")
file = open("extracted_paragraphs.txt", "a")

#da sistemare a mo di funzione
link = input('inserisci il link:\n')
link_management = urllib.request.urlopen(link)
html_page = link_management.read()
#print(html_page) #restituzione in tipo Byte
html_page = html_page.decode("utf-8") #convertito in formato stringa da cui poi cercare


#prima scrematura - ricavo i paragrafi:

regex = r"<p>.+</p>"
test_str = html_page

matches = re.finditer(regex, test_str, re.MULTILINE)
matches = re.finditer(regex, test_str)
 #   if stringcheck.isupper(char_pos + len('via' or 'corso' or 'piazza' or 'viale')
  #  file_list.pop(i).split 

for matchNum, match in enumerate(matches, start=1):  #ITS REGEX TIMEEEE!
    
    file.write("Match {matchNum} was found at {start}-{end}: {match} \n ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        file.write("Group {groupNum} found at {start}-{end}: {group} \n".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


def P_extract_list():
    file = open("extracted_paragraphs.txt", "a")
    file = str(file)
    type(file)
    ii= 0
    file_list = []
    for ii in range(file.count('Match')):
        file_list.append(file.split('Match'))
    ii = 0
    for ii in file_list:
        print(file_list[ii]) #just for a test

    return file_list

#list should now contain the strings separately.
#for each string of the list evaluate if there is the word via/corso/piazza/viale, if there is return the index of the value
#from that index extract the words having a capital letter following via

def parcella_finder(string):
    if string.find('via ') != -1:
        parcella = 'via '
        return parcella
    elif string.find('viale') != -1:
        parcella = ('viale ')
        return parcella
    elif string.find('corso ') != -1:
        parcella = ('corso ')
        return parcella
    elif string.find('piazza ') != -1:
        parcella = ' piazza '
        return parcella
    else:
        pass



file_list = P_extract_list()
i = 0
for i in file_list:
    string = file_list[i]
    parcella = parcella_finder(string)
    if ('via' or 'corso' or 'piazza' or 'viale') is string:
        da_via_in_poi = string.split('via' or 'corso' or 'piazza' or 'viale')
        da_via_in_poi = da_via_in_poi[-1]
        via = ''
        for io in range(len(da_via_in_poi)):
            if da_via_in_poi[io].isspace() and da_via_in_poi[io+1].isupper():
                via = via + da_via_in_poi[io]
            elif da_via_in_poi[io].isupper():
                via = via + da_via_in_poi[io]
            elif da_via_in_poi[io].isspace():
                break
            elif da_via_in_poi[io] == '.':
                break
            elif da_via_in_poi[i].islower():
                via = via + da_via_in_poi[io]

            via = via
    else:
        pass

    totale = parcella + via
    print(totale)
    



#Codice parte 2: geocoding (da indirizzo a cooridinate)(funzionante) e upload (tramite api)(non funzionante)

import json
import requests
import geojson


def geocoding(street_name): # Riceve la via in formato API (+ al posto degli spazi)
   # riceve la richiesta e salva la lista dei risultati in results
   r = requests.get('https://nominatim.openstreetmap.org/search?q=' + street_name + '+Milano+Italia&format=json&countrycode=it&addressdetails=1&viewbox=9.05,45.40,9.3,45.55')

   results = r.json()

   #trova il primo risultato con città milano e ne estrae le coordinate. avvisa se non è stato trovato
   success = False

   for i in range(0, len(results)):
       if 'city' in results[i]['address'].keys():
           if results[i]['address']['city']=='Milano':
               success = True
               coordinates = [ results[i]['lon'],results[i]['lat'] ]
               break

   if success == False:
       return 'Indirizzo non trovato'
   else:
       return coordinates


news_title = "Titolo della notizia"
news_link = "www.google.it"

address_text = "Piazza Abbiategrasso"

coordinates = geocoding(address_text.replace(" ","+"))
description = address_text




json_sending = {
   "type": "FeatureCollection",
   "features":
       [
           {"type": "Feature", #"id": 236910192,
           "geometry": {"type": "Point", "coordinates": coordinates},
           "properties": {
               "title": news_title,
               "description": description,
               "url": news_link,
               "marker-color": "#309504"}
           }
       ]
   }

api_maphub_url = 'https://maphub.net/api/1/map/upload'

api_key = '65tUsNddOTxsWINn'


args = {
   'file_type': 'geojson',
   'visibility': 'public',
   'title': 'Upload news',
   'short_name': 'uploaded-news',
}

headers = {
   'Authorization': 'Token ' + api_key,
   'MapHub-API-Arg': json.dumps(args)
}


r = requests.post(api_maphub_url, headers=headers, data=geojson.dumps(json_sending))

print(r.json())

