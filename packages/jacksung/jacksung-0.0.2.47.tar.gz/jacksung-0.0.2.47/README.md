# jacksung's utils
Python version is required above 3.9.

Recommend version: python 3.11.

Create env by conda: 
```conda create -n jacksung python=3.11```
## Commit new dependence
Please refer to how to upload a dependence
```
python setup.py sdist bdist_wheel
twine upload dist/*
```
## Installation
```pip install jacksung```
## Login ecnu
1 [download chromedriver](https://googlechromelabs.github.io/chrome-for-testing/)
    windows:chromedriver.exe
    linux:chromedriver
    
2 make the directory 'chrome' in the home path

3 the driver file into the 'chrome' directory

4 make the directory 'chrome' in the 'chrome' directory

5 run
```ecnu_login -u 账号 -p 密码```
## Multi threadings
```
from jacksung.utils.multi_task import MultiTasks
import time

def worker(idx):
    print(idx)
    time.sleep(2)
    return idx

mt = MultiTasks(3)
for idx in range(10):
    mt.add_task(idx, worker, (idx))
results = mt.execute_task()
```
## Connecting to mysql
```
from jacksung.utils.base_db import BaseDB, convert_str
class DB:
    def __init__(self, ini_path='../db.ini'):
        self.bd = BaseDB(ini_path)

    def insert_record(self, year, month, day, type):
        sql = rf"INSERT INTO `data_record` (`year`,`month`,`day`,`type`) VALUES ({year},{month},{day},{convert_str(type)});"
        self.bd.execute(sql)

    def record_err_log(self, log):
        sql = rf"INSERT INTO `err_log` (`log`) VALUES ({convert_str(log)});"
        self.bd.execute(sql)

    def select_record(self, year, month, day, type):
        sql = rf"select count(1) from data_record where year={year} and month={month} and day={day} and type={convert_str(type)};"
        result, cursor = self.bd.execute(sql)
        return cursor.fetchone()[0]
```
db.ini is the form  as follows:
```
[database]
host = 1.1.1.1
user = root
password = root
database = XXX
```
## Show Nvdia information
```watch_gpu```
or set the command line to the bash file
```alias watch-gpu='watch -n 1 -d watch_gpu'```

## Time calculating
```
from jacksung.utils.time import RemainTime
import time

epochs=100
rt = RemainTime(epochs)
for i in range(epochs):
    rt.update()
    time.sleep(2)
```

## Convert utils
convert .nc to numpy, convert numpy to tif (with or without geocoordinate)

```
from jacksung.utils.data_convert import nc2np, np2tif
import numpy as np

nc_t = nc2np(r'C:\Users\ECNU\Desktop\upper.nc')
np2tif(nc_t, 'constant_masks/upper')
np2tif('constant_masks/land_mask.npy', save_path='constant_masks', out_name='land_mask', left=0, top=90, x_res=0.25,
       y_res=0.25, dtype=np.float32)
np2tif('constant_masks/soil_type.npy', save_path='constant_masks', out_name='soil_type', left=0, top=90, x_res=0.25,
       y_res=0.25, dtype=np.float32)
np2tif('constant_masks/topography.npy', save_path='constant_masks', out_name='topography', left=0, top=90, x_res=0.25,
       y_res=0.25)
```
