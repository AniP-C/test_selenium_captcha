from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome()
driver.get("https://anip-c.github.io/test_selenium_captcha/")



# Enterign username
user_name = driver.find_element(By.ID, "username")
user_name.send_keys("AniPy")
time.sleep(3)
# Emtering password
pass_word = driver.find_element(By.ID, "password")
pass_word.send_keys("password")
time.sleep(3)

# Finding element in of captcha

captcha_text = driver.find_element(By.ID,"captchaLabel").text

# now spilit the text 
equation = captcha_text.replace("What is", "").replace("?", "").strip()

spillting_captcha = equation.split(" ")

num1 = int(spillting_captcha[0])
opertr = spillting_captcha[1]
num2 = int(spillting_captcha[2])
res = 0

if opertr == "+":
    res = num1 + num2
elif opertr == "-":
    res = num1 - num2
else:
    res = num1 * num2

time.sleep(3)
# Finding captcha response box 
captcha_ans_insert = driver.find_element(By.ID,"captchaResponse")

captcha_ans_insert.send_keys(res)
time.sleep(2)
# cliclimg on login
login_btn = driver.find_element(By.XPATH,'//*[@id="loginForm"]/button')
login_btn.click()


# validating success message
success_text = driver.find_element(By.ID,"successMsg").text
failuer_text = driver.find_element(By.ID,"errorMsg").text


if success_text:
    assert "Login successful! (CAPTCHA passed)" in success_text , "Success hooray"
elif failuer_text:
    assert "CAPTCHA is incorrect. Please try again." in failuer_text, "Wrong captcha enter again"
else:
    print("captcha to daal dalle")

print(spillting_captcha)
# print(captcha_text.text)
print(num1,opertr,num1)
time.sleep(3)