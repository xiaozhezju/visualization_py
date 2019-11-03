# %%
import pandas as pd
from datetime import datetime

# first row as col name
dt = pd.read_html('file:///Users/xinyanzhang/Desktop/Mas.html',header=0)

df = dt[0]

def str2dt (dtstr):
    return datetime.strptime(str(dtstr), '%Y%m%d')

df.loc[:, 'dt'] = df.loc[:, 'Date'].map(str2dt)

data = []

nrow = df.shape[0]

# pd int64 != py int  needs conversion
for row in range(nrow):
    # print(row)
    item = [df.loc[row, 'dt'], int(df.loc[row, 'Times'])]
    data.append(item)

# print(data)

# %%

from pyecharts.charts import Calendar
from pyecharts import options as opts

cald = Calendar().add("", data, calendar_opts=opts.CalendarOpts(range_=['2019-06', '2020-02'])).set_global_opts(
    title_opts=opts.TitleOpts(title="MasControl"),
    visualmap_opts=opts.VisualMapOpts(
        max_=5,
        min_=0,
        orient="horizontal",
        is_piecewise=True,
        pos_top="230px",
        pos_left="100px",
    ),
)

cald.render()

# %%

from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
make_snapshot(snapshot, cald.render(), "masterSurvery.png")
