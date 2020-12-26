from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("han GUI")
root.geometry("640x480")


#모드에 차이가 있음
#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
# progressbar.start(10) #10ms마다 움직임
# progressbar.pack()




# def btncmd():
#     progressbar.stop()
    

# btn = Button(root, text= "스톱", command = btncmd)
# btn.pack()




p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): #1~100
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() #ui 업데이트
        print(p_var2.get())

btn = Button(root, text= "시작", command = btncmd2)
btn.pack()



root.mainloop()