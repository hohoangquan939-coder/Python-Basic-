def bang_cuu_chuong(a):
    for i in range(1, 11): 
        if (a*i)%2 == 0: 
            print(f"{a} x {i} = {a*i}")
        

    
a = int(input("Nhap n: "))
bang_cuu_chuong(a)