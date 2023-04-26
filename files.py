

#lines=file.readlines()

#file_to_write=open("evens.txt",'w')

#for line in lines:
 #   if int(line)%2==0:
  #      file_to_write.write(line.strip)


with open("evens.txt",'a') as file:
    file.write("hello!")
