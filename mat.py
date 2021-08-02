import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
import numpy as np
import pandas as pd

p = "./images/dmm.png"

class TkDf(tk.Tk):

  def __init__(self, df: pd.DataFrame):
    super().__init__()
    self.title("Display DataFrame")
    self.df = df

    for r in range(len(self.df)):
      for c in range(len(self.df.columns)):
        e = tk.Entry(self)
        e.insert(0, self.df.iloc[r,c])
        e.grid(row=r,column=c)
        # e.bind("<KeyPress>",lambda event, row=r, column=c: self.change(event,row,column))

  # def change(self,event,row,column):
    # value = event.widget.get()
    # self.df.iloc[row,column] = value
    # print(self.df)

if __name__=='__main__':

    app = App()
    app.mainloop()

  # im = Image.open(p)
  # plt.imshow(im)
  # print(im.size)