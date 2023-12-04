import pyautogui as pg
from PIL import ImageGrab
import time
from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--window-size=1200x600')  # Adjust the window size as needed

# driver = webdriver.Chrome(options=chrome_options)

def isCollide(data):
    # Background
    background = None
    for i in range(830, 870):
        for j in range(200, 250):
            background = data[i, j]

    # Cactus
    for i in range(450, 620):
        for j in range(670, 700):
            if (background > 200 and data[i, j] < 90) or (background < 126 and data[i, j] > 100):
                pg.keyDown('up')
                return

    # Bird
    for i in range(400, 550):
        for j in range(500, 575):
            if (background > 200 and data[i, j] < 90) or (background < 126 and data[i, j] > 100):
                pg.keyDown('down')
                time.sleep(0.2)
                pg.keyUp('down')
                return
    return


if __name__ == '__main__':
    print("Hey dino Game is about to start in 3 seconds")
    # driver.get("chrome://dino/")
    time.sleep(3)
    print('started')
    pg.press('up')
    while True:
        image = ImageGrab.grab().convert('L')  # Taking Screenshot
        data = image.load()
        isCollide(data)
    # driver.quit()
        # # Background
        # for i in range(350, 550):
        #     for j in range(830, 870):
        #         data[i, j] = 170

        # # Cactus
        # for i in range(400, 550):
        #     for j in range(670, 700):
        #         data[i, j] = 80

        # # Bird
        # for i in range(350, 500):
        #     for j in range(500, 570):
        #         data[i, j] = 100

        # image.show()
        # break
