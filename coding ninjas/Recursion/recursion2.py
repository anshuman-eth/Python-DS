# def func(num):
#     if num==0:
#         return
#     func(num-1)
#     print(num,end=" ")

# num=int(input())
# func(num)

def func(num):
    if num==0:
        return
    print(num,end=" ")
    func(num-1)
    

num=int(input())
func(num)