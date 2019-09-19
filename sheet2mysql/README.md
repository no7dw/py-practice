# sync google sheet to MySQL

### 步骤

#### 配置goole drive api：
  - 申请 google drive api manager ，enable 之
    [link](https://developers.google.com/drive/api/v3/quickstart/python)
  - 下载credentials.json
  - 根据你的spreadID 到sheet2mysql，填写变量
  - 根据你的 content_range 到sheet2mysql，填写变量

#### 配置 MySQL 连接
  - 根据你的MySQL 配置 config.py

#### 配置MySQL create Table ，如果你是第一次 (日后 TODO 可以自动根据header 自动craete table)
  - ready go `python sheet2mysql.py`

####  备注 
https://docs.google.com/spreadsheets/d/1HBAB-O1x6QtLcLfrQtWguIbW1MSd72vv94UsSOitN3c/edit#gid=0

spreadID 是 url /d/{spreadID} --  1HBAB-O1x6QtLcLfrQtWguIbW1MSd72vv94UsSOitN3c

ref docs: 
 - https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/get
 - https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get