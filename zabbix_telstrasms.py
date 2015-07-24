#!/usr/bin/python
import urllib
import urllib2
import json
import datetime
import sys

if len(sys.argv) < 4:
    sys.exit("Usage: telstrasms.py RECIPIENT SUBJECT BODY")

smsrcpt = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

key="YOURKEYHERE"
secret="YOURSECRETHERE"
url="https://api.telstra.com/v1/oauth/token?client_id="+key+"&client_secret="+secret+"&grant_type=client_credentials&scope=SMS"
now = datetime.datetime.today()
authfile = '/tmp/telstraauth'

def GetAuthToken( url, now, key, secret ):
    response = urllib2.urlopen(url)
    newtokendict = json.loads(response.read())
    newtokendict["datetime"] = str(now)
    authtoken = newtokendict["access_token"]
    newjsontoken = json.JSONEncoder().encode(newtokendict)
    f = open(authfile,'w')
    print "new token : "+newjsontoken
    f.write(newjsontoken)
    f.close()
    return authtoken


f = open(authfile,'r+')
filetoken = f.read()
f.close()
try:
    dicttoken = json.loads(filetoken)
    authtoken = dicttoken["access_token"]
    dtobj = datetime.datetime.strptime(dicttoken["datetime"], '%Y-%m-%d %H:%M:%S.%f')
    expires = dtobj + datetime.timedelta(0,int(dicttoken["expires_in"]))
    if expires < now:
        print "expired"
        authtoken = GetAuthToken(url, now, key, secret)
    else:
        print "not expired"
except ValueError:
    print "Invalid JSON. Retrieving New Token"
    authtoken = GetAuthToken(url, now, key, secret)


smsdata = { 'to':smsrcpt, 'body':subject+" "+body }
headers = { 'Content-type':'application/json','Authorization':'Bearer '+str(authtoken) }
url = "https://api.telstra.com/v1/sms/messages"

req = urllib2.Request(url,headers=headers,data=json.dumps(smsdata))
msg = urllib2.urlopen(req)
