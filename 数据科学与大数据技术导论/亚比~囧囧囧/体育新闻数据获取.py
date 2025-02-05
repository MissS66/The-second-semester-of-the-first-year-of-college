#https://sports.cctv.com/
#中国足球https://sports.cctv.com/football/china/
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import csv
import re
from bs4 import BeautifulSoup
#标题、发布时间、点赞量、收藏量（前500个）
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
,'cookie':'HMF_CI=0079fd9efe524f7465b251e2c2a999187f9a27f659d6ae04dd6c48c94944c86218b93387d0a6fe5da94bbd919a7f5310b6535fe63a202d67f33b5125ff113b1fef; cna=nHjOHrK4iUkCAbfDSJYkDM/S; sca=ab73def9; country_code=CN; atpsida=aa6b577e67a4a1154408d7ca_1716024552_13; HMY_JC=02a83b6cfa539b975dcfc437991e2035056375133049872564dc6d997b4498a2fe,; HOY_TR=JPZTLUFQAOKCEGNB,2435789AE6BCDF01,rdakqvxwcoyfszgt; HBB_HC=3d26c3b85db2e97a13437f31b67b1a54e21d810fee97d2352b35a2c21252e645aa0c087e02e17ec52ec74af14f1328e52d'}
start_url="https://sports.cctv.com/football/china/"
driver=webdriver.Edge()
driver.get(start_url)
driver.encoding='utf-8'
time.sleep(4)  
driver.maximize_window()
for x in range(25):
    js=f'window.scrollTo({10000*x}, {10000*(x+1)});'
# 使用execute_script方法执行JavaScript代码来实现鼠标滚动
    driver.execute_script(js) # 向下滚动 10000 像素
    time.sleep(2)
content=driver.page_source
#print(content)
soup=BeautifulSoup(content,'lxml')
#print(soup)
alist=soup.find(class_="bot_list")
news=alist.find_all(style='display: list-item;')
#print(news)
for new in news:
  try:
    newurl=new.find(class_="cont").find(class_="title").find('a').get("href")
    #print(newurl)
    url2=newurl
    r2=requests.get(url2,headers=headers)
    r2.encoding='utf-8'
    soup2=BeautifulSoup(r2.text,"html.parser")
#标题
    title=soup2.find(class_="title_area").get_text() .strip()
    #print(title)

#发布报社及时间
    patterns = {
                "reporter": r'/来源：(.*?)\</',
                "atimes": r'/\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}/'
            }
    reporter_matches = re.findall(patterns['reporter'], content)
    atimes_matches = re.findall(patterns['atimes'], content)

# 从匹配结果列表中取出单个结果
    report = reporter_matches[0] if reporter_matches else "未知发布报社"
    atime = atimes_matches[0] if atimes_matches else "未知发布时间" 
    # atime=soup2.find('div',class_="info1").get_text().strip()
    #print(atime)

#正文
    contents=soup2.find(class_="content_area")
    content=contents.find_all('p')
    for p in content:
        # print(p.get_text().strip())
        content=p.get_text().strip() + content
    #print(content)

#编辑
    editors=soup2.find('div',class_="zebian")
    editor_span=editors.find('span',text=lambda text: '编辑' in text).get_text().strip()
    if editor_span:  
        editor_name = editor_span.get_text(strip=True).split('：')[1]  # 格式是“编辑：姓名”  
        # print(f"编辑：{editor_name}") 
    
#责任主编
    zd=soup2.find('div',class_="zd_area")
    zd_name=zd.find('span',id='zb').get_text().strip().split('：')[1]
    #print(zd_name)

#点赞量
    agree=soup2.find('div', class_='like', id='zanNum')
    text_nodes = agree.contents 
    for node in text_nodes:  
        if isinstance(node, str) and node.strip().isdigit():  # 检查节点是否为字符串且为数字  
            zan = node.strip()  # 去掉前后空白字符  
            break  # 找到后退出循环  
    else:  
        zan = None  # 如果没有找到数字，则设置为None  
    
    # 输出结果  
    # if number:  
    #     print(f"找到的数字是：{number}")  
    # else:  
    #     print("没有找到数字")
