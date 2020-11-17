
klopp_file = open("klopp_squad.txt", "r")

f = open('MyData', 'w')
f1 = open('FB_IMG_15892078738303084.jpg', 'rb')
f2 = open('MyData.jpg', 'wb')

for data in f1:
    f2.write(data)

for datas in klopp_file:
    f.write(datas)

klopp_file.close()