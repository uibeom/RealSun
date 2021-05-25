from tkinter import *
import tkinter.ttk
from tkinter import font

class GUI:
    sibal = "sibal"
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("안심식당")
        self.window.geometry("700x700+300+100")  #너비 x 높이  + 시작x + 시작y
        self.entry()
        self.searchValues()
        self.searchDetailValues(['시/군/구'])
        self.searchCategoryValues()
        self.button()
        self.searchList()
        self.resultList()
        self.window.mainloop()

    def entry(self):
        self.entry = tkinter.Entry(self.window, width=50, borderwidth=3, bg='light blue')
        self.entry.place(x=50, y=60)

    def searchList(self):
        #목록1 -> 검색결과 리스트 박스
        self.frame = tkinter.Frame(self.window)

        self.scrollbar=tkinter.Scrollbar(self.frame)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = tkinter.Listbox(self.frame, selectmode='extended', width= 42, height=25,yscrollcommand = self.scrollbar.set)
        for line in range(1,1001):
           self.listbox.insert(line, str(line) + "/1000")
        self.listbox.pack(side="left")

        self.scrollbar["command"]=self.listbox.yview
        self.frame.place(x=30, y=250)

    def resultList(self):
        #///
        self.frame2 = tkinter.Frame(self.window)

        self.scrollbar2=tkinter.Scrollbar(self.frame2)
        self.scrollbar2.pack(side="right", fill="y")

        self.listbox2 = tkinter.Listbox(self.frame2, selectmode='extended', width= 42, height=25,yscrollcommand = self.scrollbar2.set)
        for line in range(1,1001):
           self.listbox2.insert(line, str(line) + "/1000")
        self.listbox2.pack(side="left")

        self.scrollbar2["command"]=self.listbox2.yview
        self.frame2.place(x=360, y=250)

    def selectValues(self, event):
        self.valuesStr = self.combo1.get()
        self.searchDetailValues(self.valuesStr)

    def searchValues(self): #콤보박스 -검색필터 3개
        self.valuesStr = StringVar()
        self.valuesStr = "시/도"

        # values : 시/도
        self.values= ['서울특별시','인천광역시', '세종특별자치시', '대전광역시', '광주광역시', '대구광역시', '울산광역시', '부산광역시',
                       '경기도','강원도','충청북도','충청남도','전라북도','전라남도',
                       '경상북도', '경상남도','제주특별자치도']

        self.TempFont = font.Font(self.window, size=15, weight='bold', family='Consolas')
        self.combo1 = tkinter.ttk.Combobox( self.window, textvariable = self.valuesStr, font=self.TempFont,width = 15,height = 50, values= self.values)
        self.combo1.place(x = 50, y = 130)
        self.combo1.set(self.valuesStr)
        self.combo1.bind('<<ComboboxSelected>>', self.selectValues)

    def searchDetailValues(self, detailValues):
        self.detailValuesStr = StringVar()
        self.detailValuesStr = "시/군/구"
        if detailValues == '서울특별시':
            self.detailValues =  ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구'
                       '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
        elif detailValues == '인천광역시':
            self.detailValues = ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구']
        elif detailValues == '세종특별자치시':
            self.detailValues = ['전체 읍/면/동']
        elif detailValues == '대전광역시':
            self.detailValues = ['대덕구', '동구', '서구', '유성구', '중구']
        elif detailValues == '광주광역시':
            self.detailValues = ['광산구', '남구', '동구', '북구', '서구']
        elif detailValues == '대구광역시':
            self.detailValues = ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구']
        elif detailValues == '울산광역시':
            self.detailValues = ['남구', '동구', '북구', '울주군', '중구']
        elif detailValues == '부산광역시':
            self.detailValues = ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구',
                                 '영도구', '중구', '해운대구']
        elif detailValues == '경기도':
            self.detailValues = ['고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시',
                                    '시흥시', '안산시', '안성시', '안양시', '양주시', '여주시', '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시',
                                    '평택시', '포천시', '하남시', '화성시']
        elif detailValues == '강원도':
            self.detailValues = ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시',
                                 '태백시', '평창군', '홍천군', '화천군', '횡성군']
        elif detailValues == '충청북도':
            self.detailValues = ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천구', '청주시', '충주시']
        elif detailValues == '충청남도':
            self.detailValues = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시', '청양군',
                                 '태안군', '홍성군']
        elif detailValues == '전라북도':
            self.detailValues = ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군', '장수군', '전주시', '정읍시', '진안군']
        elif detailValues == '전라남도':
            self.detailValues = ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군', '순천시', '신안군', '여수시',
                                 '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군']
        elif detailValues == '경상북도':
            self.detailValues = ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군',
                                 '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시']
        elif detailValues == '경상남도':
            self.detailValues = ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시',
                                 '통영시', '하동군', '함안군', '함양군', '합천군']
        elif detailValues == '제주특별자치도':
            self.detailValues = ['제주시', '서귀포시']
        else:
            self.detailValues = ['시/도를 선택하세요!']

        self.combo2 = tkinter.ttk.Combobox(self.window, textvariable=self.detailValuesStr, font=self.TempFont, width=15,
                                           height=50, values=self.detailValues)
        self.combo2.place(x=250, y=130)
        self.combo2.set(self.detailValuesStr)

    def searchCategoryValues(self):
        self.categoryValuesStr = StringVar()
        self.categoryValuesStr = "업종상세"
        # categoryValues : 한식/중식/일식/양식/기타  (기타 : 베트남음식, 필리핀음식 등등 확실하게 알기 어려운 것)
        self.categoryValues = ['한식', '중식', '일식', '서양식', '기타외국식', '기타 음식점업']

        self.combo3 = tkinter.ttk.Combobox(self.window, textvariable = self.categoryValuesStr,  font=self.TempFont, width = 15, height = 50, values = self.categoryValues)
        self.combo3.place(x = 450, y=130)
        self.combo3.set(self.categoryValuesStr)








    #----------------------
    def search(self):
        pass
    def reset(self):
        pass
    def recommand(self):
        pass
    def mail(self):
        pass
    def map(self):
        pass

    def button(self):
        #버튼
        #검색버튼
        self.button = tkinter.Button(self.window, text = '검색', command = self.search, width=10, height = 1, borderwidth= 5, )
        self.button.place(x=430,y=50)
        #초기화 버튼
        self.button2 = tkinter.Button(self.window, text = '초기화', command = self.reset, width=8, height = 1, borderwidth= 5, )
        self.button2.place(x=530,y=50)
        #추천메뉴 버튼
        self.button3 = tkinter.Button(self.window, text = '추천메뉴', command = self.recommand, width=30, height = 1, borderwidth= 5, )
        self.button3.place(x=80,y=190)
        #메일 버튼
        self.button4 = tkinter.Button(self.window, text = '메일', command = self.mail, width=10, height = 1, borderwidth= 5, )
        self.button4.place(x=370,y=190)
        #지도 버튼
        self.button5 = tkinter.Button(self.window, text = '지도', command = self.map, width=10, height = 1, borderwidth= 5, )
        self.button5.place(x=470,y=190)

GUI()