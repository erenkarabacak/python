onlar = {10:"on",20:"yirmi",30:"otuz",40:"kırk",50:"elli",60:"altmış",70:"yetmiş",80:"seksen",90:"doksan"}
birler = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}

sayi = int(input("Sayı: "))
onlarb = int(sayi / 10)*10;
birlerb = sayi % 10;

if birlerb > 0:

    print("{0} sayısının okunuşu {1}{2}".format(sayi,onlar[onlarb],birler[birlerb]))
else :
    print("{0} sayısının okunuşu {1}".format(sayi, onlar[onlarb]))