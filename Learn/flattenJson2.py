# -*- coding: utf-8 -*-

import json
import csv
import os
import sys

if len(sys.argv)<2:
	print("Passed arguement is not correct")
	print("Usgae: python flattenJson.py <input-dir> <output-dir>")
	exit()
elif os.path.isdir(sys.argv[1]) is False:
	print("Input Directory path is not exists")
	print("Usgae: python flattenJson.py <input-dir> <output-file_absolute_path>")
	exit()
else:
	print("Processing Files............")
	

indir = sys.argv[1]
outfile = sys.argv[2]
all_files = [os.path.join(indir,file) for file in os.listdir(indir) if file.endswith(".txt")]
fcsv = open(outfile,"w")
csvs = csv.writer(fcsv, delimiter='|',lineterminator='\n')
lineno=0
csv_header = []

for file in all_files:
	fjson = open(file, "r")
	for line in fjson:
		data = json.loads(line)
		csv_line = []
		lineno=lineno+1
		for k,v in data.items():
			if isinstance(v,dict):
				csv_line.extend(json.loads(json.dumps(v)).values())
				if lineno==1:
					csv_header.extend([k+"."+key for key in json.loads(json.dumps(v)).keys()])
			else:
				csv_line.append(v)
				if lineno==1:
					csv_header.append(k)
		if lineno==1:
			csvs.writerow(csv_header)
		csv_line = ['NULL' if (isinstance(x,str) and len(x)<1) else x for x in csv_line ]
		csvs.writerow(csv_line)
	print(file + " is processed successfully.")
    
	fjson.close()
fcsv.close()

print ("All files are processed successfully")
print ("Output file is : "+outfile)
