# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:44:27 2023

@author: admin
"""


import requests
# import os
from bs4 import BeautifulSoup

def save_webpage(page_content, page_number):
    filename = f"0602/贝壳{str(page_number).zfill(3)}.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(page_content)
    print(f"保存网页 {filename} 完成")

def save_all_pages():
    base_url = "https://bj.lianjia.com/zufang/rt200600000001l0l1erp6000/"
    #params = {}

    # 发送请求获取第一页网页内容
    response = requests.get(base_url)
    page_content = response.text
    save_webpage(page_content, 1)

    soup = BeautifulSoup(page_content, "html.parser")
    # 获取总页数
    total_pages = int(soup.find("div", class_="content__pg")["data-totalpage"])
    div_content_pg = soup.find('div', class_='content__pg')
    # 保存剩余页面的内容
    for page_number in range(2, total_pages + 1):
        # 构建下一页的URL
        #next_page_url = base_url + div_content_pg.find('a', class_='next')['href']
        next_page_url = "https://bj.lianjia.com"+div_content_pg['data-url'].replace('{page}',str(page_number))
        
        # 发起下一页的请求
        response = requests.get(next_page_url)
        page_content = response.text
        save_webpage(page_content, page_number)
    
        # 更新soup和div_content_pg以获取下一页的URL
        soup = BeautifulSoup(page_content, 'html.parser')
        div_content_pg = soup.find('div', class_='content__pg')

    print("所有网页保存完成")

# 调用函数保存所有页面
save_all_pages()
