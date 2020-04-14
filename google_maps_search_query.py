# encoding - UTF-8
import xml.etree.ElementTree as ET
import openpyxl
from xlsxwriter.utility import xl_rowcol_to_cell
import time
import requests
from bs4 import BeautifulSoup
import urllib3
import json
import pandas as pd

#pattern = '/url?q='
#warnings.filterwarnings("ignore", category=ResourceWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Google_search(params):
    #url = 'https://www.google.com/maps/place/'
    #search_url=url+params['query']+'+/@'++'/data='+str(params['start'])
    #search_url='https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='+params['query']+'&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyBYbpDFvto8xyjZMLG9sIE47PI_Kycx7BQ'
    dfcols = ['NAME','ADDRESS','LATITUDE','LONGITUDE']
    df_xml = pd.DataFrame(columns=dfcols)
                                                                        # Enter the API key here after enabling the google maps API from GCP:
    search_url='https://maps.googleapis.com/maps/api/place/textsearch/xml?query='+params['query']+'&key=################################'
    resp=requests.get(search_url,verify=False)

    #create soup object
    soup=BeautifulSoup(resp.text,'xml')
    #print(soup)
    result_links=soup.find_all('result')
    name_links=soup.find_all('name')
    address_links=soup.find_all('formatted_address')
    location_links=soup.find_all('location')
    lat_link=soup.find_all('lat')
    lng_link=soup.find_all('lng')

    for i in range(0,len(result_links)):
        name_loc=name_links[i].get_text()
        address_loc=address_links[i].get_text()
        lat_coord=lat_link[i].get_text()
        lng_coord=lng_link[i].get_text()
        df_xml = df_xml.append(pd.Series([name_loc, address_loc,lat_coord,lng_coord], index=dfcols),ignore_index=True)

    print(df_xml)
    df_xml.to_excel("Location_details.xlsx")

val=0
input=input("Enter the thing you want to search : ")
input=input.replace("+ ","%2B+")
#print(input)
params={'query':str(input),'start':val}
t1=time.perf_counter()
Google_search(params)
t2=time.perf_counter()
t=t2-t1
print("-"*40)
print("Execution Time: ",t)
print("-"*40)
