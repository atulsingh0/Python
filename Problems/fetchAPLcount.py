import json

fh = open("Python/Problems/fetchAPLcount.txt")   # set the input file path
datadic = dict()

lines = fh.readlines()
for line in lines[1:-1]:  # removing first and last line which is [ and ]
    line=line.rstrip(',\n')  # removing last comma , and new line \n
    #print(line)
    data = json.loads(line)
    key = data.keys()
    for word in [value for key, value in data.items() if 'apl' in key.lower()]:
        if len(word) > 0:
            datadic[word] = datadic.get(word, 0) + 1   
print(datadic)    
fh.seek(0)