from nox import DmmCrawl
# from tkdf import TkDf
from tktable import TkTable
import datetime
from time import sleep
import json
import pandas as pd
import threading

def datestring():
  dt_now = datetime.datetime.now()
  oneday = datetime.timedelta(days=1)
  if dt_now.hour < 12: dt_now -= oneday
  yyyymmdd = dt_now.strftime('%Y-%m-%d')
  
  return yyyymmdd

def main():
  # DS上里
  icon_p = "./images/ds_kamisato.png"
  json_p = "./ds_kamisato.json"
  # json_p = "./ds_test.json"
  
  yyyymmdd = datestring()
  work_p = f"./ds_kamisato_works_{yyyymmdd}.json"
    
  with open(json_p, "r", encoding="utf-8") as f:
    read_dic = json.load(f)
  # print(read_dic)
  
  crawl = DmmCrawl()
  proc = crawl.openDmm()
  crawl.clickHall(icon_p)
  works = {}
  for key, item in read_dic.items():
    dic = crawl.machine(int(key), item)
    works.update(dic)
  proc.terminate()
  
  # works = {2: ["madoka", "date", "0", "0", "0", "0"]}
  lst = [[key, *item] for key, item in works.items()]
  col = ["No", "machine", "date", "初当", "継続", "最終", "前日"]
  df = pd.DataFrame(lst, columns=col)
  
  app = TkTable(df)
  app.run()
  # app.geometry("+600+50")
  # app.mainloop()
  
  df_0 = df[df["初当"] == "0"]
  
  if len(df_0):
    app_0 = TkTable(df_0)
    app_0.run()
    # app_0.geometry("+700+100")
    # app_0.mainloop()
  
    dic = {idx: list(row) for idx, row in df_0.iterrows()}
    read_json = json.dumps(dic, ensure_ascii=False)
    with open(work_p, "w", encoding="utf-8") as f:
      f.write(read_json)

def waitmonitor():
  crawl = DmmCrawl()
  crawl.clickwait()

if __name__=='__main__':

  mainprocess = threading.Thread(target=main)
  subprocess = threading.Thread(target=waitmonitor)
  
  mainprocess.start()
  subprocess.start()