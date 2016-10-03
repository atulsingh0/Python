import json
import csv
import os
import sys

if len(sys.argv)<2:
    exit()
elif (os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])) is False:
    print("Directory path is not exists")
    print("Usgae: python flattenJson.py <input-dir> <output-dir>")
    exit()
else:
    print("success")
	

indir = sys.argv[1]
outdir = sys.argv[2]
all_files = [os.path.join(indir,file) for file in os.listdir(indir)]

for file in all_files:
	fjson = open(file, "r")
	fcsv = open(os.path.join(outdir,file)+".csv","w")
	csvs = csv.writer(fcsv, delimiter='|',lineterminator='\n')
	lineno=0
	for line in fjson:
		data = json.loads(line)
		csv_line = []
		csv_header = []
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
		csvs.writerow(csv_line)
    
	fjson.close()
	fcsv.close()
