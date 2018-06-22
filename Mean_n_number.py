num = float(input("Enter your number : "))
count = 1
sum_num = 0

while num != 0 or 0.0 :
    sum_num += num
    avg = sum_num / count
    count += 1
    print("Average og number :", avg)
    num = float(input("Enter your number : "))
else:
    print("good bye")

