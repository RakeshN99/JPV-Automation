import requests
from bs4 import BeautifulSoup

import time
from bs4 import BeautifulSoup
url="C:/Users/hp/Downloads/Openreach NGWFMT-Ethernet.html"
elements=[]

try:
    with open(url,'r',encoding='utf-8') as file:
        soup=BeautifulSoup(file, 'html.parser')
        elements=soup.find_all('mat-icon',class_= 'mat-icon material-icons mat-icon-no-color')
        
        for element in elements:
            innertext = element.get_text(strip=True) 
            if innertext == "pause":
                print("The icon text is correctly set to 'pause'.",end="")
                e1=soup.find('span',class_="ag-cell-value")
                print(e1.get_text())
                
                
        
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("error occured   ",e)