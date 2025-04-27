
import random
attemp = 0
max_attemp = 5
adade_random = random.randint(0,100)

#print(adade_random)
while attemp < max_attemp :
    user_gass = int(input("Enter number: "))
    

    if  type(user_gass) == int :
          attemp += 1
          if user_gass > adade_random:
              print("adade shoma kami bozorgrar az adade mane :) ")
          elif user_gass < adade_random:
              print("adade shoma kami koochektar az adade mane :) ")
          else:
            print(" dorosst gofti ************ ")
            break
    else:
        print("meghdar vorodi shoma adad nist")

print(attemp)
