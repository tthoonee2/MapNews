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

for pars in paragraph_cleaned:
    sloc = pars.find('via ')# or 'piazza ' or 'viale ' or 'corso ')
    if sloc != None:
        listofvie.append(pars.search('via ' or 'piazza ' or 'viale ' or 'corso '))
        part = pars[sloc:25]
        regex = r"(\b[A-Z].*?\b)"
        matches = re.compile(regex, re.MULTILINE)
        listofvie[pars] += ' '
        listofvie[pars] += matches.findall(pars)
    
    
print(listofvie)
        
        
    

"""
import re
stringcas = 'ciccio pasticcio Vediamo se restituisce'
regex = r"(\b[A-Z].*?\b)"

result = 
print(result)

"""