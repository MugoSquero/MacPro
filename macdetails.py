from os import system
from time import sleep
from random import randint

def cls():
	system("clear")


def banner():
	system("figlet Macdetails")
	print("\n\n")

cls()
banner()

kart = str(input("Lütfen Ağ Kartınızı Giriniz : "))

cls()
banner()

secim = input(" 1 = MAC Adresini Göster.\n 2 = Benzer Bir Cihaz Adresi Gir.\n 3 = Rastgele Bir Cihaz Adresi Gir\n 4 = MAC Adresini Resetle\n 5 = Rastgele (unknown) MAC Adresi Gir\n 6 = Cihaz MAC Adreslerini Listele Ve Kaydet (MACLIST.txt)\n 7 = Belirli Bir MAC Adresi Gir\n 8 = Cihaza Özel Belirli MAC Adresi Gir.\n\n?: ")

cls()
banner()

if (secim == "1"):
	system("macchanger -s " + kart)
elif (secim == "2"):
	system("macchanger -a " + kart)
elif (secim == "3"):
	system("macchanger -A " + kart)
elif (secim == "4"):
	system("macchanger -p " + kart)
elif (secim == "5"):
	system("macchanger -r " + kart)
elif (secim == "6"):
	system("macchanger -l > MACLIST.txt")
elif (secim == "7"):
	macsec = input("Lütfen Belirlenecek MAC Adresini Girin (XX:XX:XX:XX:XX:XX) : ")
	system("macchanger -m " + macsec + " " + kart)
elif (secim == "8"):
	mac1 = randint(10, 99)
	mac2 = randint(10, 99)
	mac3 = randint(10, 99)
	maclistal = input("Bir Cihazın MAC Adresinin İlk 3 Hanesini Yazınız (Almak İçin Programda 6. Komutu Çalıştırın!) : ")
	mmac = (maclistal + ":" + str(mac1) + ":" + str(mac2) + ":" + str(mac3))
	system("macchanger -m " + mmac + " " + kart)
else:
	cls()
	banner()
	print("Yanlış Seçenek!")
	exit()
