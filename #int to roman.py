#int to roman
def inttoroman(num):
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol= ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    romannum=''
    for i in range(len(val)):
        while num>=val[i]:
            romannum=romannum+symbol[i]
            num=num-val[i]
    return romannum

num=int(input("Enter an integer: "))
print(f"The Roman numeral for {num} is {inttoroman(num)}")
    
