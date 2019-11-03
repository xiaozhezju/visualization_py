# %%
import bs4 as bs
import urllib.request
from datetime import datetime

source = urllib.request.urlopen('file:///Users/xinyanzhang/Desktop/Mas.html').read()
soup = bs.BeautifulSoup(source,'lxml')

table = soup.find_all('table')

table_rows = table[0].find_all('tr')

data = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    data.append(row)
    # print(row)

data = data[1:]

for elem in data:
    dt = elem[0]
    elem[0] = datetime.strptime(dt, '%Y%m%d')

# %%

from pyecharts.charts import Calendar
from pyecharts import options as opts

Calendar().add("", data, calendar_opts=opts.CalendarOpts(range_=['2019-06', '2020-02'])).set_global_opts(
    title_opts=opts.TitleOpts(title="MasControl"),
    visualmap_opts=opts.VisualMapOpts(
        max_=5,
        min_=0,
        orient="horizontal",
        is_piecewise=True,
        pos_top="230px",
        pos_left="100px",
    ),
).render()


