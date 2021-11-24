import random
import time

time.sleep(1)
print("password gen ง่ายๆ")
time.sleep(1)
gen = int(input("ความยาวของ password ที่ต้องการ(ความยาวได้ตั้งแต่ 1-69 นะ) : "))

if gen > 70:
    for i in range(200):
        print("บอกไม่ฟังงง ย้ากกกกกกกกกกกกกกกกกกกกกกก! หนีแม่ง")
        exit()
        

p = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*+'
u = "".join(random.sample(p,gen))
time.sleep(1)
print("password ของคุณ : ",u)
time.sleep(1)