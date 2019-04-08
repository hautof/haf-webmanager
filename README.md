# haf-webmanager

> haf web manager

[![Build Status](https://travis-ci.org/hautof/haf-webmanager.svg?branch=master)](https://travis-ci.org/hautof/haf-webmanager)
![PyPI](https://img.shields.io/pypi/v/hafweb.svg)
![GitHub release](https://img.shields.io/github/release/hautof/haf-webmanager.svg)

## haf

> https://github.com/tsbxmw/haf

## now have version 0.0.3 to support mysql as an api server

> apis

| id | url | description | others |
|----|----|----|----|
|1| /api/v1/main | get all tests in the db | |
|2| /api/v1/main/today | get all today test | |
|3| /api/v1/main?date_time=2019-04-08 | get the 20190408's tests | |
|4| /api/v1/suite?main_id=123 | get the main_id's suite | |
|5| /api/v1/summary?suite_id=123 | get the summary of id | |
|6| /api/v1/case?suite_id=123 | get the case of suite | |
|7| /api/v1/expect?id=123 | get the expect of id | |
|8| /api/v1/ids?id=123 | get the ids of id | |
|9| /api/v1/request?id=123 | get the request of id | |
|10| /api/v1/response?id=123 | get the response of id | |
|11| /api/v1/sqlinfo?id=123 | get the sqlinfo of id | |
|12| /api/v1/sqlinfo/checklist?id=123 | get the sqlinfo checklist of id | |
|13| /api/v1/sqlinfo/config?id=123 | get the sqlinfo config of id | |
|14| /api/v1/sqlinfo/script?id=123 | get the sqlinfo script of id | |
|15| /api/v1/case/detail?id=123 | get the detail of case id | |


## Manager of HAF based on vue & python flask

- create/edit case
- run/pasue/stop case
- generate report of case result
- dashboard of results
- results analysis
- import case (from json, xlsx, yml, py)
- export case (to json, xlsx, yml, py)
- export report
