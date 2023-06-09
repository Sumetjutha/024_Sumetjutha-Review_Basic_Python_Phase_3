# โปรแกรมหลัก
import CalculateService as C
import Weather as W

C.addition(5,10,20)

print(C.PI)

#แสดงสภาพอากาศจังหวัดระยอง
result_Rayong = W.city["ระยอง"]
print(result_Rayong)

#แสดงผลทุกๆจังหวัด
W.getWeather()

#หาค่าเลขยกกำลัง
C.power(5,2)