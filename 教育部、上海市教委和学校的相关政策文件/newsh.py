#https://edu.sh.gov.cn/xxgk2_zdgz/

#https://edu.sh.gov.cn/xxgk2_zdgz_jygzydynb/index.html
#https://edu.sh.gov.cn/xxgk2_zdgz_jygzydynb_01/index.html
#https://edu.sh.gov.cn/xxgk2_zdgz_jygzydynb_01/index_2.html

#标题，时间，发布单位，政策内容，还有分类
#思路，先获取所有页面的网址，然后遍历
from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  
from bs4 import BeautifulSoup  
import csv  
import os
#b是二级目录，m是三级页数
b_values = [f'_{i:02d}' for i in range(1, 13)]  # 生成01、02、...、12
m_values= [''] + [f'_{i}' for i in range(2,17)]  # 生成, _2, ..., _7

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
,'cookie':'Path=/; arialoadData=true; _pk_testcookie.165.24e4=1; is_uv_add_one_done=1; Path=/; _pk_ses.165.24e4=1; _pk_id.165.24e4=e2c603fb089384a6.1716295805.5.1716638001.1716637847.'}
start_url="https://edu.sh.gov.cn/xxgk2_zdgz/"
driver = webdriver.Edge()  
driver.get(start_url)  
time.sleep(2)  # 根据需要等待页面加载完成  
content = driver.page_source  
soup = BeautifulSoup(content, 'lxml')
allist = soup.find('ul',id="treeDemo_1_ul") 
littles=allist.find_all('li')
print(len(littles))
#建一个链接列表

#来源
hea="上海教育委员会"
for lit in littles[1]:
    try:
        #大类
        category="政策文件"
        #中类
        midcategory='其它工作'
        print(midcategory)
        # twourl=lit.find('a',class_='level1 ariaskiptheme').get('href')
        # print(twourl)
        #二级网页
        newtwourl='https://edu.sh.gov.cn/xxgk2_zdgz_qtgz/index.html'
        print(newtwourl)
        driver.get(newtwourl)
        time.sleep(2)
        content=driver.page_source
        soup=BeautifulSoup(content,'lxml')
        seclistss=soup.find('ul',class_='level1')
        listss=seclistss.find_all('li')
        for liit in listss:
            try:
            #小类
                smallcategory=liit.find('span',class_='node_name').get_text().strip()
                print(smallcategory)
                threeurl=liit.find('a',class_='level2 ariaskiptheme').get('href')
                #三级网页
                newthreeurl='https://edu.sh.gov.cn'+threeurl
                #urls.append(newthreeurl)
                print(newthreeurl)
        
        ##https://edu.sh.gov.cn/xxgk2_zdgz_jygzydynb_01/index_2.html
                urls=[]
                for b in b_values:
                    for m in m_values:  
                        # 构造新的URL  
                        index_of_third_underscore = newthreeurl.find('_', newthreeurl.find('_', newthreeurl.find('_') + 1) + 1)  
                        if index_of_third_underscore != -1:  
                            # 找到第一个"_"之后，我们再找后面的数字，但在这个例子中，我们假设"_0"之前的部分总是我们想要的  
                            # 所以我们只需要找到第一个"_"并切片  
                            result = newthreeurl[:index_of_third_underscore]  
                            nnurl = f"{result}{b}/index{m}.html"  
                            urls.append(nnurl)
                            print(nnurl)  
                        else:  
                            # 如果没有找到"_"，这可能是一个错误的情况  
                            result = None  # 或者一个错误消息 
                for nurlm in urls:
                    try:                     
                        driver.get(nurlm)
                        time.sleep(2)
                        content=driver.page_source
                        soup=BeautifulSoup(content,'lxml')
                        #print(soup)
                        newslls=soup.find('ul',id='listContent')
                        news=newslls.find_all('li')
                        print(len(news))
                        for new in news:
                            try:
                                #发布时间
                                release_time=new.find('span',class_='listTime').get_text()
                                print(release_time)
                                #进入内容（内容链接）
                                uuurl=new.find('a').get('href')
                                uuuurl='https://edu.sh.gov.cn'+uuurl
                                print(uuuurl)
                                driver.get(uuuurl)
                                time.sleep(1)
                                content=driver.page_source
                                soup=BeautifulSoup(content,'lxml')
                                #标题
                                title=soup.find('div',id='ivs_title').find('span').get_text().strip()
                                #print(title)
                                #发布单位   
                                try:
                                    release_unit=soup.find('div',id='ivs_content').find_all('p')[0].get_text().strip()    
                                except:
                                    release_unit="看标题"
                                #print(release_unit)
                                #政策标题及链接 
                                policy_content="" 
                                try:
                                    policy_title=soup.find('div',id='ivs_wszqyj').find('a').get_text().strip()
                                    policy_cont=soup.find('div',id='ivs_wszqyj').find('a').get('href')
                                    policy_content=policy_title+"文档链接为："+"https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fedu.sh.gov.cn"+policy_cont
                                    #print(policy_title)
                                    #print(policy_content)
                                except:
                                    policy_contents=soup.find('div',id="ivs_content").find_all('p')
                                    for p in policy_contents:
                                        policy_content += str(p.get_text(strip=True)) + "\n"  # 使用strip=True在get_text()中直接去除前后的空白，并添加换行符  
                                # print(policy_content)
             
                                # 列的名称，即表格的表头  
                                header = ["文件来源","大类","中类","小类" ,"发布时间", "标题","内容链接", "发布单位", "政策内容"]  
                                listt = [hea,category, midcategory, smallcategory,release_time, title, uuuurl, release_unit,policy_content]  
                                
                                if not os.path.exists("教育相关政策文件信息.csv") or os.path.getsize("教育相关政策文件信息.csv") == 0:  
                                    # 文件不存在或为空，写入表头  
                                    with open("教育相关政策文件信息.csv", "w", newline='', encoding="utf-8-sig") as f:  
                                        write = csv.writer(f)  
                                        write.writerow(header)
                                # 写入CSV文件，包括表头（如果文件不存在或为空）  
                                with open("教育相关政策文件信息.csv", "a+",newline='',encoding="utf-8-sig") as f:  
                                    write=csv.writer(f)
                                    write.writerow(listt)   
                                
                            except AttributeError as e:  
                                print(f"AttributeError occurred: {e}")  
                            except Exception as e:  
                                # 其他类型的异常  
                                print(f"An unexpected error occurred: {e}")
                    except :  
                        pass
            except AttributeError as e:
                with open("second_错误链接.txt", "a", encoding="utf-8") as f:
                    f.write(newthreeurl + "\n")  
        # 当find方法返回None时，尝试访问其属性或方法会抛出AttributeError  
                print(f"AttributeError occurred: {e}")  
            except Exception as e:  
                # 其他类型的异常  
                print(f"An unexpected error occurred: {e}")      
                
    except Exception as e:
        print(e)
driver.quit()        



