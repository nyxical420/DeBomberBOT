from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import keyboard
import random
import time

# Settings
roomcode = "CODE"
textfile = "words.txt"
humanmode = True
usebonus = True # Setting this to False will lower the chance of the bot getting another life.
createtypo = True

# User / Bot Settings
isbotaccount = False
botname = "DeBomberBOT"
jklmSettings = "" # JSON Data Required

driver = webdriver.Chrome("./chromedriver")

if isbotaccount == False:
    driver.get("https://jklm.fun")
    driver.execute_script(f'auth = {jklmSettings}')
    driver.execute_script('localStorage.setItem("jklmSettings", JSON.stringify(auth))')
    driver.get("https://jklm.fun/" + roomcode)

if isbotaccount == True: 
    driver.get("https://jklm.fun/" + roomcode)
    time.sleep(1)
    name = driver.find_element_by_xpath("/html/body/div[2]/div[3]/form/div[2]/input")
    name.click()
    name.send_keys(Keys.CONTROL, "a")
    name.send_keys(Keys.DELETE)
    name.send_keys(botname)
    name.send_keys(Keys.RETURN)

humanspeed   = [0.04, 0.05, 0.06, 0.07, 0.10, 0.12, 0.15, 0.20]
thinktimer   = [0.20, 0.25, 0.30, 0.35]
joindelay    = [0.07, 0.10, 0.20]
removekey    = [0.08, 0.09, 0.10, 0.20]
bonus        = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
typoletters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

wordlistone = open(textfile)
stringone = wordlistone.read()

# Bot
print("Note: If you want to make the bot faster, try minimizing the chrome window.")
while True:
    if keyboard.is_pressed('enter'):
        print("\n\rBot Activated!")
        while not keyboard.is_pressed('delete'):
            while True:
                try:
                    driver.switch_to.frame(driver.find_element_by_xpath("//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))
                except:
                    break

            while True:
                try:
                    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/button").click()
                except:
                    break

            try:
                if not driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
                    #syllable = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div").text
                    syllable = driver.find_element_by_class_name("syllable").text
                    answerBox = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
                    var = syllable

                    words = [w for w in stringone.splitlines() if var in w]

                    wgeneration_limit = 30
                    reqltr = random.choice(bonus)
                    gen = 1
                    while gen == 1:
                        try:
                            a = random.choice(words)
                        except:
                            print("Cannot choose from an empty sequence (IndexError)")
                            gen -= 1

                        if wgeneration_limit != 0:
                            if reqltr in a:
                                print(f"Word Accepted: {a}")
                                break
                            
                            if reqltr not in a:
                                wgeneration_limit -= 1
                                continue
                            
                        if wgeneration_limit == 0:
                            wgeneration_limit += 30
                            print("Word Generation reached generation limit. Stopped Generating words to avoid generating words in an endless loop.")
                            break
                    
                    answerBox.click()

                    if humanmode == False:
                        if driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input").is_displayed():
                            answerBox.send_keys(a)
                            result = "".join(dict.fromkeys(a))
                            for letter in result:
                                letters = [w for w in bonus if letter in w]
                                if letters:
                                    bonus.remove(letter)
                                if not letters:
                                    print(f"Letter '{letter}' not in list")

                        if bonus == []:
                            fillbonus = "ABCDEFGHIJKLMNOPQRSTUV"
                            for bonusfill in fillbonus:
                                bonus.append(bonusfill)
                        print("Bonus Letters Left: " + ','.join(str(x) for x in bonus)) 
                    
                    if humanmode == True:
                        if driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input").is_displayed():
                            time.sleep(random.choice(thinktimer))
                            for letters in a:
                                if createtypo == True:
                                    typo = random.randint(1, 30)
                                    
                                    if typo == 15:
                                        if not driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input").is_displayed():
                                            break

                                        presstypo = random.randint(1, 2)

                                        for i in range(presstypo):
                                            answerBox.send_keys(random.choice(typoletters))
                                            time.sleep(random.choice(humanspeed))

                                        time.sleep(0.40)

                                        for i in range(presstypo):
                                            answerBox.send_keys(Keys.BACK_SPACE)
                                            time.sleep(random.choice(removekey))

                                        answerBox.send_keys(letters)

                                    if typo != 15:
                                        answerBox.send_keys(letters)
                                        time.sleep(random.choice(humanspeed))
                                
                                if createtypo == False:
                                    answerBox.send_keys(letters)
                                    time.sleep(random.choice(humanspeed))

                            result = "".join(dict.fromkeys(a))
                            for letter in result:
                                letters = [w for w in bonus if letter in w]
                                if letters:
                                    bonus.remove(letter)
                                if not letters:
                                    print(f"Letter '{letter}' not in list")

                            if bonus == []:
                                fillbonus = "ABCDEFGHIJKLMNOPQRSTUV"
                                for bonusfill in fillbonus:
                                    bonus.append(bonusfill)
                            print("Bonus Letters Left: " + ','.join(str(x) for x in bonus)) 

                    answerBox.send_keys(Keys.RETURN)
                    time.sleep(0.90)
            except:
                pass
    
    else:
        print("\rWaiting for activation... [Press Enter to Activate Bot]", end="")
