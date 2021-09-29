from ppadb.client import Client
import pyautogui
import time

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


take_screenshot(device)

main1_area = [247,1294,395,146]
main2_area = [290,1446,320,109]
retry_area = [469,1447,317,106]
rankup_area = [187,686,530,167]
gameover_area = [89,997,735,405]

def start():
    while True:
        take_screenshot(device)
        start = pyautogui.locate(get_img('start.png'), get_img('screen.png'), region=main1_area, confidence=0.8)
        if start != None:
            device.shell('input tap {0} {1}'.format(pyautogui.center(start)[0], pyautogui.center(start)[1]))
            break

    print('Start Battle')

def next():
    while True:
        take_screenshot(device)
        #if abort():
        #    continue

        if rankup():
            continue

        next = pyautogui.locate(get_img('next.png'), get_img('screen.png'), region=main2_area, confidence=0.8)
        if next != None:
            device.shell('input tap {0} {1}'.format(pyautogui.center(next)[0], pyautogui.center(next)[1]))
            break
    print('Next')

def ok():
    while True:
        take_screenshot(device)
        ok = pyautogui.locate(get_img('ok.png'), get_img('screen.png'), region=main2_area, confidence=0.8)
        if ok != None:
            device.shell('input tap {0} {1}'.format(pyautogui.center(ok)[0], pyautogui.center(ok)[1]))
            break
    print('Ok')

def retry():
    while True:
        take_screenshot(device)
        retry = pyautogui.locate(get_img('retry.png'), get_img('screen.png'), region=retry_area, confidence=0.8)
        if retry != None:
            device.shell('input tap {0} {1}'.format(pyautogui.center(retry)[0], pyautogui.center(retry)[1]))
            break
    print('Retry Battle')

def rankup():
    rankup = pyautogui.locate(get_img('rankup.png'), get_img('screen.png'), region=rankup_area, confidence=0.8)
    if rankup != None:
        device.shell('input tap {0} {1}'.format(pyautogui.center(rankup)[0], pyautogui.center(rankup)[1]))
        return True
    else:
        return False

def abort():
    abort = pyautogui.locate(get_img('abort.png'), get_img('screen.png'), region=gameover_area, confidence=0.8)
    if rankup != None:
        device.shell('input tap {0} {1}'.format(pyautogui.center(rankup)[0], pyautogui.center(rankup)[1]))
        time.sleep(0.5)
        ok()
        return True
    else:
        return False


def auto_farm(count):
    print('Auto Farm Starts for {} times'.format(count))
    print('==================')
    for i in range(count):
        print('Battle Number',i+1)
        start()
        next()
        #time.sleep(2)
        #next()
        retry()
        print('==================')
    print('Auto Farm Finished')

def auto_battle():
    print('Auto Battle Started')
    print('==================')
    while True:
        start()
        next()
        time.sleep(2)
        next()
        ok()
        print('==================')


#ToStart
#auto_battle()
auto_farm(81//14)
