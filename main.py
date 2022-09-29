print("Multiplication tables")
num = input("Enter a number to generate its multiplication table: ")
start_num = 1
while start_num <= 10:
    table = int(num) * int(start_num)
    print(f'{start_num} x {num} = {table}')
    start_num = start_num + 1

