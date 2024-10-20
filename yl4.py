def binaarne_otsing(arr, otsitav):

    vasak = 0
    parem = len(arr) - 1
    
    while vasak <= parem:
        keskel = (vasak + parem) // 2  # Leiame keskmise indeksi
        
        if arr[keskel] == otsitav:
            return keskel  # Tagastame leitud indeksi
        elif arr[keskel] < otsitav:
            vasak = keskel + 1  # Otsime paremas pooles
        else:
            parem = keskel - 1  # Otsime vasakus pooles
    
    return "Number ei ole loendis."  # Kui number ei leitud

sorteeritud_loend = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] #suvaline numbrite loend
otsitav_number = int(input("sisesta number mille indeksit otsid ")) #kasutaja saab sisestada numbri mille indeksit otsib

tulemus = binaarne_otsing(sorteeritud_loend, otsitav_number) #ananb tulemuse
print(f"Indeks: {tulemus}")