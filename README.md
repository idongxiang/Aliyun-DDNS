### Python3

##### 1.安装阿里云SDK核心库
```
pip install aliyun-python-sdk-core
```
##### 2.安装阿里云SDK alidns库
```
pip install aliyun-python-sdk-alidns
```
##### 3.配置阿里云访问凭据和域名
```
{
  "access-key-id": "<your-access-key-id>",
  "access-key-secret": "<your-access-key-secret>",
  "your-region-id": "<your-region-id>",
  "ddns-domain": "<your-ddns-domain>",
  "ddns-sub-domain": "<your-ddns-sub-domain>"
}
```
##### 4.执行
```
# chmod +x DDNS.py

# ./DDNS.py
```
##### 4.Cron定时执行