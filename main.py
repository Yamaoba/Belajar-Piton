text = '\n====================== Penghitung Bangun Ruang ==========================\n'
buka = text.center(20)

print(buka)

awal = input('\nPilih yang mana? kubus/balok: \n')
if awal== "balok" or awal=="Balok":
    pilihb = input('\nPilih yang mana? volume/luas permukaan: \n')
    
    if pilihb== 'volume' or pilihb=='Volume':
      print('\nPenghitung volume balok\n')
      ab = int(input('Panjang: '))
      bb  = int(input('Lebar: '))
      tb  = int(input('Tinggi: '))
      print (ab * bb * tb)
      
    elif pilihb== 'luas permukaan' or pilihb=='Luas permukaan':
      print('\nPenghitung luas permukaan balok\n')
      abl = int(input('Panjang: '))
      bbl  = int(input('Lebar: '))
      tbl  = int(input('Tinggi: '))
      print (2 * (abl*bbl + abl*tbl + bbl*tbl))

if awal== "kubus" or awal=="Kubus":
    pilihk = input('\nPilih yang mana? volume/luas permukaan: \n')
    
    if pilihk== 'volume' or pilihk=='Volume':
      print('\nPenghitung volume kubus\n')
      sk = int(input('Sisi: '))
      print (sk * sk * sk)

    elif pilihk== 'luas permukaan' or pilihk=='Luas permukaan':
      print('\nPenghitung luas permukaan kubus\n')
      skl = int(input('Sisi: '))
      print (6 * skl * skl)
      
else:
    raise Exception("Input Salah")
