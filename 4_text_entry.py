from tkinter import *

root = Tk()
root.title("han GUI")

txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, "글자를 입력하세요")



e = Entry(root, width = 30)
e.insert(0,"한줄만 가능")
e.pack()


def btncmd():
    print(txt.get("1.0", END)) #1은 첫번째 라인, 0은 0번째 컬럼 위치
    print(e.get())

    #삭제
    txt.delete("1.0" , END)
    e.delete(0, END)

btn = Button(root, text= "클릭", command = btncmd)
btn.pack()


root.mainloop()