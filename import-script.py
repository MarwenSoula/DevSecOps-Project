"""

Description: Using python 2
1. Creates a product type
2. Creates a product using that product type if it does not already exist
3. Creates an engagement within that product
4. Uploads 2 vulnerability scan results

"""

from random import randint
from datetime import datetime, timedelta
import os
import requests
import json
import xml.etree.ElementTree as ET
import time


# *************************SETUP CONNECTION SECTION***************************
host = 'http://20.199.42.60:8080/'
api_key = "d829790e43adf05890b0dbe0bfa5bafe85162037"
key = 'Token ' + api_key
user_id = 1 #default user
prod_name = "Spring Boot Microservice Application" #Product Name
prod_desc = "Fisrt test"
eng_name = "Engagement_Spring_Boot" #Engagement Name
start_date = datetime.now()
end_date = start_date+timedelta(days=180)

headers = {
    'Authorization': key,
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
Upload_headers = {
    'Authorization': key,
    'Accept': 'application/json',
    #'Content-Type': 'multipart/form-data'


}
# *************************PRODUCT TYPE SECTION***************************
#Create product type function:
def create_prod_type():
    data = {
        "name": "Inovation IT for Hospitals",
        "created": start_date.strftime("%Y-%m-%d"),
        "updated": start_date.strftime("%Y-%m-%d"),
        "critical_product": False,
        "key_product": False
        }
    response = requests.post(host+'/api/v2/product_types/', headers=headers, data=json.dumps(data))
    print "Creating Product Type response: " + str(response)
create_prod_type()

# *************************PRODUCT SECTION***************************

def get_product_id(p_name):
    products = requests.get(host+'/api/v2/products/', headers=headers)
    data = json.loads(products.text)
    for product in data["results"]:
        if p_name == product['name']:
            product_id = product['id']
            return product_id

prod_id = get_product_id(prod_name)

def create_product(p_name):
    data = {
        "name": p_name,
        "description": prod_desc,
        "prod_type": 1,
    }
    if prod_id == None:
        response = requests.post(host+'/api/v2/products/', headers=headers, data=json.dumps(data))
        print "[+] Product creation response: " + str(response)
    else:
        print "[-] Product not created as it already exists ID: " + str(prod_id)

create_product(prod_name)

# *************************ENGAGEMENT SECTION***************************

def get_engagement_id(e_name):
    engagements = requests.get(host+'/api/v2/engagements/', headers=headers)
    data = json.loads(engagements.text)
    for engagement in data["results"]:
        if e_name == engagement['name'] and engagement['product'] == prod_id:
            e_id = engagement['id']
            return e_id

eng_id = get_engagement_id(eng_name)

def create_engagement(e_name):
    data = {
        "status": "In Progress",
        "product": prod_id,
        "name": e_name,
        "lead": user_id,
        "target_end": end_date.strftime("%Y-%m-%d"),
        "target_start": start_date.strftime("%Y-%m-%d")
    }
    if eng_id == None:
        response = requests.post(host+'/api/v2/engagements/', headers=headers, data=json.dumps(data))
        print "[+] Engagement creation response: " + str(response)
    else:
        print "[-] Engagement not created as it already exists ID: " + str(eng_id)

prod_id = get_product_id(prod_name)
create_engagement(eng_name)

# *************************UPLOAD RESULTS SECTION***************************


def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('trivy-deparment-service.json', open('trivy-deparment-service.json','rb'), 'text/xml')  }
    data = {
        'scan_type':'Trivy Scan',
        'tags':  'dep:0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Trivy Scan' +" Response: "+ str(response.content)

upload()

def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('trivy-employee-service.json', open('trivy-deparment-service.json','rb'), 'text/xml')  }
    data = {
        'scan_type':'Trivy Scan',
        'tags':  'emp:0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Trivy Scan' +" Response: "+ str(response.content)

upload()

def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('trivy-Oraganization-service.json', open('trivy-deparment-service.json','rb'), 'text/xml')  }
    data = {
        'scan_type':'Trivy Scan',
        'tags':  'org:0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Trivy Scan' +" Response: "+ str(response.content)

upload()

def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('trivy-gateway-service.json', open('trivy-deparment-service.json','rb'), 'text/xml')  }
    data = {
        'scan_type':'Trivy Scan',
        'tags':  'gat:0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Trivy Scan' +" Response: "+ str(response.content)

upload()

def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('trufflehog_report.json', open('trufflehog_report.json','rb'), 'text/xml')  }
    data = {
        'scan_type':'Trufflehog Scan',
        'tags':  '0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Trufflehog Scan' +" Response: "+ str(response.content)

upload()

def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('dependency-check-report.xml', open('dependency-check-report.xml','rb'), 'text/xml')  }
    data = {
        'scan_type':'Dependency Check Scan',
        'tags':  '0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'Dependency Check Scan' +" Response: "+ str(response.content)

upload()


def upload():
    # Assignment: Finish the upload function
    eng_id = get_engagement_id(eng_name)
    files = {
        'file': ('ZAP-report.xml', open('ZAP-report.xml','rb'), 'text/xml')  }
    data = {
        'scan_type':'ZAP Scan',
        'tags':  '0.1',
        'verified': 'false',
        'active': 'true',
        'scan_date': start_date.strftime("%Y-%m-%d"),
        'engagement_name': eng_name,
        'product_name': prod_name
            }
    response = requests.post(host+'/api/v2/import-scan/', headers=Upload_headers, files=files, data=data)
    print "[+] Uploading " + 'ZAP Scan' +" Response: "+ str(response.content)

upload()
