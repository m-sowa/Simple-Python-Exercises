#Program draws a Christmas tree
print()

def triangle(height):
    for i in range(height):
        for j in range(10):
            print(' ', end='')
        for j in range(10 - i):
            print(' ', end='')
        for j in range(i*2 + 1):
            print('*', end='')
        print()


for w in range (3,6):
    triangle(w)

#ending
input("\n\nPress Enter to finish.")