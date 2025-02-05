#其他部门
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/index_1.html（1-18）
#中央文件：
# http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/
# http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/index_1.html
#教育部：#http://www.moe.gov.cn/was5/web/search?channelid=239993&page=1  （1-846）
#标题，时间，发布单位，政策内容，还有分类
from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  
from bs4 import BeautifulSoup  
import csv  
import os
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
,'cookie':'wdcid=4fd3bfb4969fb5b7; WT_USER_ID=2-25fd7aa4da09cfb; wdses=26752c3ed8d2c8f2; wdlast=1716442517'}
start_url="http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/"
# 定义需要查询的页码列表  
b_values = [f'{i}' for i in range(1, 11)]  # 生成b11, b12, ..., b17

urls = ["http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/"]  
for b in b_values:  
    url = f"http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/index_{b}.html"  
    urls.append(url)  
# 创建webdriver实例（在循环外）  
driver = webdriver.Edge()  
# 其他部分保持不变
try:
    for url in urls:
        print(f"正在爬取{url}...")
        try:
            driver.get(url)
            time.sleep(1)
            content = driver.page_source
            soup = BeautifulSoup(content, 'lxml')
            alist = soup.find('ul', id="list")
            news = alist.find_all('li')
            category = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[3]/div[1]/h2').text.strip()
            #print(category)

            for new in news:
                try:
                    release_time = new.find('span').get_text().strip()
                    urlss = new.find('a').get('href')
                    newurl = 'http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/' + urlss.lstrip('./')
                    driver.get(newurl)
                    time.sleep(1)
                    content = driver.page_source
                    soup = BeautifulSoup(content, 'lxml')
                    title = soup.find('div', class_='moe-detail-box').find('h1').get_text().strip()
                    release_unit = soup.find('div', class_='TRS_Editor').find('p').get_text().strip()
                    content = soup.find('div', class_='TRS_Editor').find_all('p')
                    policy_content = ""
                    for p in content:
                        policy_content += p.get_text(strip=True) + "\n"
                    hea = "中华人民共和国教育部"
                    #print(hea, category, "", "", release_time, title, release_unit, policy_content)
                    header = ["文件来源", "大类", "中类", "小类", "发布时间", "标题", "内容链接", "发布单位", "政策内容"]
                    listt = [hea, category, "", "", release_time, title, release_unit, newurl, policy_content]
                    if not os.path.exists("教育相关政策文件信息.csv") or os.path.getsize("教育相关政策文件信息.csv") == 0:
                        with open("教育相关政策文件信息.csv", "w", newline='', encoding="utf-8-sig") as f:
                            write = csv.writer(f)
                            write.writerow(header)
                    with open("教育相关政策文件信息.csv", "a+", newline='', encoding="utf-8-sig") as f:
                        write = csv.writer(f)
                        write.writerow(listt)
                    time.sleep(1)
                except Exception as e:
                    print(f"出错了: {e} or None URL,第{i}页")
                    with open("错误链接.txt", "a", encoding="utf-8") as f:
                        f.write(newurl + "\n")
                    continue
        except Exception as e:
            print(f"出错了: {e} or None URL")
            with open("错误链接.txt", "a", encoding="utf-8") as f:
                f.write(url + "\n")
            continue
finally:
    driver.quit()
