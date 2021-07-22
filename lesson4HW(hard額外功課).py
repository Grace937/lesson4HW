w=int(input('幾層?'))
a=int(w/2)
b=int(w/2-0.5)
for i in range(w):
    if i<a:
        print(' '*i+'*'+' '*(w-2*(i+1))+'*'+' '*i)
    elif i==a:
        if a==b:
            print(' '*(w-i-1)+'*'+' '*(w-i-1))
        else:
            print(' '*(w-i-1)+'*'*2+' '*(w-i-1))
    else:
        print(' '*(w-i-1)+'*'+' '*((i*2)-w)+'*'+' '*(w-i-1))