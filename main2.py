#libraries needed
import requests
import re
from bs4 import BeautifulSoup

paragraph_cleaned = []
listofvie = []
url ='https://www.milanotoday.it/cronaca/ragazzo-precipita-scuola-salesiani.html'    #input('insert news link: ')
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
#test if it retrieves the html doc
paragraphs = soup.find_all('p')
for i in range(0,len(paragraphs)):
    paragraph_cleaned.append(paragraphs[i].text)

print(paragraph_cleaned)

#print(paragraph_cleaned)
#up until here it is debugged
list_rep = []
i = 0
sloc = []
for pars in paragraph_cleaned:
    sloc.append(pars.find('via '))# or 'piazza ' or 'viale ' or 'corso ')
    print(sloc)
    if sloc[i] != -1:
        print(sloc)
        print(True)
        listofvie.append(re.findall('via ',pars))
        print(listofvie)
        part = pars[sloc:25]
        print(part)
        listofvie[i] += ' '
        print(listofvie)
        listofvie[i] += re.findall(part,'([A-Z].\S+')                                #regex = r"(\b[A-Z].*?\b)"
        i += 1                                #matches = re.compile(regex, re.MULTILINE)
    else:
        print('no match')    
                                        #listofvie[pars] += matches.findall(pars)
    
    
print(listofvie)
        
        
    

"""
import re
stringcas = 'ciccio pasticcio Vediamo se restituisce'
regex = r"(\b[A-Z].*?\b)"

result = 
print(result)

"""