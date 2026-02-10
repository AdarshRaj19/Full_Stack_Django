def add(a,b):
    return a+b
print(add(2,3))
def add2(a,b=100):
    return a+b
print(add2(12))

def abc(*arg):
    print(arg)
abc(1,2,3,4,5,"gg")

#write a fun which can calculate sum of any number pass to that function
def mysum(*nums):
    s=0
    for num in nums:
        s = s+num
    return s
print(mysum(1,2,3,4,5,6,7,8,9,10))

#write a fun to print a braking msg for dinner party
def dinner_breaking_msg(name):
    print(f"Dear {name}, the dinner party is about to end. Please wrap up your conversations.") 
dinner_breaking_msg("Adarsh")
dinner_breaking_msg("Raj")

#other code
def dinner_invite(name):
    print("*****************************************")
    print(f"Dear {name}, you are cordially invited to the dinner party at my place this Saturday at 7 PM.")
dinner_invite("Adarsh")
dinner_invite("Raj")

def greeting(*names):
    for name in names:
        print("*"*40)
        print(f"welcome to Mr. /ms. {name}\nyou are invited for dinner party today")
        print("*"*40)
greeting("Adarsh","Raj","Ankit")

