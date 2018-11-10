# -*- coding: utf-8 -*-
"""
Author: Atul Singh
Date:  Nov 10, 2018
Usgae: python <ENV>

This Python Script read the input config files which contains the service url
and their request and call the services and records their responses. 
"""

import concurrent.futures
import requests
from string import Template
import time
import xml.etree.ElementTree as ET
import json
import sys

#checking for arguement

if len(sys.argv) < 2 :
	print("Usage: python <ENV> [LineNo]")
	print("ENV : QA, IST")
	sys.exit(1);
elif len(sys.argv)==2 :
	env=sys.argv[1]
else:
	env=sys.argv[1]
	lineno=env=sys.argv[2]

	
def env_conf(env):
	"returning env conf file"
	return (env+'.cnf', 'outok'+env, 'outerr'+env)

if env=='QA':
	inputfile='WebService_HealthCheck_QA.config'
	outputokfile='WebService_HealthCheck_QA.out'
	outputerrorfile='WebService_HealthCheck_QA.err'
	cert_file_path = "nonPrd.cer"
	key_file_path = "nonPrd_keys.key"
elif env=='IST':
	inputfile='WebService_HealthCheck_IST.cnf'
	outputokfile='WebService_HealthCheck_IST.out'
	outputerrorfile='WebService_HealthCheck_IST.err'
	cert_file_path = "nonPrd.cer"
	key_file_path = "nonPrd_keys.key"
else:
	print("Enter the correct env value")
	print("Usage: python <ENV> [LineNo]")
	print("ENV : QA, IST")
	sys.exit(2);	

urlTemplate = Template('https://dummy_url')

headers = {'Content-Type':'text/xml;charset=UTF-8'}

# Retrieve a single page and report the URL and contents
def fire_rest_get_request(url, timeout):
    start_time = time.time()
    response=requests.get(url, timeout=timeout,headers=headers)
    end_time=time.time() - start_time
    return {'responsetime':end_time,'response':response}


def fire_rest_post_request(url, timeout, inp):
	start_time = time.time()
	cert=(cert_file_path,key_file_path)
	response=requests.post(url, timeout=timeout,headers=headers, data=inp, cert=cert, verify=False)
	end_time=time.time() - start_time
	data=response.json()
	return {'responsetime':end_time,'response':response, 'data':data}


def write(text,filename):
    file = open(filename, 'a')
    file.write(text+'\n')   
    file.close()
    
with open(inputfile) as fh:
	timeout=15
	for line in fh:
		line_arr = line.strip('\n').split('|')
		eg = line_arr[0]
		sname = line_arr[1]
		url = line_arr[2]
		req_data=line_arr[3]
		resp = fire_rest_post_request(url, timeout, req_data)
		write(eg+'|'+sname+'|'+str(resp['data']),outputokfile)
        
        
