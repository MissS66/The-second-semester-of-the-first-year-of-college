from selenium import webdriver  
from selenium.webdriver.common.by import By  
import time  
from bs4 import BeautifulSoup  
import csv  
import os
# https://www.maiche.com/rank/hot/p2.html
#https://www.maiche.com/rank/sale/b11d202404.html
# 标题、发布时间、点赞量、收藏量（前500个）  
headers = {  
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',  
    # 注意：cookie可能过期或不适用于自动化脚本，因此这里可能不需要它  
    # 'cookie': '...'  
}  
# 定义需要查询的月份列表  
# months = ['202404', '202403', '202402','202401','202312']  
#b_values = [f'b2{i}' for i in range(1, 8)]  # 生成b11, b12, ..., b17
i_values = [str(i) for i in range(1, 5)]  # 将数字转换为字符串，因为URL中可能需要字符串  
 
# 使用列表推导来生成URL列表  
# urls = [f"https://www.maiche.com/rank/sale/{b}d{month}p{i}.html" for b in b_values for month in months for i in i_values]  
 
# urlss = ["https://www.maiche.com/rank/sale/b1{i}d{month}.html".format(i) for i in range(1, 7)]  
  
urls = []  
#for b in b_values:  
    # for month in months: 
for i in i_values: 
        url = f"https://www.maiche.com/rank/repute/b3p{i}.html"  
        urls.append(url)  
# 创建webdriver实例（在循环外）  
driver = webdriver.Edge()  
  
try:  
    for url in urls:
        driver.get(url)  
        time.sleep(1)  # 根据需要等待页面加载完成  
        # driver.maximize_window()  # 这行代码可能不是必要的，取决于需求  
        # for i in range(1, 5):  
        content = driver.page_source  
        #print(content)  
        soup = BeautifulSoup(content, 'lxml')  
        alist = soup.find(class_="list-content") 
        # print(alist) 
        news=alist.find_all('li', class_='cl')  
        #print(len(news))  
        for new in news:       
            try:
                    #时间
                    # cartime=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[1]/div[3]').text.strip()  
                    cartime='2024年4月'
                    #print(cartime)  
                    #车型
                    cartype=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[1]/h1').text.strip()  
                    #cartype=new.find('h1', class_='fl').get_text(strip=True, separator=' ')
                    #print(cartype)  
                    # 排名  
                    carrank = new.find('div', class_='thubm fl').find('span', class_='n').get_text().strip()  
                    #print(carrank)  

                    # 车名  
                    carname = new.find('div',class_='info fl').find('h3').find('a',target='_blank').get_text().strip() 
                    #carname=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/h3/a').text.strip()  
                    #print(carname)  
                    
                    # 厂商指导价  
                    price_range = new.find('div',class_='info fl').find('p').find('a', target='_blank').find('strong').get_text().strip()  
                    #price_range=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/p/a/strong').text.strip()  
                    #print(price_range)  
                    #车辆价格降幅排行
                    # down_volume = new.find('div',class_='item fr price').find('span', class_='item-num').get_text().strip()  
                    #口碑
                    comment_volume = new.find('div',class_='item fr repute').find('span', class_='item-score').get_text().strip()  
                    # 全国月关注度 
                    # attention_volume = new.find('div',class_='item fr hot').find('span', class_='item-num').get_text().strip()  
                    # 销售量
                    #sales_volume = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[3]/div/div[2]/span[1]').text.strip()  
                    #print(sales_volume)  
                    # print(f"排名：{carrank}，车名：{carname}，厂商指导价：{price_range}，销量：{sales_volume}")
                    #质保
                    quality_guarantee=new.find('p',class_='b fl').find_all('span', class_='el')[0].get_text().strip()  
                    #quality_guarantee=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[1]/span[1]').text.strip()  
                    #print(quality_guarantee)  
                    #环保标准
                    environment_standard=new.find('p',class_='b fl').find_all('span', class_='el')[1].get_text().strip()  
                    #environment_standard=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[1]/span[2]').text.strip()
                    #print(environment_standard)  
                    #油耗
                    soil_consumption=new.find('p',class_='y fl').find_all('span', class_='el')[0].get_text().strip()  
                    #soil_consumption=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[2]/span[1]').text.strip()
                    #print(soil_consumption) 
                    #燃油标号
                    fuel_label=new.find('p',class_='y fl').find_all('span', class_='el')[1].get_text().strip()  
                    #fuel_label=driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/div/div[2]/ul/li[1]/div[2]/div/p[2]/span[2]').text.strip()
                    #print(fuel_label)  
                    
                    print(cartime,cartype,carname,price_range,comment_volume,quality_guarantee,environment_standard,soil_consumption,fuel_label)
                    # 列的名称，即表格的表头  
                    header = ['时间', '车型', '车名', '厂商指导价格范围', '评分', '质保', '环保标准', '油耗', '燃油标号']  
                    listt = [cartime, cartype, carname, price_range, comment_volume, quality_guarantee, environment_standard, soil_consumption, fuel_label]  

                    if not os.path.exists("车辆口碑排行信息.csv") or os.path.getsize("车辆口碑排行信息.csv") == 0:  
                        # 文件不存在或为空，写入表头  
                        with open("车辆口碑排行信息.csv", "w", newline='', encoding="utf-8-sig") as f:  
                            write = csv.writer(f)  
                            write.writerow(header)
                    # 写入CSV文件，包括表头（如果文件不存在或为空）  
                    with open("车辆口碑排行信息.csv", "a+",newline='',encoding="utf-8-sig") as f:  
                        write=csv.writer(f)
                        write.writerow(listt)   
                    
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