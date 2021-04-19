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
print("                  The program is open source.               ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

process = input("Please select the action to be done. encrypt/decrypt : ")



if process == "encrypt":
     try:
         girisDosya = input("Please enter the file to be encrypted (data.txt)")
         cikisDosya = input("Please enter in which file the encrypted file will be put (output.txt)")
         sifre = input("Please enter the decrypt key of the file. If you lose this key, you cannot decrypt the file again.")
         with open(os.getcwd()+"/"+girisDosya, "rb") as girisD:
             with open(os.getcwd()+"/"+cikisDosya, "wb") as cikisD:
              pyAesCrypt.encryptStream(girisD, cikisD, sifre, 64*1024)
              print("File Successfully Encrypt Through PixelCrypt")
     except ValueError:
             print("An Error Occurred, Most Likely Decrypt Key Wrong.")
 

        #######################################




if process == "decrypt":
      try:
         girisDosya = input("Please enter the encrypted file (encrypted.txt)")
         cikisDosya = input("Please enter in which file the file to be corrected will be put. (decrypted.txt)")
         sifre = input("Please enter the decrypt key of the encrypted file. If you lost this key, you cannot decrypt the file again.")
         with open(os.getcwd()+"/"+girisDosya, "rb") as girisD:
                with open(os.getcwd()+"/"+cikisDosya, "wb") as cikisD:
                 boyut = os.stat(str(os.getcwd()+"/"+girisDosya)).st_size
                 pyAesCrypt.decryptStream(girisD, cikisD, sifre, 64*1024, boyut)
#                 pyAesCrypt.decryptStream(girisD, cikisD, sifre, 64*1024)
                 print("File Successfully Decrypt Through PixelCrypt")
      except ValueError:
             print("An Error Occurred, Most Likely Decrypt Key Wrong.")

        #######################################

if process != "decrypt":
	if process != "encrypt":
		print("Please just enter encrypt or decrypt. Restart the program.")