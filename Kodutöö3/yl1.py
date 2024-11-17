def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

andmed = [10,30,58,43,90,104]
element = 90

index = linear_search(andmed,element)

if index != -1:
    print("Number leiti indeksil",index)
else:
    print("Numbrit ei leitud")

#Ajakompleksus on O(n) kuna see sõltub otsitava elemendi asukohast. Parim on O(1) - element on esimene.
#Halvim on O(n) kui leitakse element lõpust või ei leita üldse elementi massiivist.
#Ruumikompleksus on O(1) kuna ei kasutata muid muutujaid kui neid, mis on olemas.