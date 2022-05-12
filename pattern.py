# pattern printing

print("How Many Row You Want To Print")
while True:
    try:
        row= int(input())

    except ValueError:
        print("sorry, i didn't understand that ")

        continue
      
    else :
        break
while True:
  try:
    one = int(input("type 1 or 0: ")) 
    if one== 1 or one == 0:
      new = bool(one)
      break
    else:
      print("this value is not 0 or 1 please enter right value")      
  except ValueError:
    print("Provide an integer value...")
    continue

if new == True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
