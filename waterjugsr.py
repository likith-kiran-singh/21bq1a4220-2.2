def pour(jug1,jug2,fill):
    max1,max2,fill=jug1,jug2,fill
    print("%d\t%d"%(jug1,jug2))
    
    apply_rule(ch,x,y)
def apply_rule():






j1 = int(input("Enter the Capacity of Jug-1 in Liters: "))
j2 = int(input("Enter the Capacity of Jug 2 in Liters: "))
g = int(input("Enter the Required water in Jug-1:"))
def rules():
    print("================================RULES==============================")
    print("Rule 1: Fill Jug-1")
    print("Rule 2: Fill Jug-2")
    print("Rule 3: Pour Some Water from Jug-1") # not used 
    print("Rule 4: Pour Some Water from Jug-2") # not used
    print("Rule 5: Empty Jug-1 ")
    print("Rule 6: Empty Jug-2 ")
    print("Rule 7: Transfer some water from Jug-1 to jug 2 until Jug-2  is full")
    print("Rule 8: Transfer some water from Jug-2 to jug 1 until Jug-1 is full")
    print("Rule 9: Transfer all water from Jug-1 to Jug-2")
    print("Rule 10: Transfer all water from Jug-2 to Jug-1")
        
x = y = 0
print("================================STATUS===========================")
print("The Initial State is:", end = " ")
print(x, y)

while(True):
  if (x==g):#or (y==g):
    print('***************  GOAL ACHIEVED! ******************')
    break
  else:
      rule=input("DO u want to see the rules?(y/n)")
      if rule=='yes':
          rules()
      ch = int(input("Enter rule to apply: "))
      x, y = apply_rule(ch, x, y)
      print("================================STATUS===========================")
      print("After Applyting the Rule, then the Current State is:", end = " ")
      print(x, y)
      break