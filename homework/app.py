import pyautogui
def appopen():

    x=int(input(""))

    if x==1:
        pyautogui.hotkey('win','r')
        pyautogui.write('C:\Users\Admin\Desktop\Canva.lnk')
        pyautogui.press('enter')




appopen()