#dictionaries
#marks={"alice":30, "alina":45}
#alice_marks=marks["alice"]
#print(alice_marks)
#marks["Alpha"]=49
#login_credentials={"Alpha":"Alpha123", "Hima":"hexagon101"}
#username = input("enter username: ")
#checkifuserexists
#if username in login_credentials:
 #   p = input("enter your password: ")
  #  Original_password=login_credentials[username]

#    if p == Original_password:
 #       print("successfully logged in")
  #  else:
   #     print("incorrect passsword")
#else:
   # print("invalid username")

string = input("enter a string: ")
counter = {}
#store letter occurences
for letter in string:
    if not letter in counter:
         counter[letter] = 1
    else:
         counter[letter] = counter[letter] + 1
print(counter)
#find most occuring letter
most_occuring_letter = " "
max_so_far = 0
for letter in counter:
     if counter[letter]>max_so_far:
          max_so_far = counter[letter]
          most_occuring_letter = letter
print(most_occuring_letter)
print(max_so_far)
