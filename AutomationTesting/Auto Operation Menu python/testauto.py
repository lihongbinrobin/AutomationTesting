__author__ = 'a1'
import subprocess
import uiautomation as automation
import time
import MenuOperation

def main():
    subprocess.Popen('redcore.exe') #启动浏览器
    time.sleep(1)
    redWindow = automation.WindowControl(searchDepth = 1, ClassName = 'Chrome_WidgetWin_1') #取浏览器handle
    if not redWindow.Exists(0):
        automation.Logger.WriteLine('未找到红芯浏览器，请重试！',automation.ConsoleColor.Yellow)
        return
    redWindow.ShowWindow(automation.ShowWindow.Maximize)   #最大化浏览器
    redWindow.SetActive()
    time.sleep(1)

    MenuOperation.menuOperation(redWindow)   #操作浏览器菜单


if __name__ == '__main__':
    main()
    input('全部运行完成')
