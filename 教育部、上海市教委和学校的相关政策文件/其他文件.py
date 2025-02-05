#其他部门
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/index_1.html（1-18）
#中央文件：
# http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/
# http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/index_1.html
#教育部：#http://www.moe.gov.cn/was5/web/search?channelid=239993&page=1  （1-846）
#标题，时间，发布单位，政策内容，还有分类

#共371条，少了四条：
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/srcsite/A08/s7056/201607/t20160707_271098.html
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/srcsite/A12/moe_1407/s3008/200705/t20070517_76339.html
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/srcsite/A13/moe_772/200411/t20041117_80567.html
#http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/s78/A13/sks_left/s6387/moe_772/tnull_22302.html


from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  
from bs4 import BeautifulSoup  
import csv  
import os
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
,'cookie':'wdcid=4fd3bfb4969fb5b7; WT_USER_ID=2-25fd7aa4da09cfb; wdses=26752c3ed8d2c8f2; wdlast=1716442517'}
# start_url="http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/"
# 定义需要查询的页码列表  
#b_values = [f'{i}' for i in range(1, 19)]  # 生成b1, b2, ..., b18

urls = ["http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/"]  
# for b in b_values:  
#     url = f"http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/index_{b}.html"  
#     urls.append(url)  
# 创建webdriver实例（在循环外）  
driver = webdriver.Edge()  
try:  
    for url in urls:
        print("正在爬取：" + url)
        driver.get(url)  
        time.sleep(1)  # 根据需要等待页面加载完成  
        # driver.maximize_window()  # 这行代码可能不是必要的，取决于需求  
        content = driver.page_source  
        #print(content)  
        soup = BeautifulSoup(content, 'lxml')  
        alist = soup.find('ul',id="list") 
        # print(alist) 
        news=alist.find_all('li')  
        #print(len(news))  
        #类别
        category=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div[3]/div[1]/h2').text.strip()
        #print(category)

        for new in news:       
            try:
#时间
                release_time=new.find('span').get_text().strip()  
                #print(release_time)
#进入二级链接http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/202402/t20240229_1117317.html
                urlss=new.find('a').get('href')
                newurl='http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/'+urlss.lstrip('./')
                #print(newurl)
                driver.get(newurl)
                time.sleep(1)
                content=driver.page_source
                soup=BeautifulSoup(content,'lxml')
#标题
                title=soup.find('div',class_='moe-detail-box').find('h1').get_text().strip()
                #print(title)
#发布单位       
                try:
                    release_unit=soup.find('div',class_='TRS_Editor').find('p').get_text().strip()
                except:
                    try:
                        release_unit=soup.find('p',id='moe-policy-wenhao').get_text().strip()
                    except:
                        try:
                            release_unit=soup.find('p',align='right').get_text().strip()
                        except:
                            release_unit="未说明"
#政策内容       
                policy_content = ""  
                try:
                    content=soup.find('div',class_='TRS_Editor').find_all('p')
                except:
                    content=soup.find('div',class_='moe-detail-box').find_all('p')
                    # 初始化一个空字符串来存储所有<p>标签的文本内容  
                    
                for p in content:
                    policy_content += p.get_text(strip=True) + "\n"  # 使用strip=True在get_text()中直接去除前后的空白，并添加换行符  
                    # print(policy_content)
#文件来源
                hea="中华人民共和国教育部"
#写入CSV文件  
                #print(hea,category,"","",release_time,title,release_unit,policy_content)
                # 列的名称，即表格的表头  
                header = ["文件来源","大类","中类","小类" ,"发布时间", "标题","内容链接", "发布单位", "政策内容"]  
                listt = [hea,category, "", "",release_time, title, newurl, release_unit,policy_content]  

                if not os.path.exists("教育相关政策文件信息.csv") or os.path.getsize("教育相关政策文件信息.csv") == 0:  
                    # 文件不存在或为空，写入表头  
                    with open("教育相关政策文件信息.csv", "w", newline='', encoding="utf-8-sig") as f:  
                        write = csv.writer(f)  
                        write.writerow(header)
                # 写入CSV文件，包括表头（如果文件不存在或为空）  
                with open("教育相关政策文件信息.csv", "a+",newline='',encoding="utf-8-sig") as f:  
                    write=csv.writer(f)
                    write.writerow(listt)   
            except Exception as e:
                    print(f"出错了: {e} or None URL")
                    with open("错误链接.txt", "a", encoding="utf-8") as f:
                        f.write(newurl + "\n")
                    continue
                    
except Exception as e:  
                    print(f"出错了: {e} or None URL") 
        # try:
        #     next_page_button = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[3]/div/ul/li[4]/a')  
        #     next_page_button.click()  # 点击下一页  
        #     # 这里可能还需要一个等待条件来确保新页面加载完成  
        #     sleep(1)  # 简单的等待，不推荐在生产环境中使用  
        # except NoSuchElementException:  
        #     # 如果没有找到下一页按钮，则跳出循环  
        #     break  
  
finally:  
    # 确保在循环结束后关闭webdriver实例  
    driver.quit()