"""
Телефонный справочник с внешним хранилищем информации, дополнить функционалом добавления информации, удаления и редактирования.
"""


import shelve
class PhoneBook:
    def __init__(self, nameBook, dicRec={}):
        self.nameBook = nameBook
        self.dicRec = dicRec
    def loadBook(self):
        db = shelve.open(self.nameBook)
        self.dicRec = dict(db.items())
        db.close()
    def saveBook(self):
        db = shelve.open(self.nameBook)
        for (key, record) in self.dicRec.items():
            db[key] = record
        db.close()
 
    def createRec(self):
        print(self.nameBook)
        label = input('название записи: ')
        phone = input('телефон : ')
        print('ФИО,коммент. - Если нет, просто нажимайте Enter')
        familyName = input('ФИО: ')
        comment = input('Комментарий: ')
        if len(self.dicRec)>0:
            L = sorted(self.dicRec.items(), key=lambda item: item[0])
            keyRec = str(int(L[-1][0]) + 1)
        else:
            keyRec = "1"
        record = PhoneRec(keyRec, label, phone, familyName, comment)
        self.dicRec[keyRec] = record
    def delPhoneRec(self, key):
        del dicRec[key]
    def readPhoneRec(self):
        for key in t1.dicRec.keys():
            print("{:<3}- {:<25}- {:<20}- {:<30}- {:<30}".format(key, t1.dicRec[key].label, 
                                                                            t1.dicRec[key].phone, 
                                                                            t1.dicRec[key].familyName,  
                                                                            t1.dicRec[key].comment))
class PhoneRec:
    def __init__(self, keyRec, label, phone, familyName, comment):
        self.keyRec = keyRec
        self.label = label
        self.phone = phone
        self.familyName = familyName
        self.comment = comment
 
if __name__ == '__main__':
    t1 = PhoneBook("Телефоны")
    t1.loadBook()
    t1.createRec()
    t1.readPhoneRec()
 
    t1.saveBook()


    -----------------------------------------------------------------------------------------------------------------


    from tkinter import *
import shelve
 
class PhoneBook:
    def __init__(self, nameBook, dicRec={}):
        self.nameBook = nameBook
        self.dicRec = dicRec
    def loadBook(self):
        db = shelve.open(self.nameBook)
        self.dicRec = dict(db.items())
        db.close()
    def saveBook(self):
        db = shelve.open(self.nameBook)
        for (key, record) in self.dicRec.items():
            db[key] = record
        db.close()
 
class PhoneRec:
    def __init__(self, keyRec, char, label, phone, familyName, comment, delR=''):
        self.keyRec = keyRec
        self.char = char
        self.label = label
        self.phone = phone
        self.familyName = familyName
        self.comment = comment
        self.delR = delR
 
fieldnamesRec = ('keyRec', 'char', 'label', 'phone', 'familyName', 'comment', 'delR')
activCh = 'А'
 
def makeWidgets():
    global entriesRec, entRec
    window = Tk()
    window.title('Телефонны')
    window.geometry('1260x600+0+0')
    form1 = Frame(window)
    form1.pack()
    alph = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", 
            "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Э", "Ю", "Я"]
    for i in range(len(alph)):
        Button(form1, text=alph[i], command=(lambda x=alph[i]: fetch(x))).pack(side=LEFT)
    entFind = Entry(form1, width=27).pack(side=LEFT)
    Button(form1, text="Поиск", command=fetchFind).pack(side=LEFT)
 
    form2 = Frame(window)
    form2.pack()
    entriesRec = {}
    entRec = {}
    for (ix, label) in enumerate(fieldnamesRec):
        lab = Label(form2, text=label)
        lab.grid(row=2, column=ix)
    for i in range(1, 26):
        for (ix, label) in enumerate(fieldnamesRec):
            if label == 'keyRec' or label == 'char' or label == 'delR':
                ent = Entry(form2, state='normal', width=6)
            else:
                ent = Entry(form2, width=40)
            ent.grid(row=i+2, column=ix)
            entriesRec[label+str(i)] = ent
    Button(window, text="Сохранить", command=saveRec).pack(side=LEFT)
    labKeyRec = Label(window, text='keyRec').pack(side=LEFT)
    ent = Entry(window, width=10)
    ent.pack(side=LEFT)
    entRec['entKeyRec'] = ent
    Button(window, text="Удалить", command=delKeyRec).pack(side=LEFT)
    Button(window, text="Выход", command=lambda :window.destroy()).pack(side=RIGHT)
    return window
 
def clear_sheet():
    for i in range(1, 26):
        for field in fieldnamesRec:
            if field == 'keyRec' or field == 'delR':
                entriesRec[field+str(i)].config(state='normal')
                entriesRec[field+str(i)].delete(0, END)
                entriesRec[field+str(i)].config(state='readonly')
            else:
                entriesRec[field+str(i)].delete(0, END)
