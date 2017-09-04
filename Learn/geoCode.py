
import urllib
import json

#serviceurl = 'https://maps.googleapis.com/maps/api/directions/json?'
serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'
api_key = 'AIzaSyBLe7mgfpYfciZRkdQfG_aANo4dfkq-F_0'

while True:
    address = input('Enter location: ');
    if len(address) < 1 : break
	#destination = raw_input('Enter Destinaton location: ')
    #if len(address) < 1 : break
    values = {'address': address,
                'key':api_key}
	
    #url = serviceurl + urllib.urlencode(values)
    print ('Retrieving', serviceurl)
    uh = urllib.request.Request(serviceurl, data=values)
    data = uh.read()
    print ('Retrieved',len(data),'characters')
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue
    print (json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print (location)