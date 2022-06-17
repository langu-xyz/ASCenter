![ASCenter](https://socialify.git.ci/langu-xyz/ASCenter/image?description=1&language=1&name=1&owner=1&theme=Light)

## Introduction

ASCenter是EASM中的攻击面和资产管理中心，本次开源将原来的SpringMVC通过Django重写，Django-Admin天然适合开发资产管理类平台，可以快速简单的实现数据CURD操作和各类API。
它用于存储各个工具产出的数据，包括基本资产、攻击面和流量日志，然后这些数据可以用于其它工具的消费，例如越权扫描器。

## Features

1. 快速构建、修改models，满足个性化需求
2. 操作简单，可维护性高
3. models经过长时间的个人使用验证
4. 支持大型数据(流量日志)的存储和消费

## Usage

```
pip3 install django
pip3 install djangorestframework
```
```
python3 manage.py runserver
```
```
http://127.0.0.1:8000/admin/
Username:django
Password:ascenter
```

![image](https://user-images.githubusercontent.com/12745454/174252775-dad31a02-ae89-4d2f-a1d8-faf8fd147226.png)


## APIs

http://127.0.0.1:8000/api/docs/

![image](https://user-images.githubusercontent.com/12745454/174252264-a3eaf949-8f17-43f9-8718-07a5a579b9c3.png)


## Workflow

<img width="848" alt="image" src="https://user-images.githubusercontent.com/12745454/174217762-453551fc-692f-4ebe-a129-075927bf9008.png">


Enjoy your hacking life.
