rad = int(input("radius : "))
dia = (rad*2)+1
h = rad
k = rad
x = 1
y = 1

for cord in range(0,dia):
    for rows in range (0,dia):
        if (((x-h)**2)+((y-k)**2)) == rad**2:
            print('x')
        else:
            print (' ')
        x = x+1
    y = y+1 
        
