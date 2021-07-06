#Question2
Lista = ["Brasil", "Eua", "França", "Itália", "Holanda", "Japão", "China"]

#Question3
print(Lista)

#Question4
print(Lista[0:4])

#Question5
print(Lista[-3:])

#Question6
print(Lista[1:5])

#Question7
print(Lista[2:7:2])

#Question8
print(Lista[::-1])

#Question9
for item in Lista[0:7:2]:
    print(item)

#Question10
Frutas = ["apple", "Apple", "APPLE", "banana"]

#Question11
for Fruta in Frutas:
    print(Fruta)
   
#Question12
for Fruta in Frutas:
    if Fruta == "apple":
       print(Fruta)
    else:
        print("apple")

#Question13
for Fruta in Frutas:
    if Fruta == "apple":
       print(Fruta.upper())
    else:
        print(Fruta.lower())

