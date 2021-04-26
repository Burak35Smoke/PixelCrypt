import time
import pycrypt
import os
from os import stat, remove
print("  --------\      /-\    \    /  --------  |                 ")
print("  |        |    |   |    \  /   |         |                ")
print("  |        |     \-/      \     |____     |                 ")
print("  |--------      | |     / \    |         |                ")
print("  |              | |    /   \   |         |                 ")
print("  |              |_|   /     \  --------- ---------               ")
print("")
print("  -----------     -------  \    /   |------\   ----------     ")
print(" |               |      /   \  /    |       |      ||          ")
print(" |               |     /     \/     |       |      ||         ")
print(" |               |-----       \     |------/       ||         ")
print(" |               |     \       \    |              ||          ")
print("  -----------    |      \       \   |              ||          ")
print("               Burak DOĞAN - github/Burak35Smoke               ")
print("                  Program açık kaynak kodludur.                ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

process = input("Lütfen yapılacak işlemi seçiniz. encrypt/decrypt : ")



if process == "encrypt":
     try:
         metin = input("Lütfen şifrelenecek metni girin (test) ")
         print(pycrypt.caesar.encrypt(metin, 12))
         print("PixelCrypt Aracılığı İle Metin Başarılı Bir Şekilde Encrypt Edildi ")
     except ValueError:
             print("Bir Hata Oluştu.")
 

        #######################################




if process == "decrypt":
      try:
         metin = input("Lütfen şifrelenen metni girin ")
         print(pycrypt.caesar.decrypt(metin, 12))
         print("PixelCrypt Aracılığı İle Dosya Başarılı Bir Şekilde Decrypt Edildi ")
      except ValueError:
             print("Bir Hata Oluştu, Yüksek İhtimalle Decrypt Key'i Yanlış veya Şifreleme sayısı bir sayı değil. ")

        #######################################


if process != "decrypt":
	if process != "encrypt":
		print("Lütfen sadece encrypt veya decrypt giriniz. Programı yeniden başlatınız.")
