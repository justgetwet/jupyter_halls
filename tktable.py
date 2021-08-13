import tkinter as tk
from tkinter import ttk
import pandas as pd
import json
import unicodedata

class TkTable:

  def __init__(self, df: pd.DataFrame):
    self.root = tk.Tk()
    self.df = df
    
    self.root.geometry("400x800+600+50")
    # self.bgcolor = "lightyellow"
    self.tblcolor = "lavender"
    
    canvas = tk.Canvas(self.root)

    bar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
    bar.pack(side=tk.RIGHT, fill=tk.Y)
    bar.config(command=canvas.yview)
    canvas.config(yscrollcommand=bar.set)
    canvas.config(scrollregion=(0, 0, 0, 910*3)) # スクロール範囲を設定
    # canvas.config(bg=self.bgcolor)
    canvas.pack(fill=tk.BOTH, expand=True) # tk.BOTH：縦横両方向に対して引き伸ばす
    # Canvasの上にFrameを載せる
    self.Frame = tk.Frame(canvas, bd=5)
    # self.Frame.config(bg=self.bgcolor)
    canvas.create_window((0,0), window=self.Frame, anchor=tk.NW)
    
  def treev(self):
    tree = ttk.Treeview(self.Frame, height=len(self.df))
    
    s = ttk.Style()
    s.theme_use("clam")
    s.configure("Treeview.Heading", background=self.tblcolor)
    
    tree["show"] = "headings"
    cols = tuple(range(1, len(self.df.columns)+1))
    tree['columns'] = cols
    sizes = self.column_sizes()
    for i, col, size in zip(cols, self.df.columns, sizes):
      tree.heading(i, text=f"{col}")
      tree.column(i, width=size*8+4) # 
    
    lst = [tuple(t)[1:] for t in self.df.itertuples()]
    for i, tpl in enumerate(lst):
      tree.insert("", "end", tags=i, values=tpl)
    
    tree.pack(pady=10, padx=10)
    
  def column_sizes(self) -> list:

    def ea_width_count(text):
      count = 0
      for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
          count += 2
        else:
          count += 1
      return count
    
    lst_columns = [[col] + list(self.df[col]) for col in self.df.columns]
    col_sizes = []
    for lst in lst_columns:
      col_sizes.append(max([ea_width_count(str(e)) for e in lst]))

    return col_sizes
  
  def run(self):
    self.treev()
    self.root.mainloop()

if __name__ == '__main__':

  yyyymmdd = "2021-08-10"
  work_p = f"./ds_kamisato_works_{yyyymmdd}.json"
  with open(work_p, "r", encoding="utf-8") as f:
    read_dic = json.load(f)

  # lst = [[key, *item] for key, item in read_dic.items()]
  lst = [list(v) for v in read_dic.values()]
  col = ["No", "machine", "date", "初当", "継続", "最終", "前日"]
  df = pd.DataFrame(lst, columns=col)
  
  t = TkTable(df)
  t.run()
