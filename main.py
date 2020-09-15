# Author: Grace Lavin gcl5087@psu.edu
# Collaborator: Yue Wu yzw5627@psu.edu
# Collaborator: Shiao Zhuang sqz5328@psu.edu
# Collaborator: Michael Artlip mva5905@psu.edu
# Section: 1
# Breakout: 18

def sum_n(n):
  if n == 0:
    return 0
  else:
    return n + sum_n(n-1)
  

def print_n(s, n):
  if n > 0:
    print(s)
    return print_n(s,n-1)

def run():
  getN = input("Enter an int: ")
  intN = int(getN)
  print(f"sum is {sum_n(intN)}.")
  getS = input("Enter a string: ")
  print_n(getS, intN)
 
   
  
if __name__ == "__main__":
  run()


