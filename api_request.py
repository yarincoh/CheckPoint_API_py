import requests, json

Management_ip = input('Please enter IP of the Management Server: ')
Port = input('Please enter the port of the Management Server: ')

# Set the URL endpoint
url = f'https://{Management_ip}:{Port}/web_api/install-database'

user = 'admin'
password = 'zubur1'

def api_call(Management_ip, Port, install-database, json_payload, sid):
    url = 'https://' + Management_ip + ':' + Port + '/web_api/' + 'install-database'
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers)
    return r.json()

def login(user,password):
    payload = {'user':user, 'password' : password}
    response = api_call(Management_ip, 4434, 'login',payload, '')
    return response["sid"]

sid = login('my_username','secret')
print("session id: " + sid)
# Set the request headers
headers = {'Content-Type': 'application/json'}

# Set the request body
data = {}

# Send the request
response = requests.post(url, headers=headers, json=payload, verify=False)

print(response)

# Check if the request was successful
if response.status_code == 200:
    print('Database installation request sent successfully')
    publish_result = api_call('192.168.65.2', 443,"publish", {},sid)
    print("publish result: " + json.dumps(publish_result))
else:
    print('Error: Failed to send database installation request')
