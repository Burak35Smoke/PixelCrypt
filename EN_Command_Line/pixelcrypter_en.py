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
print("                  The program is open source.                ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

process = input("Please select the action to be taken. encrypt/decrypt : ")



if process == "encrypt":
     try:
         metin = input("Please enter the text to be encrypted (test) ")
         print(pycrypt.caesar.encrypt(metin, 12))
         print("Text Successfully Encrypt Through PixelCrypt ")
     except ValueError:
             print("Something went wrong.")
 

        #######################################




if process == "decrypt":
      try:
         metin = input("Please enter the encrypted text ")
         print(pycrypt.caesar.decrypt(metin, 12))
         print("Text Successfully Encrypt Through PixelCrypt ")
      except ValueError:
             print("Something went wrong.")

        #######################################


if process != "decrypt":
	if process != "encrypt":
		print("Please just enter encrypt or decrypt. Restart the program.")
