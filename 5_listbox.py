from tkinter import *

root = Tk()
root.title("han GUI")

listbox = Listbox(root, selectmod = "extended", height= 0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()











def btncmd():
    #listbox.delete(0)#END면 맨뒤에 항목 삭제 0이면 맨 앞항목

    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인(시작 idx, 끝 idx)
    #print("1번째부터 3까지의 항목: ", listbox.get(0,2))

    #선택된 항목 확인( 위치로 반환(순서))
    print("선택된 항목: ", listbox.curselection())

    

btn = Button(root, text= "클릭", command = btncmd)
btn.pack()


root.mainloop()