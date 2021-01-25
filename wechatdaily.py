import lackey
from WindowMgr import *


# turn on the monitor
win32gui.SendMessage(win32con.HWND_BROADCAST,
                     win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)

lackey.sleep(1)

lackey.Keyboard().keyDown(lackey.Key.PRINTSCREEN)
lackey.Keyboard().keyUp(lackey.Key.PRINTSCREEN)

# call the wechat window to foreground
w = WindowMgr()
w.find_window("WeChatMainWndForPC","微信")
w.set_foreground()

lackey.Keyboard().keyDown(lackey.Key.PRINTSCREEN)
lackey.Keyboard().keyUp(lackey.Key.PRINTSCREEN)

lackey.sleep(1)
lackey.click(r"D:\Code\DAD\image\chat.jpg")
lackey.Mouse().move(60, 0)
lackey.sleep(1)
lackey.Mouse().wheel(1, 200)
# enter the subscription list
while True:
    try:
        lackey.click(r"D:\Code\DAD\image\subscription.jpg")
        break
    except:
        lackey.Mouse().wheel(0, 10)


lackey.Mouse().move(200, 0)
lackey.sleep(1)
lackey.Mouse().wheel(1, 100)
lackey.sleep(1)

# enter the HNU subscription
lackey.click(r"D:\Code\DAD\image\HNU.jpg")
lackey.click(r"D:\Code\DAD\image\more.jpg")
try:
    lackey.click(r"D:\Code\DAD\image\enter.jpg")
except:
    pass
lackey.click(r"D:\Code\DAD\image\func.jpg")
lackey.click(r"D:\Code\DAD\image\prevent.jpg")

lackey.sleep(5)

try:
    lackey.click(r"D:\Code\DAD\image\agree.jpg")
except:
    lackey.Keyboard().keyDown(lackey.Key.PRINTSCREEN)
    lackey.Keyboard().keyUp(lackey.Key.PRINTSCREEN)


# enter the daily attendance web page
lackey.sleep(3)

lackey.Mouse().wheel(0, 4)

# type the location
try:
    lackey.click(r"D:\Code\DAD\image\loc.jpg")
    lackey.click(r"D:\Code\DAD\image\TJ.jpg")

    while True:
        try:
            lackey.click(r"D:\Code\DAD\image\HN.jpg")
            break
        except:
            lackey.Mouse().click()

    lackey.click(r"D:\Code\DAD\image\YL.jpg")
    lackey.click(r"D:\Code\DAD\image\confirm.jpg")
except:
    pass

lackey.click(r"D:\Code\DAD\image\addr.jpg")
lackey.Keyboard().type('hndx')
lackey.Keyboard().type(lackey.Key().SPACE)

# type the temperature
lackey.sleep(1)
lackey.click(r"D:\Code\DAD\image\type.jpg")
lackey.Mouse().move(-30, 0)
lackey.Mouse().click()
lackey.Keyboard().type("{36.5}")
lackey.Mouse().move(0, 40)
lackey.Mouse().click()
lackey.Keyboard().type("{36.5}")
lackey.Mouse().wheel(0, 7)
lackey.sleep(1)
lackey.click(r"D:\Code\DAD\image\attendance.jpg")

