#Fibinacci number

#0,1,1,2,3,5,8,12,20......
# f0 ? , f1 ? 

def fibonacci(num):
    if num <= 1:
        return num
    else :
        return fibonacci(num-1) + fibonacci(num-2)
for i in range(10):
    print(fibonacci(i))