def fetch(ch):
    global activCh
    clear_sheet()
    activCh = ch
    count = 1
    dicRe = t1.dicRec.copy()
    while count <= 25 and len(dicRe):
        for key in t1.dicRec.keys():
            if t1.dicRec[key].char == ch: #and t1.dicRec[key].delR=='':
                record = t1.dicRec[key]
                for field in fieldnamesRec:
                    if field == 'keyRec' or field == 'delR':
                        entriesRec[field+str(count)].config(state='normal')
                        entriesRec[field+str(count)].insert(0, getattr(record, field))
                        entriesRec[field+str(count)].config(state='readonly')
                    else:
                        entriesRec[field+str(count)].insert(0, getattr(record, field))
                count += 1
                dicRe.pop(key)
                if count > 25:
                    break
            else:
                dicRe.pop(key)
    return dicRe
 
def delKeyRec():
    # физическое удаление из базы данных
    key = entRec['entKeyRec'].get()
    del t1.dicRec[key]
    db = shelve.open(t1.nameBook)
    del db[key]
    db.close()
    for i in range(1, 26):
        if entriesRec['keyRec'+str(i)].get() == key:
            entriesRec['delR'+str(i)].config(state='normal')
            entriesRec['delR'+str(i)].insert(0, 'у')
            entriesRec['delR'+str(i)].config(state='readonly')
    entRec['entKeyRec'].delete(0, END)
    # пометить как удаленную
#    key = entRec['entKeyRec'].get()
#    record = t1.dicRec[key]
#    setattr(record, 'delR', 'у')
#    print(t1.dicRec[key].delR)
#    entRec['entKeyRec'].delete(0, END)
def fetchFind():
    pass
def saveRec():
    for i in range(1, 26):
        key = entriesRec['keyRec'+str(i)].get()
        if entriesRec['delR'+str(i)].get() == 'у':
            continue
        elif key:
            record = t1.dicRec[key]
            for field in fieldnamesRec:
                setattr(record, field, entriesRec[field+str(i)].get())
            t1.dicRec[key] = record
        else:
            existRec = False
            for field in fieldnamesRec:
                if entriesRec[field+str(i)].get(): existRec = True # Если существует запись в поле на этой строке
            if existRec:
                if entriesRec['char'+str(i)].get():
                    char = entriesRec['char'+str(i)].get()
                else:
                    char = activCh
                label = entriesRec['label'+str(i)].get()
                phone = entriesRec['phone'+str(i)].get()
                familyName = entriesRec['familyName'+str(i)].get()
                comment = entriesRec['comment'+str(i)].get()
                if len(t1.dicRec)>0:
                    L = sorted(t1.dicRec.items(), key=lambda item: int(item[0]))
                    keyRec = str(int(L[-1][0]) + 1)
                else:
                    keyRec = "1"
                record = PhoneRec(keyRec, char, label, phone, familyName, comment)
                t1.dicRec[keyRec] = record
    t1.saveBook()
    fetch(activCh)
 
if __name__ == '__main__':
 
    t1 = PhoneBook("Телефоны")
    t1.loadBook()
 
    window = makeWidgets()
    window.mainloop()


    -----------------------------------------------------------------------------------------------------------------

    from tkinter import *
import shelve
 
class PhoneBook:
    def __init__(self, nameBook, dicRec={}):
        self.nameBook = nameBook
        self.dicRec = dicRec
    def loadBook(self):
        db = shelve.open(self.nameBook)
        self.dicRec = dict(db.items())
        db.close()
    def saveBook(self):
        db = shelve.open(self.nameBook)
        for (key, record) in self.dicRec.items():
            db[key] = record
        db.close()
 
class PhoneRec:
    def __init__(self, keyRec, char, label, phone, familyName, comment, delR=''):
        self.keyRec = keyRec
        self.char = char
        self.label = label
        self.phone = phone
        self.familyName = familyName
        self.comment = comment
        self.delR = delR
 
fieldnamesRec = ('keyRec', 'char', 'label', 'phone', 'familyName', 'comment', 'delR')
activCh = 'А'
 
def makeWidgets():
    global entriesRec, entRec
    entRec = {}
    window = Tk()
    window.title('Телефонны')
    window.geometry('1260x600+0+0')
    form1 = Frame(window)
    form1.pack()
    alph = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", 
            "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Э", "Ю", "Я"]
    for i in range(len(alph)):
        Button(form1, text=alph[i], command=(lambda x=alph[i]: fetch(x))).pack(side=LEFT)
    ent = Entry(form1, width=27)
    ent.pack(side=LEFT)
    entRec['entFind'] = ent
    Button(form1, text="Поиск", command=fetchFind).pack(side=LEFT)
 
    form2 = Frame(window)
    form2.pack()
    entriesRec = {}
    for (ix, label) in enumerate(fieldnamesRec):
        lab = Label(form2, text=label)
        lab.grid(row=2, column=ix)
    for i in range(1, 26):
        for (ix, label) in enumerate(fieldnamesRec):
            if label == 'keyRec' or label == 'char' or label == 'delR':
                ent = Entry(form2, state='normal', width=6)
            else:
                ent = Entry(form2, width=40)
            ent.grid(row=i+2, column=ix)
            entriesRec[label+str(i)] = ent
    Button(window, text="Сохранить", command=saveRec).pack(side=LEFT)
    labKeyRec = Label(window, text='keyRec').pack(side=LEFT)
    ent = Entry(window, width=10)
    ent.pack(side=LEFT)
    entRec['entKeyRec'] = ent
    Button(window, text="Удалить", command=delKeyRec).pack(side=LEFT)
    Button(window, text="Выход", command=lambda :window.destroy()).pack(side=RIGHT)
    return window
 
