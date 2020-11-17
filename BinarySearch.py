

pos =-1

def search(list, n):
    i = 0
    u = len(list)-1

    while i <= u:
        mid = (i+u) // 2

        if list(mid) == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l =mid + 1
            else:
                u = mid - 1

    return False

list = [4, 7, 8, 12, 45, 99]
n = 45

if search(list, n):
    print("Found", pos)
else:
    print("Not Found")
