import requests
import json,os
from openpyxl import Workbook
#url = 'https://api.map.baidu.com/geocoding/v3/?address='+'北京市海淀区上地十街10号'+'&output=json&ak=7DRDehceFn0wg2Q4Z4E8f3QeADRqDrQQ&callback=showLocation //GET请求'

def get_location(url,sheet,line):
    resp = requests.get(url)

    m = resp.text
    m = json.loads(m)
    #print(type(m))
    address=line
    location = m['result']['location']
    lng=location['lng']
    lat=location['lat']
    comprehension = m['result']['comprehension']
    # confidence=m['result']['confidence']
    # level=m['result']['level']
    # precise=m['result']['precise']
    
    #tup=[address,lng,lat,confidence,comprehension,level,precise]
    tup=[address,lng,lat,comprehension]

    # 将每个元素作为一行数据写入Excel文件中
    sheet.append(tup)
    print(tup)

#{"status":0,"result":{"location":{"lng":116.3076223267197,"lat":40.05682848596073},"precise":1,"confidence":80,"comprehension":100,"level":"门址"}}

#get_location(url)
output_file="location.xlsx"
# 如果文件已经存在，先删除文件
if os.path.exists(output_file):
    os.remove(output_file)
# 创建一个工作簿
workbook = Workbook()

# 获取工作簿的活动表单
sheet = workbook.active
# 定义列名
# column_names = ['address', 'lng', 'lat', 'confidence', 'comprehension', 'level', 'precise']
column_names = ['address', 'lng', 'lat', 'comprehension']

# 写入列名到第一行
sheet.append(column_names)

f = open('bzdz.txt',encoding = 'UTF-8', errors = 'ignore')
for line in f:
    #txt.append(line.strip())
    tag=line.strip().split('-')[2]
    line='北京市'+''.join(line.strip().split('-'))
    #print(line)
    url = 'https://api.map.baidu.com/geocoding/v3/?address='+line+'&output=json&ak=9Et5IvzoNpoM5Ne5qmSpW7VH3YdFGal5&callback=showLocation //GET请求'
    get_location(url,sheet,tag)

# 保存Excel文件
workbook.save(output_file)


