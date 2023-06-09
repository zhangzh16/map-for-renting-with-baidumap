#import bs4
from bs4 import BeautifulSoup
import os
from openpyxl import Workbook

lists = []
names = []

def make_filename():
    path = './0602/'
    files = os.listdir(path)
    #num = int((len(files)-1) / 2)
#    print(num)
    for x in range(len(files)):
        filename = path+'贝壳' + str(x+1).rjust(3,'0') + '.html'
        names.append(filename)
    return(names)

def get_some_message(filename):#获取信息的主要部分
    file = open(filename,'r',encoding = 'utf-8')
    soup = BeautifulSoup(file , "html.parser")

    #print(soup.get_text())

    m = soup.find_all('div')
    #print(m)

    for x in m:
        house = []
        try:
            if 'BJ' not in x['data-house_code']:
                continue
            #这里的if会过滤掉公寓选项，因为公寓的house_code不含有BJ
            house.append(x['data-house_code'])#根tag
            #print(x.div.p.get_text().replace(' ',''))
            #print(x.div.children)
            #house.append(x['data-house_code'])

            # title = x.find('p', class_='content__list--item--title').a.get_text().strip()
            # house.append(title[0:2])
            # house.append(title[3:])

            des = x.find('p', class_='content__list--item--des')
            # area = des.i.next_sibling.strip()
            # house.append(area)

            district = des.a.get_text()
            house.append(district)

            sub_district = des.find_all('a')[1].get_text()
            house.append(sub_district)
            
            subsub_district = des.find_all('a')[2].get_text()
            house.append(subsub_district)

            size = des.find('i', class_='').next_sibling.strip()
            house.append(size)
            
            orientation = des.find('i', class_='').next_sibling.next_sibling.next_sibling.strip()
            house.append(orientation)

            room_info = des.find('i', class_='').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strip()
            house.append(room_info)
            
            room_floor = des.find('span', class_='hide').get_text().strip().replace('/\n','').replace(' ','')
            house.append(room_floor)

            price = x.find('span', class_='content__list--item-price').em.get_text().strip()
            house.append(price)
            
            time = x.find('p', class_='content__list--item--brand oneline').find('span', class_='content__list--item--time oneline').get_text().strip()
            house.append(time)
            
            useformap='-'.join(map(str, [district,sub_district,subsub_district]))
            house.append(useformap)
            
            tags = x.find('p', class_='content__list--item--bottom oneline').find_all('i')
            tag_info = [tag.get_text().strip() for tag in tags]
            tag_info_fin = '-'.join(map(str, tag_info))
            house.append(tag_info_fin)

            brand = x.find('p', class_='content__list--item--brand oneline').span.get_text().strip()
            house.append(brand)
            
            
            # for child in x.div.children:#child tag
            #     child_text = child.get_text().replace('\n','').replace(' ','')
            #     if child_text != '':
            #         house.append(child_text)
            #     else:
            #         pass
            #print(' ')
        except:
            pass

        if house != []:
            lists.append(house)
        else:
            pass

    return(lists)

make_filename()
for name in names:
    get_some_message(name)
#print(lists)

for house in lists:
    print(house)

# 定义写入文件的路径
file_path = './0602output.txt'

# 打开文件，以写入模式写入内容
with open(file_path, 'w') as f:
    # 遍历列表A中的每一个元素
    for item in lists:
        # 将列表中的每个元素转为字符串，并用空格连接
        line = ' '.join(map(str, item))
        # 写入文件
        f.write(line + '\n')

output_file="./0602output.xlsx"
# 如果文件已经存在，先删除文件
if os.path.exists(output_file):
    os.remove(output_file)
# 创建一个工作簿
workbook = Workbook()

# 获取工作簿的活动表单
sheet = workbook.active
# 定义列名
column_names = ['房源id', '行政区', '片区', '小区',  '面积', '朝向', '房型', '楼层', '价格', 
                '维护时间', '地图搜索用','标签', '来源']

# 写入列名到第一行
sheet.append(column_names)
# 遍历列表A中的每一个元素
for row in lists:
    # 将每个元素作为一行数据写入Excel文件中
    sheet.append(row)

# 保存Excel文件
workbook.save(output_file)