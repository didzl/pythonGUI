from tkinter import *

root = Tk()
root.title("han GUI")


chkvar = IntVar() #chkvar에 int형으로 값을 저장
chkbx = Checkbutton(root, text = "오늘 하루 보지 않기" , variable = chkvar)
#chkbx.select() #선택된 처리
#chkbx.deselect() #선택 해제
chkbx.pack()


chkvar2 = IntVar()
chkbx2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbx2.pack()





def btncmd():
    print(chkvar.get()) #0: 체크 해제, 1: 체크 
    print(chkvar2.get())

    

btn = Button(root, text= "클릭", command = btncmd)
btn.pack()


root.mainloop()