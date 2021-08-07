import subprocess, sys
import pandas as pd
import datetime
import json
import os

def datestring():
  dt_now = datetime.datetime.now()
  oneday = datetime.timedelta(days=1)
  if dt_now.hour < 12: dt_now -= oneday
  # dt_now -= oneday
  yyyymmdd = dt_now.strftime('%Y-%m-%d')
  
  return yyyymmdd
  
def df2md(p: str, df: pd.DataFrame) -> None:

  markdown_text = f"""---
layout: post
---

### sub title

{df.to_html()}

"""
  with open(p, "w", encoding="utf-8") as f:
    f.write(markdown_text)
    
  while not os.path.isfile(p):
    sleep(1)

if __name__=='__main__':

  p = "C:/Users/frog7/jupyter/halls/else"

  yyyymmdd = datestring()
  
  json_p = f"./ds_kamisato_{yyyymmdd}.json"
  with open(json_p, "r", encoding="utf-8") as f:
    read_dic = json.load(f)
    
  lst = [v for v in read_dic.values()]
  col = ["No", "machine", "date", "初当", "継続", "最終", "前日"]
  df = pd.DataFrame(lst, columns=col)
  md_p = p +  "/_posts/" + yyyymmdd + "-ds-kamisato-zero.md"
  
  df2md(md_p, df)

  try:
    proc = subprocess.run('bundle exec jekyll build', cwd=p, shell=True)
    print(proc.returncode)
  except subprocess.CalledProcessError:
    print("a jekyll processing failed")
    sys.exit(1)

  try:
    proc = subprocess.run('surge _site/ brown-jellyfish.surge.sh', cwd=p, shell=True)
  except subprocess.CalledProcessError:
    print("a surge processing failed")
    sys.exit(1)
  

  # work_json = nox
  # df = work_json
  # df.loc[] = []
  # lst <- marge <- df
  # zerogame_json = dic <- lst

  # markdown = zerogame_json

  # bundle exec jekyll build
  # surge _site/ brown-jellyfish.surge.sh
  
  