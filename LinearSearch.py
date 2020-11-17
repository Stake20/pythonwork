'''

pos =-1

def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1

    return False


'''


list = [5, 8, 4, 6, 9, 2]
n = 9
posi = -1
def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['posi'] = i
            return True



if search(list, n):
    print("Found", posi)
else:
    print("Not Found")





