import time
print('Bom akan meledak 5 detik lagi')

for i in range(5, 0, -1):
    time.sleep(1)
    print str(i)

print('BOOM!!')
