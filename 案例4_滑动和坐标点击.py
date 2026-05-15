import time

from comm.base import *

driver = Driver().open_app('com.dangdang.buy2','.activity.ActivityMainTab')

start_x = '700'
start_y = '300'
end_x = '200'
end_y = '300'

time.sleep(5)
driver.swipe(start_x,start_y,end_x,end_y)

time.sleep(5)
driver.swipe(end_x,end_y,start_x,start_y)

#点击坐标，持续500毫秒
time.sleep(5)
driver.tap([(760,57)],500)