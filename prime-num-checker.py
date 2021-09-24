#Write your code below this line 👇
def prime_checker(number):
    ok = 0
    for nr in range(2,number):
        if(number % nr == 0 and ok == 0):
            print("It's not a prime number")
            ok = 1
    if ok == 0:
        print("It's a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



