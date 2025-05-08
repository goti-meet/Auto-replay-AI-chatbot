import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(api_key="sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop") #Api keys was deleted so not working

# Give time to switch to the screen you want to work on
time.sleep(3)

# Step 1: Click the icon
pyautogui.click(1206, 1040)
time.sleep(1)  # Allow time for any UI response

# Step 2: Drag to select text
pyautogui.moveTo(706 ,216)
pyautogui.mouseDown()
pyautogui.moveTo(1883, 910, duration=1.0)
pyautogui.mouseUp()

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # Allow clipboard to update
pyautogui.click(1883, 909)

# Step 4: Store text in variable
copied_text = pyperclip.paste()

print(copied_text)

 
response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[ 
            {"role": "system", "content": "You are a persone name MEET GOTI who speake hindi as well as english . you are indian and my friend. you analyze chat history  and respone like MEET GOTI. you respone as MEET GOTI "}, 

        {"role": "user", "content": copied_text}
    ]
)
responsee = response.choices[0].message.content 

pyperclip.copy(responsee)

# Step 5: Click and press Enter
pyautogui.click(1042, 970)
time.sleep(1)

pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

pyautogui.press('enter')
