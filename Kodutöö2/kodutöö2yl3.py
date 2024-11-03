def insertion_sort(loend):  
  
        for i in range(1, len(loend)):  
  
            value = loend[i]  
  
            j = i - 1  
            while j >= 0 and value < loend[j]:  
                loend[j + 1] = loend[j]  
                j -= 1  
            loend[j + 1] = value  
        return loend  
  
loend = [12, 11, 13, 5, 6, 7]  
print("Mittesorteeritud loend on: ", loend)  
  
print("Sorteeritud loend on: ", insertion_sort(loend))  

#Insertion sort on tõhusam selles loendis, kuna andmed on osaliselt sorteeritud
#(Elemendid enamasti õigete kohtade ligidal) ja see vähendab töömahtu.