import random
import time

# Educational intuit, I take no responsibility for anything YOU do with this code

numbers = random.randint(0, 9)
characters = '@', '!', '#', '$', '&', '*'
letters1 = 'abcdefghijklmnopqrstuvwxyz'
letters2 = letters1.upper()

list = numbers, random.choice(characters), random.choice(letters1), random.choice(letters2)
decryptor_key = random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list), random.choice(list)

print("Your decriptor is being generated...")
time.sleep(3.5)
print("Generated!!!")

waring = open("WARING!.txt", "w")
waring.write("Hello you who are reading this, I am grateful to have seen this text file.\nThis file was created to make it very clear, I do not take responsibility for anything you do with this\nlittle code, I created it for educational purposes and not for a kiddie script\nto take it and use for a ransoware. Thanks for the preview =)")
waring.close()
archive = open("decryptor_key", "x")
archive.write("Your decryptor is: {}".format(decryptor_key))
archive.close()
