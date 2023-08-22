#แสดงข้อมูลหลายๆ ประเภทใน Print เดียว

#1. ใช้ , โดยมันจะมี space ในแต่ละ ,
print("SAU", 555, 123.456, True, 10+50)

#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช่ String ต้องแปลงเป็น String และไม่มี space เหมือนกับ ,
print("SAU "+str(555)+" "+str(123.456)+" "+str(True)+" "+str(10+50))

#3. ใช้เมธอดชื่อ format
print("SAU {} {} {} {}".format(555, 123.456, True, 10+50))
print("SAU {0} {1} {2} {3}".format(555, 123.456, True, 10+50))

#4. ใฃ้ f-string ***
print(f"SAU 555 {123.456} {True} {10+50}")

#-----------------------
#กรณี 1 บรรทัดมีหลาย Statement
print("aaa"); print("111"); print(False)