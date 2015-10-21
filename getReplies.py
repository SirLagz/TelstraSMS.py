#!/usr/bin/python
import urllib
import urllib2
import json
import datetime
import sys

smsMessageId = sys.argv[1]
key="YOURKEY"
secret="YOURSECRET"
authfile = '/tmp/telstraauth'
now = datetime.datetime.today()


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


headers = { 'Authorization':'Bearer '+str(authtoken) }
url = "https://api.telstra.com/v1/sms/messages/"+smsMessageId+"/response"

req = urllib2.Request(url,headers=headers)
msg = urllib2.urlopen(req)

print msg.read()
