from os import system
from time import sleep

system("apt install figlet > null")
system("clear")
def banner():
	system("figlet AUTOMAC")
	print(" ============================================\n|\n|-- By Mugo Squero\n\n")

banner()

kart = str(input("Lütfen Ağ Kartınızı Giriniz : "))

system("clear")
banner()

isc = str(input(" 0 = Automac'i Başlat\n 1 = Automac'i Durdur!\n\n?: "))


if (isc == "1"):
	system("clear")
	banner()
	print("Durduruluyor..!\n\n")
	sleep(2)
	system("macchanger -p " + kart + " > null")
	system("rm null")
	print("Eski MAC Adresi Geri Alındı!")
	exit()

else:
	system("clear")
	banner()
	system("clear")
	banner()

sure = int(input("Her Değişim Arası Beklenilecek Süre? (saniye) : "))

system("clear")
banner()
print("İşlem Başlatılıyor...")
sleep(2)
system("rm null")
system("clear")
while 1:
	banner()
	print(55 * "-")
	system("macchanger -a " + kart)
	print(55 * "-")
	sleep(sure)
	system("clear")
