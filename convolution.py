import itertools

def sumAllMem(arr):
  sum=0
  for i in arr:
    sum=sum+i
  return sum

def dice_variants(x):
  variants = []
  # Generate all possible variants from using 4 dices
  for roll in itertools.product(range(1, 7), repeat=4):
    # filter only variants that sum of 4 dices matches
    if sumAllMem(roll) == x:
      variants.append(list(roll))
  return variants

def calProb(arr):
  p=[0.3, 0.1, 0.1, 0.2, 0.2, 0.1]
  prod=1
  for i in arr:
    prod=prod*p[i-1]
  return prod

def sumRV():
  res=[]
  for i in range(4,25):
    sum=0
    print("sum",i,"variants:",dice_variants(i))
    for j in dice_variants(i):
      sum=sum+calProb(j)
    res.append(f"{sum:.4f}")
  return res

result=sumRV()
print("\nResult:")
for i in range(4,25):
  print("sum",i,"prob:",result[i-4])