#相关标签
    signs=soup2.find('span',class_="content_area")
    keywords = []  
  
    for li in signs.find_all('li'):  
        a_tag = li.find('a')  
        if a_tag:  
            href = a_tag['href']  
            match = re.search(r'qtext=([^&]+)', href)  
            if match:  
                keywords.append(match.group(1))  
        time.sleep(1)
        #print(keywords)
#相关标签的链接
    links = []  
    for a_tag in signs.find_all('a', href=True):  
        links.append(a_tag['href'])  
    #print(links)
  except:
    try:
        newurl=new.find(class_="cont").find(class_="listZd").find('a').get("href")
        #print(newurl)
        url2=newurl
        r2=requests.get(url2,headers=headers)
        r2.encoding='utf-8'
        soup2=BeautifulSoup(r2.text,"html.parser")
    #标题
        title=soup2.find(class_="title_area").get_text() .strip()
        #print(title)

    #发布报社及时间
        patterns = {
                    "reporter": r'/来源：(.*?)\</',
                    "atimes": r'/\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}/'
                }
        reporter_matches = re.findall(patterns['reporter'], content)
        atimes_matches = re.findall(patterns['atimes'], content)

    # 从匹配结果列表中取出单个结果
        report = reporter_matches[0] if reporter_matches else "未知发布报社"
        atime = atimes_matches[0] if atimes_matches else "未知发布时间" 
        # atime=soup2.find('div',class_="info1").get_text().strip()
        #print(atime)

    #正文
        contents=soup2.find(class_="content_area").get_text().strip()
        content=contents.find_all('p')
        for p in content:
            # print(p.get_text().strip())
            content=p.get_text().strip() + content
        #print(content)

    #编辑
        editors=soup2.find('div',class_="zebian")
        editor_span=editors.find('span',text=lambda text: '编辑' in text).get_text().strip()
        if editor_span:  
            editor_name = editor_span.get_text(strip=True).split('：')[1]  # 格式是“编辑：姓名”  
            # print(f"编辑：{editor_name}") 
        
    #责任主编
        zd=soup2.find('div',class_="zd_area")
        zd_name=zd.find('span',id='zb').get_text().strip().split('：')[1]
        #print(zd_name)

    #点赞量
        agree=soup2.find('div', class_='like', id='zanNum')
        text_nodes = agree.contents 
        for node in text_nodes:  
            if isinstance(node, str) and node.strip().isdigit():  # 检查节点是否为字符串且为数字  
                zan = node.strip()  # 去掉前后空白字符  
                break  # 找到后退出循环  
        else:  
            zan = None  # 如果没有找到数字，则设置为None  
        
        # 输出结果  
        # if number:  
        #     print(f"找到的数字是：{number}")  
        # else:  
        #     print("没有找到数字")
    #相关标签
        signs=soup2.find('span',class_="content_area")
        keywords = []  
    
        for li in signs.find_all('li'):  
            a_tag = li.find('a')  
            if a_tag:  
                href = a_tag['href']  
                match = re.search(r'qtext=([^&]+)', href)  
                if match:  
                    keywords.append(match.group(1))  
            time.sleep(1)
            #print(keywords)
    #相关标签的链接
        links = []  
        for a_tag in signs.find_all('a', href=True):  
            links.append(a_tag['href'])  
        #print(links)
    except:
        continue
  print(title,atime,agree,shoucang)
  listt=[title,atime,agree,shoucang]
  with open("Bzhano2~.csv","a+",newline='',encoding="utf-8-sig") as f:
    write=csv.writer(f)
    write.writerow(listt)
print("爬取完毕！")
driver.quit()