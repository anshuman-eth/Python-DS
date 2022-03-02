
def final(operations):
    t=0
    for i in operations:
        if (i=='++X') or (i=='X++'):
            t=t+1
        elif (i=='--X') or (i=='X--'):
            t=t-1
    return t

operations=["--X","X++","X++"]
p=final(operations)
print(p)