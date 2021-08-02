import tkinter as tk
import pandas as pd
import json
import datetime

class TkDf(tk.Tk):

  def __init__(self, df: pd.DataFrame):
    super().__init__()
    self.title("Display DataFrame")
    self.col_line = 0

    if type(df.columns) == pd.core.indexes.base.Index:
      for c in range(len(df.columns)):
        e = tk.Entry(self)
        e.insert(0, df.columns[c])
        e.grid(row=0, column=c)
      self.col_line = 1
          
    for r in range(len(df)):
      for c in range(len(df.columns)):
        e = tk.Entry(self)
        e.insert(0, df.iloc[r,c])
        e.grid(row=r+self.col_line,column=c)
                
if __name__=='__main__':

  dt_now = datetime.datetime.now()
  oneday = datetime.timedelta(days=1)
  if dt_now.hour < 12: dt_now -= oneday
  yyyymmdd = dt_now.strftime('%Y-%m-%d')
  
  p_r = f"./ds_works_{yyyymmdd}.json"
  with open(p_r, "r", encoding="utf-8") as f:
    read_dic = json.load(f)
    
  lst = [[key, *item] for key, item in read_dic.items()]
  col = ["No", "machine", "date", "初当", "継続", "最終", "前日"]
  df = pd.DataFrame(lst, columns=col)
  
  app = TkDf(df)
  app.geometry("+600+50")
  app.mainloop()
  
  df_0 = df[df["初当"] == "0"]
  
  app_0 = TkDf(df_0)
  app_0.geometry("+700+100")
  app_0.mainloop()