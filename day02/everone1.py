count =  3
while count > 0:
    print(f"sending... {count}")
    count = count - 1
    # for - walk a range or a list
    for i in range (1,4): # 1,2,3(stops before 4)
        print(f"recipt #{i}")
        for name in ["Almaz" , "dawit" , "tigist"]:
            print(f"selam,{name}")