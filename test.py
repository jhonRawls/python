import urllib.request
userId=[1143718680]
response=urllib.request.urlopen('https://pan.baidu.com/share/home?uk=1143718680&view=follow')
print(response.read().decode('UTF-8'))
#/pcloud/friendpage?type=follow&uk=1143718680&self=0