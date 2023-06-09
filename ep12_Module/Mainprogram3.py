# เรียก function เฉพาะที่เราต้องการ
from CalculateService import addition
from CalculateService import PI
from Weather import city

# ดึงมาทั้งหมด
from Weather import *
from CalculateService import *

addition(50,150,200)
print(PI)
print(city)

power(5,6)