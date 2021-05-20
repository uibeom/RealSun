import tkinter
import tkinter.ttk
window=tkinter.Tk()

window.title("안심식당")
window.geometry("700x700+300+100")  #너비 x 높이  + 시작x + 시작y
window.resizable(True, True)

#목록1 -> 검색결과 리스트 박스
frame = tkinter.Frame(window)

scrollbar=tkinter.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tkinter.Listbox(frame, selectmode='extended', width= 42, height=25,yscrollcommand = scrollbar.set)
for line in range(1,1001):
   listbox.insert(line, str(line) + "/1000")
listbox.pack(side="left")

scrollbar["command"]=listbox.yview
frame.place(x=30, y=250)
#///
frame2 = tkinter.Frame(window)

scrollbar2=tkinter.Scrollbar(frame2)
scrollbar2.pack(side="right", fill="y")

listbox2 = tkinter.Listbox(frame2, selectmode='extended', width= 42, height=25,yscrollcommand = scrollbar2.set)
for line in range(1,1001):
   listbox2.insert(line, str(line) + "/1000")
listbox2.pack(side="left")

scrollbar2["command"]=listbox2.yview
frame2.place(x=360, y=250)
#-------------------------------------
#콤보박스 -검색필터 3개


values= ['서울특별시','부산광역시','대구광역시','광주광역시', '대전광역시','인천광역시','울산광역시',
               '세종특별자치시','경기도','강원도','충청북도','충청남도','전라북도','전라남도',
               '경상북도', '경상남도','제주특별자치도']
combo1 = tkinter.ttk.Combobox(window, width=30, height = 50, values=values)
combo1.place(x=50, y = 130)
combo1.set("목록 선택")








#----------------------
def search():
    pass
def reset():
    pass
def recommand():
    pass
def mail():
    pass
def map():
    pass
#버튼
#검색버튼
button = tkinter.Button(window, text = '검색', command = search, width=10, height = 1, borderwidth= 5, )
button.place(x=430,y=50)
#초기화 버튼
button2 = tkinter.Button(window, text = '초기화', command = reset, width=8, height = 1, borderwidth= 5, )
button2.place(x=530,y=50)
#추천메뉴 버튼
button3 = tkinter.Button(window, text = '추천메뉴', command = recommand, width=30, height = 1, borderwidth= 5, )
button3.place(x=80,y=190)
#메일 버튼
button4 = tkinter.Button(window, text = '메일', command = mail, width=10, height = 1, borderwidth= 5, )
button4.place(x=370,y=190)
#지도 버튼
button5 = tkinter.Button(window, text = '지도', command = map, width=10, height = 1, borderwidth= 5, )
button5.place(x=470,y=190)



#입력창
entry=tkinter.Entry(window, width = 50, borderwidth= 3, bg = 'light blue')
entry.place(x=50,y=60)

window.mainloop()