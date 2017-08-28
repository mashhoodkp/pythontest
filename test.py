import requests
from bs4 import BeautifulSoup
import csv
import os
page= requests.get("http://hotels.ctrip.com/hotel/taipei617#ctm_ref=hod_hp_sb_lst")
#page= requests.get("C:\Users\Melomaniac\Downloads\scrap.htm")
soup = BeautifulSoup(page.content, 'html.parser')
hot_name=[]
hot_price=[]
hot_addrs=[]
hot_value=[]
judge_no=[]
judge_score=[]
last_book=[]
promo_info=[]
#print(soup.prettify())
#print(list (soup.children))
#<span class="J_price_lowList">
name=soup.find_all('h2' ,class_="hotel_name")
address=soup.find_all('p',class_='hotel_item_htladdress')
rating=soup.find_all('span' ,class_="hotel_value")
judge=soup.find_all('span',class_='hotel_judgement')
score=soup.find_all('span',class_='total_judgement_score')
price=soup.find_all('span',class_='J_price_lowList')
lastbook=soup.find_all('p',class_='hotel_item_last_book')
promotion=soup.find_all('div',class_='promotion_info')
#web=name.find('a')
#print (web.get.("href"))
#,class_='J_price_lowList')
#for item in price:#.find_all("J_price_lowList"):
 #print(item.get("J_price_lowList"))
for item in name:
    value=item.get_text()
    hot_name.append(value.encode('utf-8'))
for item in price:
   value=item.get_text()
   hot_price.append(value.encode('utf-8'))
for item in address:
    value=item.get_text()
    hot_addrs.append(value.encode('utf-8'))
for item in rating:
    value=item.get_text()
    hot_value.append(value.encode('utf-8'))
for item in judge:
    value=item.get_text()
    judge_no.append(value.encode('utf-8'))
for item in score:
    value=item.get_text()
    judge_score.append(value.encode('utf-8'))
for item in lastbook:
    value=item.get_text()
    last_book.append(value.encode('utf-8'))
for item in promotion:
    value=item.get_text()
    promo_info.append(value.encode('utf-8'))
z=len(hot_name)
#f=open("Hotel.csv","w")
#f.truncate()
#f.close()
exp_list=[]
#final_list=[]
#for key in price:
#print(hot_name[0])
exp_list=[hot_name[0],hot_price[0],hot_addrs[0],hot_value[0],judge_no[0],judge_score[0],last_book[0],promo_info[0]]
with open ("Hotel.csv",'w') as myfile:
        wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
        wr.writerow(exp_list)
        wr.writerow("\n")
z=z-1
i=1    
while(i<z):
    exp_list=[hot_name[i],hot_price[i],hot_addrs[i],hot_value[i],judge_no[i],judge_score[i],last_book[i],promo_info[i]]
    #final_list.append(exp_list.encode('utf-8'))
    with open ("Hotel.csv",'a') as myfile:
        wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
        wr.writerow(exp_list)
        wr.writerow("\n")
    i=i+1
#k=0    
#for i in final_list:
'''with open ("sa.csv",'a') as myfile:
    wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
    wr.writerow(final_list)
    wr.writerow("\n")'''
  #      k=k+1''''
