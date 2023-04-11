szam = int(input('Adj meg egy számot 5 és 10 között! '))

while szam < 5 or 10 < szam:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
print('Rendben!') 