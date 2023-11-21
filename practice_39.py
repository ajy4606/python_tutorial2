#패키지
import travel.thailand #모듈이나 패키지만 가능, 클래스나 함수는 불가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage #클래스 import 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# *을 쓸 때 공개와 비공개 설정이 필요함 __all__ = ["vietnam"]
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
