# from pynput import mouse

# file_path = "clicks.txt"
# max_clicks = 64
# click_count = 0

# def on_click(x, y, button, pressed):
#     global click_count
#     if pressed:
#         click_count += 1
#         coord = f"{x}, {y}\n"
#         print(f"[{click_count}] Mouse clicked at ({x}, {y})")

#         # Save to file
#         with open(file_path, "a") as f:
#             f.write(coord)

#         # Stop after 64 clicks
#         if click_count >= max_clicks:
#             print(f"✅ Recorded {max_clicks} clicks. Saved in {file_path}")
#             return False  # stops the listener

# with mouse.Listener(on_click=on_click) as listener:
#     listener.join()



import pyautogui
import time

# Load coordinates from file
file_path = "clicks.txt"
with open(file_path, "r") as f:
    coords = [line.strip().split(",") for line in f]

# Convert to integers
coords = [(int(x), int(y)) for x, y in coords]

print(f"Replaying {len(coords)} clicks...")

time.sleep(5)  # small delay so you can switch to target window

for (x, y) in coords:
    pyautogui.click(x, y)
    time.sleep(0.001)  # delay between clicks (adjust as needed)

print("✅ Done replaying clicks.")
