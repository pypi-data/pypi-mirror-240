from time import sleep
while True:
    ch = input("select a option:\n\t1- start timer\n\t2- exit\n\tchoice:")
    if ch == "1":
        h = int(input("enter hours:"))
        m = int(input("enter minutes:"))
        s = int(input("enter seconds:"))
        total = (h * 3600) + (m * 60) + s
        while total >= 1:
            print(total)
            total -= 1
            sleep(1)
        print("timer ended")
    elif ch == "2":
        print("exiting ...")
        break
    else:
        print("wrong input!")
