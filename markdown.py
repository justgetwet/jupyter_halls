import pandas as pd
import json
import datetime

def datestring():
  dt_now = datetime.datetime.now()
  oneday = datetime.timedelta(days=1)
  if dt_now.hour < 12: dt_now -= oneday
  yyyymmdd = dt_now.strftime('%Y-%m-%d')
  
  return yyyymmdd

if __name__=='__main__':

  yyyymmdd = datestring()
  p = f"./ds_kamisato_{yyyymmdd}.json"
  with open(p, "r", encoding="utf-8") as f:
    read_dic = json.load(f)
    
  lst = [[*item] for key, item in read_dic.items()]
  col = ["No", "machine", "date", "初当", "継続", "最終", "前日"]
  tbl = pd.DataFrame(lst, columns=col).to_html()

  markdown_text = f"""---
layout: post
---

### Table

{tbl}

"""

  p_m = f"./else/_posts/{yyyymmdd}-Ds-Kamisato-Zeros.md"
  with open(p_m, "w", encoding="utf-8") as f:
    f.write(markdown_text)
    
  # print(markdown_text)