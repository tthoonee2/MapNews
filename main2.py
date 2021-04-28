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


#print(paragraph_cleaned)
#up until here it is debugged
list_rep = []
i = 0
for pars in paragraph_cleaned:
    sloc = pars.find('via ')# or 'piazza ' or 'viale ' or 'corso ')
    if sloc != -1:
        print(sloc)
        print(True)
        listofvie.append(re.find('via ',pars))
        print(listofvie)
        print(pars)
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