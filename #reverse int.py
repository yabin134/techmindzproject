#reverse int
num=int(input("Enter a integer  :"))
def reverseint(num):
    rev=int(str(num)[::-1])
    return rev

rev=reverseint(num)


print(f"Reversed integer is {rev}")