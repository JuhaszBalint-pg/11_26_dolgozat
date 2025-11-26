'''
B csoport
Olvasunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze.
Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?
'''

szamok = []
fut = True

print('Adj meg egész számokat!\nA 0 bevitele a számok megadásának végét jelenti!\n')

while fut:
    useri = int(input(''))
    szamok.append(useri)
    if useri == 0:
        fut = False
    
print(szamok)

print('1. feladat')
neg_tiz_es_tizenot_kozt = []
for i in szamok:
    if -15< i <-10:
        neg_tiz_es_tizenot_kozt.append(i)
    
neg_tiz_es_tizenot_kozt_elof = len(neg_tiz_es_tizenot_kozt)

if neg_tiz_es_tizenot_kozt_elof > 0:
    print('Előfordul -10 és -15 közötti szám!')
else:
    print('Nem fordul elő -10 és -15 közötti szám')

print('2. feladat')
legn_koz_tobb_i = 0
for i in szamok:
    if i % 2 == 0 and i % 5 == 0 and i != 0:
        legn_koz_tobb_i = szamok.index(i)

if legn_koz_tobb_i != 0:
    print(f'{legn_koz_tobb_i}. indexen fordult elő utoljára 2-vel és 5-tel osztható szám')
else: 
    print('Nem fordult elő 2-vel és 5-tel osztható szám')

print('3. feladat')
husz_nagyobb = 0
for i in szamok:
    if i > 20:
        husz_nagyobb += 1

print(f'{husz_nagyobb} szám nagyobb húsznál') 

print('4.feladat')
legkis_pozitiv = 1000000000000000
for i in szamok:
    if i < legkis_pozitiv and i > 0:
        legkis_pozitiv = i
        legkis_pozitiv_elof = szamok.index(legkis_pozitiv) + 1
print(f'{legkis_pozitiv} a legkisebb pozitiv egész szám, előfordult: {legkis_pozitiv_elof}.-ként')

print('5. feladat')
negativ_szamok = []
negativ_összegek = 0
for i in szamok:
    if i < 0:
        negativ_szamok.append(i)
        negativ_összegek += i

negativ_atlag = negativ_összegek/len(negativ_szamok)
print(f'{negativ_atlag} a negativ számok átlaga')