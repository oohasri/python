import random
def randInt(min='',max=''):
    # num = random.random()
    num = int(random.random() * 100)
    if max!=0:
        num = int(random.random() * 50)
    if min!=0:
        num = int(random.random() * 50 + 50)
    if min!=0 and max!=0:
        num = int(random.random() * max-min + min)
    if min>max:
    	temp=min
    	min=max
    	max=temp
    if max<0:
    	temp=max
    	max=min
    	min=
    return num
#print(randInt())
#print(randInt(max=50))
#print(randInt(min=20))
print(randInt(min=50, max=500))