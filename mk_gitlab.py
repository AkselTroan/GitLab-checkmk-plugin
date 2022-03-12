import requests, sys, json


__version__ = "2.0.0p20"

ip = "localhost"
port = "443"
server = ip + ":" + port


health = requests.get(server + "/-/health")
readiness = requests.get(server + "/-/readiness?all=1")
liveness = requests.get(server + "/-/liveness")

if health.text == "GitLab OK":
    sys.stdout.write('0 "Health" - Health passed')
else:
    sys.stdout.write('2 "Health" - Health failed')


read = json.loads(readiness.text)
live = json.loads(liveness.text)


if read['status'] == "ok":
    sys.stdout.write('0 "Readiness" - Readiness passed')
else:
    sys.stdout.write('2 "Readiness" - Readiness failed')


if live['status'] == "ok":
    sys.stdout.write('0 Liveness" - Liveness passed')
else:
    sys.stdout.write('2 "Liveness" - Liveness Failed')
