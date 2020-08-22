#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import json
import urllib.request
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109 import DeleteSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import AddDomainRecordRequest


# 获取公网ip
def get_public_ip():
    res = urllib.request.urlopen('https://ipv4.jsonip.com/')
    content = res.read()
    print(str(content, 'utf-8'))
    content = json.loads(str(content, 'utf-8'))
    return content['ip']


# 新增解析记录
def add_domain_record():
    req = AddDomainRecordRequest.AddDomainRecordRequest()
    req.set_DomainName(domain)
    req.set_RR(subDomain)
    req.set_Type('A')
    req.set_Value(publicIp)
    print(json.dumps(req.get_query_params()))
    res = client.do_action_with_exception(req)
    print(str(res, 'utf-8'))


# 修改解析记录
def update_domain_record(record_id):
    req = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    req.set_RecordId(record_id)
    req.set_RR(subDomain)
    req.set_Type('A')
    req.set_Value(publicIp)
    print(json.dumps(req.get_query_params()))
    res = client.do_action_with_exception(req)
    print(str(res, 'utf-8'))


# 删除解析记录
def delete_domain_record():
    req = DeleteSubDomainRecordsRequest.DeleteSubDomainRecordsRequest()
    req.set_DomainName(domain)
    req.set_RR(subDomain)
    req.set_Type('A')
    print(json.dumps(req.get_query_params()))
    res = client.do_action_with_exception(req)
    print(str(res, 'utf-8'))


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " DDNS")

config = json.load(open('config.json'))

# 创建AcsClient实例
client = AcsClient(
    # "<your-access-key-id>",
    config['access-key-id'],
    # "<your-access-key-secret>",
    config['access-key-secret'],
    # "<your-region-id>"
    config['region-id']
)
domain = config['ddns-domain']
subDomain = config['ddns-sub-domain']
# 获取公网ip
print('Get Public IP Address')
publicIp = get_public_ip()
print('Get DDNS Records')
# 创建request，并设置参数
request = DescribeSubDomainRecordsRequest.DescribeSubDomainRecordsRequest()
request.set_SubDomain(subDomain + "." + domain)
# 发起API请求并显示返回值
print(json.dumps(request.get_query_params()))
response = client.do_action_with_exception(request)
print(str(response, 'utf-8'))
response = json.loads(str(response, 'utf-8'))
if response['TotalCount'] > 0:
    if response['TotalCount'] != 1:
        print('Delete DDNS Records')
        delete_domain_record()
        print('Add DDNS Record')
        add_domain_record()
    else:
        if response['DomainRecords']['Record'][0]['Value'] != publicIp:
            print('Update DDNS Records')
            update_domain_record(response['DomainRecords']['Record'][0]['RecordId'])
        else:
            print("Not Modified")
else:
    print('Add DDNS Record')
    add_domain_record()
print('')
