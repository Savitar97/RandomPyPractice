import random

def e_pi(n):
  num_p_in_circle=0
  num_all_p=0
  for _ in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    dis=x**2+y**2
    if dis<=1:
      num_p_in_circle+=1
    num_all_p+=1
  return 4*num_p_in_circle/num_all_p
    
