import time
import pyAesCrypt
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
         girisDosya = input("Lütfen şifrelenecek dosyayı girin (data.txt)")
         cikisDosya = input("Lütfen şifrelenen dosyanın hangi dosyaya koyulacağını girin (output.txt)")
         sifre = input("Lütfen dosyanın decrypt keyini girin bu key'i kaybederseniz dosyayı tekrar decrypt edemezsiniz")
         with open(os.getcwd()+"/"+girisDosya, "rb") as girisD:
             with open(os.getcwd()+"/"+cikisDosya, "wb") as cikisD:
              pyAesCrypt.encryptStream(girisD, cikisD, sifre, 64*1024)
              print("PixelCrypt Aracılığı İle Dosya Başarılı Bir Şekilde Encrypt Edildi")
     except ValueError:
             remove(cikisD)#hata olduğunda çıkış verisini sil.
 

        #######################################




if process == "decrypt":
      try:
         girisDosya = input("Lütfen şifrelenmiş dosyayı girin (encrypted.txt)")
         cikisDosya = input("Lütfen düzeltilecek dosyanın hangi dosyaya koyulacağını girin (decrypted.txt)")
         sifre = input("Lütfen şifrlenmiş dosyanın decrypt keyini girin bu key'i kaybettiyseniz dosyayı tekrar decrypt edemezsiniz.")
         with open(os.getcwd()+"/"+girisDosya, "rb") as girisD:
                with open(os.getcwd()+"/"+cikisDosya, "wb") as cikisD:
                 boyut = os.stat(str(os.getcwd()+"/"+girisDosya)).st_size
                 pyAesCrypt.decryptStream(girisD, cikisD, sifre, 64*1024, boyut)
#                 pyAesCrypt.decryptStream(girisD, cikisD, sifre, 64*1024)
                 print("PixelCrypt Aracılığı İle Dosya Başarılı Bir Şekilde Decrypt Edildi")
      except ValueError:
             print("Bir Hata Oluştu, Yüksek İhtimalle Decrypt Key'i Yanlış.")

        #######################################

if process != "decrypt":
	if process != "encrypt":
		print("Lütfen sadece encrypt veya decrypt giriniz. Programı yeniden başlatınız.")