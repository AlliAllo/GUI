import pickle
from tkinter import *
from tkinter import messagebox

warningbox = None

filename = 'betalinger.pk'
fodboldtur = {}
infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()


def save(person, beløb):
    print(person.title(),beløb)
    # CHECK IF PERON OR BELØB IS EMPTY. IF IT IS DO NOTHING
    if person and beløb:

        # HVIS PERSONEN ALLEREDE ER I DICT SÅ TILJØJER MAN BELØBET ELLERS TILFØJER MAN EN NY PERSON TIL DICT MED BELØBET
        if person.title() in fodboldtur:
            fodboldtur[person.title()] += int(beløb)
        else:
            fodboldtur[person.title()] = int(beløb)

        print(fodboldtur)
        print("saved")

        outfile = open(filename, 'wb')
        pickle.dump(fodboldtur, outfile)
        outfile.close()
        print("Programmet er afsluttet!")

    else:
        global warningbox
        warningbox = True
        mainMenu()


def betal():
    betalWindow = Tk()
    betalWindow.title("Betal menu")
    betalWindow.geometry("300x100")

    def click3():
        saveornot = messagebox.askyesno("You forgot to save!", "Would you like to save?")
        if saveornot:
            personStr = str(personEntry.get())
            beløbInt = str(beløbEntry.get())

            betalWindow.destroy()
            save(personStr,beløbInt)
        if not saveornot:
            betalWindow.destroy()


    def back1():
        saveornot = messagebox.askyesno("You forgot to save!", "Would you like to save?")
        if saveornot:
            personStr = str(personEntry.get())
            beløbInt = str(beløbEntry.get())

            betalWindow.destroy()

            save(personStr, beløbInt)
            mainMenu()
        if not saveornot:
            betalWindow.destroy()
            mainMenu()

    def saveandexit():
        personStr = str(personEntry.get())
        beløbInt = str(beløbEntry.get())

        betalWindow.destroy()
        save(personStr,beløbInt)
        mainMenu()

    labelPerson = Label(betalWindow, text="Person")
    labelBeløb = Label(betalWindow, text="Beløb")
    labelPerson.grid(column=0,row=0,padx=9)
    labelBeløb.grid(column=1,row=0,padx=9)

    personEntry = Entry(betalWindow, width=20)
    personEntry.grid(column=0, row=1,padx=17)

    beløbEntry = Entry(betalWindow, width=20)
    beløbEntry.grid(column=1, row=1,padx=0)

    backButton = Button(betalWindow,text="back",command=back1, width=7)
    backButton.place(relx=0.15,rely=0.8,anchor=CENTER)

    saveButton = Button(betalWindow, text="save and exit...", command=saveandexit, width=11)
    saveButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    betalWindow.protocol("WM_DELETE_WINDOW", click3)
    betalWindow.resizable(0, 0)


def tabel():
    tabelWindow = Tk()
    tabelWindow.title("Tabel menu")

    # HER LAVER DICT OM TIL EN LISTE FOR AT KUNNE FINDE LÆNGDEN
    liste = []
    for ting in fodboldtur.items():
        liste.append(ting)

    height = len(liste) * 30 + 100
    # HER BRUGER JEG EN FSTRING TIL AT SÆTTE HØJDEN AF SKÆRMEN. HØJDEN ER LÆNGDEN AF DICT GANGET MED 30.
    tabelWindow.geometry(f"300x{height}")

    def back2():
        tabelWindow.destroy()
        mainMenu()

    def reset():
        deleteornot = messagebox.askyesno("Warning!", "Are you sure, this will clear the payments?")
        if deleteornot:
            fodboldtur.clear()
            outfile = open(filename, 'wb')
            pickle.dump(fodboldtur, outfile)
            outfile.close()

            tabelWindow.destroy()
            mainMenu()
        if not deleteornot:
            tabelWindow.destroy()
            tabel()

    backButton = Button(tabelWindow, text="back", command=back2, width=7)
    backButton.place(x=40, y=height-20, anchor=CENTER)

    resetButton = Button(tabelWindow, text="reset dict", command=reset, width=9)
    resetButton.place(relx=0.8, y=height - 20, anchor=CENTER)

    tabelWindow.resizable(0, 0)

    # HAR DET SVÆRT VED AT FORKLAR... PRØV AT SNAK MED MIG HVIS DU IKKE HELT FORSTÅR, JEG VIL NOK OGSÅ SELV SPØRGER HVORDAN JEG SKAL FORKLARE DET, haha...
    # JEG VAR RIMELIGT STOLT AF DENNE DEL, FIK LIDT HJÆLP AF MADS MED AT FINDE ULIGE OG LIGE TAL. TAK MADS!
    for label in range(len(liste)*2):
        rowLabel = int(label / 2)
        if (label % 2) == 0:
            columnLabel = 0
        else:
            columnLabel = 1
        text = str(liste[int(label/2)][columnLabel])

        name = Label(tabelWindow,width=22,text=text)
        name.grid(column=columnLabel,row=rowLabel,padx=0)
def mainMenu():
    global warningbox
    window = Tk()
    window.geometry("400x200")
    window.title("Menu")
    if warningbox:
        messagebox.showerror("Error!", "Write something on both entries")
        warningbox = False

    def clicked():
        window.destroy()
        betal()

    def clicked2():
        window.destroy()
        tabel()

    betalButton = Button(window, text="Betal",command=clicked,background="white",foreground="black",height=7,width=18)
    betalButton.grid(column=0,row=0,padx=25)

    tabelButton = Button(window, text="Tabel",command=clicked2,background="white",foreground="black",height=7,width=18)
    tabelButton.grid(column=1,row=0,padx=50,pady=40)


    window.resizable(0, 0)
    window.mainloop()

mainMenu()



