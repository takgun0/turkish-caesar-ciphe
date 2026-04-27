"""
Sezar Şifreleme Aracı
--------------------------------------
Bu program, girilen metni belirtilen kaydırma miktarına göre
Sezar algoritması kullanarak şifreler veya çözer.
"""
alfabe_kucuk = "abcçdefgğhıijklmnoöprsştuüvyz"
alfabe_buyuk = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

sonuc = ""
print("Sezar Şifreleme Aracına Hoş Geldiniz")

islem = input("Yapmak istediğiniz işlem (şifrele/çöz): ").lower().strip()
mesaj = input("Metni giriniz: ")

try:
    kaydirma = int(input("Kaydırma miktarını giriniz: "))
except ValueError:
    print("Hata: Lütfen sadece sayı giriniz!")
    exit()

if islem == 'çöz':
    kaydirma = -kaydirma

for harf in mesaj:
    # Karakter büyük harf ise
    if harf in alfabe_buyuk:
        indeks = alfabe_buyuk.index(harf)
        yeni_indeks = (indeks + kaydirma) % len(alfabe_buyuk)
        sonuc += alfabe_buyuk[yeni_indeks]

    # Karakter küçük harf ise
    elif harf in alfabe_kucuk:
        indeks = alfabe_kucuk.index(harf)
        yeni_indeks = (indeks + kaydirma) % len(alfabe_kucuk)
        sonuc += alfabe_kucuk[yeni_indeks]

    # Harf değilse (boşluk, nokta vs.) olduğu gibi bırak
    else:
        sonuc += harf

print("\nİşlem Sonucu:", sonuc)