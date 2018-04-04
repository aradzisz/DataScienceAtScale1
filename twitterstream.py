import chardet
import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "8qP7e0CR5tRcFgcxiR4Cbm8dC"
api_secret = "FdrsD5epA2apce6v17utZMJEZbFkU7DNrB67FJYotumV2smiwI"
access_token_key = "766506188-uSe8NHzkISo71QgVKktUtmPEcuAUhvKJA3aMFhLL"
access_token_secret = "inIO1agGNAUPW97TgAp3YKOGDlz6IGml2NT8DZMdd4AJX"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

def fetchsamples3():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  url_search = "https://api.twitter.com/1.1/search/tweets.json?q=warsaw"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
      line_encoded = str(line, encoding='utf-8')
      printline_encoded.strip()
            

def fetchsamples2():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  url_search = "https://api.twitter.com/1.1/search/tweets.json?q=warsaw"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
      
      line_encoded = json.loads(line.decode('ascii'))
      print line_encoded

def fetchsamples_write():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  url_search = "https://api.twitter.com/1.1/search/tweets.json?q=warsaw"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  raw_response = response.read()
  encoding = raw_response.info().get_content_charset('utf8')
  encoded_response = json.loads(raw_response.decode(encoding))
  print "test"

  with open("output.json", "w+", encoding ='utf8') as f:
      json.dump(encoded_response, f, indent=4)

if __name__ == '__main__':
  fetchsamples()
