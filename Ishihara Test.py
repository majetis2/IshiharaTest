import tkinter
from tkinter import*
from PIL import ImageTk, Image
import random

#0 -nothing
#-1 - unsure

#Create a list of plates
plates = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
          "16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28",
          "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]

choices = [["1","2","3","4"]]

answers_choice = choices*38

print(answers_choice)


normal_answers = [12,8,6,29,57,5,3,15,74,2,6,97,45,5,7,16,73,0,0,0,0,26,42,
                  35,96,'purple and red spots', 'purple and red spots', 0, 0, 'blu-green line',
                  'blue-green line', 'ornage line', 'orange line','blue-green and yellow-green line',
                  'blue-green and yellow-green line', 'violet and orange line', 'violet and orange line',
                  'orange line']

redgreen_answers = []

prot_answers = []

deut_answers = []

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < len(plates)):  #Needs to change
        x = random.randint(0,len(plates)-1)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
##    if score >= 20:
##        img = PhotoImage(file="great.png")
##        labelimage.configure(image=img)
##        labelimage.image = img
##        labelresulttext.configure(text="You Are Excellent !!")
##    elif(score >= 10 and score < 20):
##        img = PhotoImage(file="ok.png")
##        labelimage.configure(image=img)
##        labelimage.image = img
##        labelresulttext.configure(text="You Can be Better !!")
##    else:
##        img = PhotoImage(file="bad.png")
##        labelimage.configure(image=img)
##        labelimage.image = img
##        labelresulttext.configure(text="You Should Work Hard !!")
        
        

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score+5
        x += 1
    print(score)
    showresult(score)
        


ques = 1
def selected():
    global radiovar, user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < len(plates):  #Need to change this
        plate_change = PhotoImage(file = plates[indexes[ques]]+'.png')
        lblQuestion.config(image = plate_change)
        lblQuestion.img = plate_change
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()
    #print(x)




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    photo = PhotoImage(file = plates[indexes[0]]+".png")
    lblQuestion = Label(
        root,
        image = photo,
        background = "#ffffff"
    )
    lblQuestion.image = photo
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)


    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times",12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times",12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times",12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times",12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title('Ishihara Test')
root.geometry('700x600')
root.config(background = "#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="1.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff"
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Ishihara Test",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))


img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read the Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules= Label(
    root,
    text = "This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nHence think before you select",
    width = 100,
    font = ("Times",14),
    background =  "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()
    
root.mainloop()

