import pyautogui
import time

# ==== SETTINGS ====
start_delay = 5        # seconds before clicking starts
num_clicks =  100     # total number of clicks
click_delay = 0.3     # delay between clicks in seconds
# ===================

print(f"Waiting {start_delay} seconds... Place your cursor where you want the clicks.")
time.sleep(start_delay)

for i in range(num_clicks):
    # pyautogui.press("space")
    pyautogui.click()
    print(f"Clicked {i+1}/{num_clicks}")
    time.sleep(click_delay)

print("Done clicking!")
                                                  