def draw_piramyd(n):
    for i in range(n):
        print("*"*i, "\n")
        
        
n = int(input("Enter the levels of the pyramid: "))
draw_piramyd(n)