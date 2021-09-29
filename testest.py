from ppadb.client import Client
import pyautogui


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]
#print(device)

def get_img(filename, dir='images/'):
    return dir + filename

def take_screenshot(device):
    image = device.screencap()
    #image = device.shell("screencap -p | sed 's/\r$//' > screen.png")
    with open(get_img('screen.png'), 'wb') as f:
        f.write(image)

#main_button_area = [247,1294,395,146]
#rankup_area = [187,686,530,167]
#gameover_area = [89,997,735,405]
take_screenshot(device)
img = pyautogui.locate(get_img('ok.png'), get_img('screen.png'), confidence=0.8)

print('Area:',img)
#print('Count:',len(img))
#print('Center:',pyautogui.center(img))