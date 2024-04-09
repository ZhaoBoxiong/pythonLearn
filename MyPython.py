print("Hello Python World")

def python_loop():
    I_MAX = 3
    J_MAX = 2
    for i in range(I_MAX):
        for j in range(J_MAX):
            print("value of i is:", i, end=", ")
            print("value of j is:", j)
            
python_loop()


num = 10
pi = 3.14
letter = 'A'

my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_dict = {'name': 'Alice', 'age': 25}
my_set = {1, 2, 3, 4}

print("num =", num)
print("pi =", pi)
print("letter =", letter)
print("my_list =", my_list)
print("my_tuple =", my_tuple)
print("my_dict =", my_dict)
print("my_set =", my_set)


my_list = [1, 2, 3, 4, 5]
my_list.append(6)

for i in range(len(my_list)):
    print("my_list[{}] = {}".format(i, my_list[i]))

try:
    x = 10 / 0
except ZeroDivisionError:
    print("The divisor cannot be zero.")
