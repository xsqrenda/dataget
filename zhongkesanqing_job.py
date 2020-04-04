# 用法:python /home/crawler/zhongkesanqing_job.py 几天内（不含）
# 例子:python /home/crawler/zhongkesanqing_job.py 10
from bs4 import BeautifulSoup
import requests,re,datetime,sys

url='http://special.zhaopin.com/pagepublish/34595653/index.html'
r = requests.get(url)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, "lxml");
x = re.search(r'\[\r\n\[([\s\S]*)\]\r\n\]',r.text).group().replace('\n','').replace('\r','')
a = eval(x)
for i in a:
	if re.search(r'^\d{4}(\-)\d{1,2}\1\d{1,2}$',i[8]):
		distribution_date = datetime.datetime.strptime(i[8],'%Y-%m-%d')
		now_date = datetime.datetime.now()
		dis = now_date - distribution_date	
		dis_days = dis.days
		if i[2]=='兰州' and dis_days<eval(sys.argv[1]):# and '兰州' in i[6] eval(days)
			print(i)
