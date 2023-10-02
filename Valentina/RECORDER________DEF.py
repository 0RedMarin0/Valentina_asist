import cv2
import numpy as np
import pyautogui
import mouseinfo
import pyscreeze
from PIL import ImageGrab
'''
SCREEN_SIZE = (1920, 1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

out = cv2.VideoWriter("output.avi", fourcc, 15.0, (SCREEN_SIZE))

while True:
    img = ImageGrab.grab()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    print(img)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()
'''
#im = ImageGrab.grab()
#im.save("pill.tiff")

with open("rgb_size.txt", "w") as file:
    arr = []
    for y in range(10):
        for x in range(19):
            rgb = ImageGrab.grab().load()[x, y]
            arr.extend([list(rgb)])
    print(arr)
    file.write(f"{arr}")

