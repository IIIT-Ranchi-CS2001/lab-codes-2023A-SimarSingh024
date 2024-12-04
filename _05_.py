s1 = "Maha Bharat"
p = s1.split()
print(p[0][0].lower()+p[0][1:].upper()+" "+p[1][0].lower()+p[1][1:].upper()) #Generates mAHA bHARAT
print(p[1]) #Generates Bharat
print(p[1]*3) #Generates BharatBharatBharat
print("Mera"+" "+p[1]) #Generates Mera Bharat
print("Mera"+" "+p[1]+" "+"Mahan") #Generates Mera Bharat Mahan