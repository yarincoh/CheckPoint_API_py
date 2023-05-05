import requests, json

ip_addr = input('Please enter the IP of the Management: ')

port = input('Please enter the port of the Management: ')

command = 'test-sic-status'

json_payload = { "name" : "one" }

user = 'admin'
password = 'zubur1'


def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ip_addr + ':' + port + '/web_api/' + 'test-sic-status'
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers)
    return r.json()


def login(user,password):
    payload = {'user':user, 'password' : password}
    response = api_call(ip_addr, port, json_payload, 'sid', '')
    return response["sid"]

sid = login(user,password)
print("session id: " + sid)

new_host_data = {'name':'test-new', 'ip-address':'172.30.93.29'}
new_host_result = api_call(ip_addr, port, command, json_payload, sid)
print(json.dumps(new_host_result))

publish_result = api_call(ip_addr, port,"publish", {},sid)
print("publish result: " + json.dumps(publish_result))

logout_result = api_call(ip_addr, port,"logout", {},sid)
print("logout result: " + json.dumps(logout_result))