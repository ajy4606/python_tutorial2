import theater_module
theater_module.price(3) # 3명이서 영화보러 감
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv #모듈명이 길 때에는 이름을 변경 가능, 별명
mv.price(3)
mv.price_morning(4)

from theater_module import *
#from random import *
price(3)
price_morning(5)

from theater_module import price, price_morning
price(5)
price_morning(6)

from theater_module import price_soldier as ps
ps(15)
