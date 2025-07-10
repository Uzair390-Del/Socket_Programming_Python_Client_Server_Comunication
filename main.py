# existing 4 http packages hhtp client ,server,cookies ,cookies jar
# An HTTP client is used to send HTTP requests (like GET, POST, PUT, DELETE) to a server and receive responses.
# An HTTP server listens for incoming HTTP requests and sends back responses.
# it is for get method 
import http.client
import json

con_obj=http.client.HTTPConnection("www.httpbin.org")
# con_obj.request("GET","/")
# response= con_obj.getresponse()
# print('status: {}'.format(response.seekable))
# headers_list=response.getheaders()
# print("headers: {}".format(headers_list))
#post
header_list={'Content-type:': 'apllication/json'}
post_text={'text':'Hello worlds'}
json_data=json.dumps(post_text)
con_obj.request('POST','/post',json_data,header_list)
response=con_obj.getresponse()
print(response.read().decode())
con_obj.close()


# HTTP SERVER AND SHARE FILE ON THE NETWORK
#python -m http.server 5000 or greater than 1024