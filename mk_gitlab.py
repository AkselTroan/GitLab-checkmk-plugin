#!/usr/bin/env python3
import requests, sys, json


__version__ = "2.0.0p20"

server = "localhost"


health = requests.get(server + "/-/health")
readiness = requests.get(server + "/-/readiness?all=1")
liveness = requests.get(server + "/-/liveness")

if health.text == "GitLab OK":
    print('0 "GitLab Health" - Health passed')
else:
    print('2 "GitLab Health" - Health failed')


read = json.loads(readiness.text)
live = json.loads(liveness.text)


if read['status'] == "ok":
    print('0 "GitLab Readiness" - Readiness passed')
else:
    print('2 "GitLab Readiness" - Readiness failed')


if live['status'] == "ok":
    print('0 "GitLab Liveness" - Liveness passed')
else:
    print('2 "GitLab Liveness" - Liveness Failed')