__author__ = 'a1'
import time
import subprocess
import uiautomation as automation

def menuOperation(redWindow):


    menuMulItems = [u'历史记录(H)',u'书签(B)',u'更多工具(L)',u'退出(X) Ctrl+Shift+Q']
    bookmarker = [u'为此网页添加书签… Ctrl+D',u'显示书签栏(S) Ctrl+Shift+B',u'书签管理器(B) Ctrl+Shift+O',u'导入书签和设置...']
    moretools= [u'网页另存为(A)... Ctrl+S',u'清除浏览数据(C)... Ctrl+Shift+Del',u'任务管理器(T) Shift+Esc',u'开发者工具(D) Ctrl+Shift+I']
   # moretools= [u'任务管理器(T) Shift+Esc']

    for chindMenu in menuMulItems:
        time.sleep(1)

        if chindMenu == u'历史记录(H)':
            redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
            time.sleep(1)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
            searchEdit.Click()
            time.sleep(2)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == u'历史记录(H) Ctrl+H')#操作二级菜单
            searchEdit.Click()
            time.sleep(3)
        if chindMenu == u'书签(B)':
            for index in range(len(bookmarker)):
                if bookmarker[index] == u'导入书签和设置...':

                    redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
                    time.sleep(1)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
                    searchEdit.Click()
                    #searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == bookmarker[0]) #操作二级菜单… Ctrl+D
                    redWindow.MoveCursor(ratioY=0.2,ratioX=0.7)
                    time.sleep(2)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == bookmarker[index]) #操作二级菜单… Ctrl+D
                    searchEdit.Click()
                    time.sleep(2)
                    redWindow.SendKeys('{esc}')

                else:
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.EditControl) and c.Name == u'地址和搜索栏'))
                    searchEdit.Click()
                    searchEdit.SendKeys('www.redcore.cn{Enter}',0.05)
                    time.sleep(2)
                    redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
                    time.sleep(1)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu) #操作一级菜单
                    searchEdit.Click()
                    time.sleep(2)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == bookmarker[0]) #操作二级菜单… Ctrl+D
                    redWindow.MoveCursor(ratioY=0.2,ratioX=0.7)
                    #searchEdit.MoveMoveCursor()
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == bookmarker[index]) #操作二级菜单… Ctrl+D
                    searchEdit.Click()
                    time.sleep(2)
                    redWindow.SendKeys('{Enter}')
                print("书签：" +moretools[index])
        if chindMenu == u'更多工具(L)':
            for index in range(len(moretools)):
                if moretools[index] == u'网页另存为(A)... Ctrl+S':
                    redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
                    time.sleep(1)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
                    searchEdit.Click()
                    time.sleep(2)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == moretools[index])#操作二级菜单
                    searchEdit.Click()
                    time.sleep(2)
                    #另存为窗口处理
                    parentdWindow = automation.WindowControl(searchDepth = 1, ClassName = 'Chrome_WidgetWin_1')
                    saveas = parentdWindow.WindowControl(searchDepth=3,searchWaitTime=10,name=u'另存为')
                    saveas.MoveToCenter()
                    print(saveas)
                    time.sleep(1)
                    button = saveas.ButtonControl(searchDepth=1,searchWaitTime=10,AutomationId='2')
                    print(button)
                    button.Click()
                    time.sleep(1)
                elif moretools[index] == u'任务管理器(T) Shift+Esc':
                    redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
                    time.sleep(1)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
                    searchEdit.Click()
                    time.sleep(2)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == moretools[index])#操作二级菜单
                    searchEdit.Click()
                    time.sleep(2)
                    taskWindow = automation.WindowControl(name = u'任务管理器 - 红芯企业浏览器',searchDepth = 1 ,ClassName = 'Chrome_WidgetWin_1')
                    closeButton = taskWindow.ButtonControl(searchDepth=2,Name=u'关闭')
                    closeButton.Click()
                else:
                    redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
                    time.sleep(1)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
                    searchEdit.Click()
                    time.sleep(2)
                    searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == moretools[index])#操作二级菜单
                    searchEdit.Click()
                    time.sleep(2)
                    redWindow.SendKeys('{esc}')
                   # searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == u'保存(S)')
                    #searchEdit.Click()
                   # redWindow.SendKeys('{Esc}')

                    time.sleep(2)
                print("更多工具" +moretools[index])

        print("多级菜单循环数据 " + chindMenu)
    else:
        print("没有循环数据!")
    print("多级菜单完成循环!")


    '''
    操作浏览器菜单， menuSingleItems包含的项，只操作没有下级菜单的选项
    Operation redcore browser mainMenu， only include Level 1 menus
    '''

    menuSingleItems = [u'打开新的标签页(T)',u'下载内容(D) Ctrl+J',u'查找(F)... Ctrl+F',u'设置(S)',u'关于 红芯企业浏览器(C)',u'打印(P)... Ctrl+P',u'打开新的窗口(N) Ctrl+N',u'退出(X) Ctrl+Shift+Q'] #,u'退出(X) Ctrl+Shift+Q'

    for chindMenu in menuSingleItems:
        time.sleep(1)

        if chindMenu == u'打印(P)... Ctrl+P1':
            redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
            time.sleep(1)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
            searchEdit.Click()
            time.sleep(3)
            redWindow.SendKeys('{Esc}')

        elif chindMenu == u'打开新的窗口(N) Ctrl+N':
            redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
            time.sleep(1)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
            searchEdit.Click()
            time.sleep(2)
            redWindow.SendKeys('{Alt}{F4}')

        elif chindMenu == u'退出(X) Ctrl+Shift+Q':
            redWindow = automation.WindowControl(searchDepth = 1, ClassName = 'Chrome_WidgetWin_1') #取浏览器handle
            redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
            time.sleep(1)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
            searchEdit.Click()
            time.sleep(2)

        else :

            redWindow.MenuItemControl(searchDepth=5,searchWaitTime=10,foundIndex = 2,name=u'红芯企业浏览器').Click()
            time.sleep(1)
            searchEdit = automation.FindControl(redWindow,lambda c, d: (isinstance(c, automation.MenuItemControl) or isinstance(c, automation.MenuControl)) and c.Name == chindMenu)
            searchEdit.Click()

        print("一级菜单循环数据 " + chindMenu)
    else:
        print("没有循环数据!")
    print("一级菜单完成循环!")


