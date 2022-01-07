'''import time
giay=time.time()
print(giay)



hientai=time.ctime(giay)
print(hientai)



print("nhập: ")
time.sleep(5)
print("hết giờ")


thoigian=time.localtime()
print(thoigian)
print("năm hiện tại", thoigian.tm_year)


import time
t=time.localtime()
print(t)
t=time.strftime("%m/%d/%y, %H:%m:%S", t)
print(t)
print(type(t))'''


#BT
import time
ten=input("nhập: ")
tuoi=int(input("nhập tuổi: "))
hientai=time.localtime()
nam=hientai.tm_year
print(nam)
(100-tuoi)+2021
print(f'nam {ten} đạt 100 tủi ', (100-tuoi)+nam)