def clear_sheet():
    for i in range(1, 26):
        for field in fieldnamesRec:
            if field == 'keyRec' or field == 'delR':
                entriesRec[field+str(i)].config(state='normal')
                entriesRec[field+str(i)].delete(0, END)
                entriesRec[field+str(i)].config(state='readonly')
            else:
                entriesRec[field+str(i)].delete(0, END)
def fetch(ch):
    global activCh
    clear_sheet()
    activCh = ch
    count = 1
    dicRe = t1.dicRec.copy()
    while count <= 25 and len(dicRe):
        for key in t1.dicRec.keys():
            if t1.dicRec[key].char == ch: #and t1.dicRec[key].delR=='':
                record = t1.dicRec[key]
                for field in fieldnamesRec:
                    if field == 'keyRec' or field == 'delR':
                        entriesRec[field+str(count)].config(state='normal')
                        entriesRec[field+str(count)].insert(0, getattr(record, field))
                        entriesRec[field+str(count)].config(state='readonly')
                    else:
                        entriesRec[field+str(count)].insert(0, getattr(record, field))
                count += 1
                dicRe.pop(key)
                if count > 25:
                    break
            else:
                dicRe.pop(key)
    return dicRe
 
def delKeyRec():
    # физическое удаление из базы данных
    key = entRec['entKeyRec'].get()
    del t1.dicRec[key]
    db = shelve.open(t1.nameBook)
    del db[key]
    db.close()
    for i in range(1, 26):
        if entriesRec['keyRec'+str(i)].get() == key:
            entriesRec['delR'+str(i)].config(state='normal')
            entriesRec['delR'+str(i)].insert(0, 'у')
            entriesRec['delR'+str(i)].config(state='readonly')
    entRec['entKeyRec'].delete(0, END)
    # пометить как удаленную
#    key = entRec['entKeyRec'].get()
#    record = t1.dicRec[key]
#    setattr(record, 'delR', 'у')
#    print(t1.dicRec[key].delR)
#    entRec['entKeyRec'].delete(0, END)
def fetchFind():
    clear_sheet()
    strF = entRec['entFind'].get()
    dicFind = {}
    for key in t1.dicRec.keys():
        record = t1.dicRec[key]
        for field in fieldnamesRec:
            if (field != 'keyRec' and field != 'char' and field != 'delR' and 
                getattr(record, field).find(strF) != -1):
                dicFind[key] = record
                break
    count = 1
    dicRe = dicFind.copy()
    while count <= 25 and len(dicRe):
        for key in dicFind.keys():
            record = dicFind[key]
            for field in fieldnamesRec:
                if field == 'keyRec' or field == 'delR':
                    entriesRec[field+str(count)].config(state='normal')
                    entriesRec[field+str(count)].insert(0, getattr(record, field))
                    entriesRec[field+str(count)].config(state='readonly')
                else:
                    entriesRec[field+str(count)].insert(0, getattr(record, field))
            count += 1
            dicRe.pop(key)
            if count > 25:
                break
    return dicRe
 
def saveRec():
    for i in range(1, 26):
        key = entriesRec['keyRec'+str(i)].get()
        if entriesRec['delR'+str(i)].get() == 'у':
            continue
        elif key:
            record = t1.dicRec[key]
            for field in fieldnamesRec:
                setattr(record, field, entriesRec[field+str(i)].get())
            t1.dicRec[key] = record
        else:
            existRec = False
            for field in fieldnamesRec:
                if entriesRec[field+str(i)].get(): existRec = True # Если существует запись в поле на этой строке
            if existRec:
                if entriesRec['char'+str(i)].get():
                    char = entriesRec['char'+str(i)].get()
                else:
                    char = activCh
                label = entriesRec['label'+str(i)].get()
                phone = entriesRec['phone'+str(i)].get()
                familyName = entriesRec['familyName'+str(i)].get()
                comment = entriesRec['comment'+str(i)].get()
                if len(t1.dicRec)>0:
                    L = sorted(t1.dicRec.items(), key=lambda item: int(item[0]))
                    keyRec = str(int(L[-1][0]) + 1)
                else:
                    keyRec = "1"
                record = PhoneRec(keyRec, char, label, phone, familyName, comment)
                t1.dicRec[keyRec] = record
    t1.saveBook()
    fetch(activCh)
 
if __name__ == '__main__':
 
    t1 = PhoneBook("Телефоны")
    t1.loadBook()
 
    window = makeWidgets()
    window.mainloop()



    