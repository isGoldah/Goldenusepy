import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk

w=Tk()
w.geometry('350x500')
w.title(' CORSO PYTHON IOSONOALE')
photo = PhotoImage(file = "logo.PNG")
w.iconphoto(False, photo)
w.resizable(0,0)

def run():
    if():
        run()


j=0
r=0
for i in range(100):
    c=str(333333+r)
    Frame(w,width=10,height=500,bg="#"+c).place(x=j,y=0)   
    j=j+10                                    
    r=r+0

Frame(w,width=250,height=400,bg='#737373').place(x=50,y=50)


from PIL import ImageTk,Image



imagea=Image.open("logo.png")
imageb= ImageTk.PhotoImage(imagea)

label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)


label1.place(x=115, y=60)

def discordpy():
    w.title("CORSO DISCORD.PY")
    label1.destroy()
    w.geometry("350x750")
    j=0
    r=0
    for i in range(100):
        c=str(333333+r)
        Frame(w,width=10,height=750,bg="#"+c).place(x=j,y=0)   
        j=j+10                                    
        r=r+0

    Frame(w,width=250,height=750,bg='#737373').place(x=50,y=50)
    message = ''' 
Hello Word Bot

Ora saltare subito per programmare un bot sofisticato utilizzando una nuova piattaforma non è facile. Cominciamo con un semplice bot "Hello World" che utilizza Discord.py. Bene:

    Crea il bot
    Aggiungilo al nostro server
    Programma il bot
    Prova la sua funzionalità

Nota: questo tutorial presuppone che tu abbia già installato python (versione 3.5.3 o successiva) su una macchina Windows e sappia come utilizzare la riga di comando per eseguire uno script python . Qualsiasi comando inviato al prompt dei comandi sarà preceduto da una "$"
Giving the Bot Brains (Programma il bot)

Il nostro bot sta aspettando offline, pronto per noi per connetterci e dargli vita! Esaminiamo ciò di cui abbiamo bisogno:

    Il discord.pymodulo python installato
    Un editor per scrivere la sceneggiatura
    Da qualche parte per eseguire il nostro script python

$ pip install discord.py

La prima sezione di codice saranno le nostre importazioni. In questo momento abbiamo solo bisogno di discordun'estensione dal discordpacchetto,commands

# Imports
import discord
from discord.ext import commands
view raw
tut_bot_imports.py hosted with ❤ by GitHub

Successivamente creeremo una variabile TOKENche contiene il nostro token per autorizzare il codice con Discord. Ciò non solo consentirà al codice di interagire con Discord, ma indicherà anche a Discord con quale bot stiamo interagendo. Il nostro token si troverà nella pagina Bot . È nascosto per impostazione predefinita. Si tratta di informazioni sensibili e condividerle con chiunque consentirà loro pieno accesso al tuo bot fino a quando non rigenererai il tuo token.
Il nostro prossimo passo è inizializzare il nostro bot. Da commandsuseremo il Botmetodo. Aggiungiamo l'argomento command_prefix='!'per dire al nostro bot che i comandi inizieranno con un punto esclamativo (!). Qualunque cosa funzionerà qui, ma i caratteri speciali sono considerati best practice poiché è improbabile che attivino erroneamente il nostro bot.

# Create bot
client = commands.Bot(command_prefix='!')
view raw
create_bot.py hosted with ❤ by GitHub

Successivamente avremo l'output dello script sulla console in modo da poter verificare che il bot sia connesso correttamente. Scriveremo una funzione che stampa il nome e il numero ID del bot quando si connette. Quando clientviene inizializzato, entrambi namee iddiventano disponibili come parte userdell'attributo. Con una semplice formattazione del testo, possiamo stampare client.user.namee client.user.idalla console. Non preoccuparti troppo del codice che precede la funzione, a questo punto devi solo sapere che questi sono necessari per il funzionamento di Discord.py.

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
view raw
tut_bot_start_info.py hosted with ❤ by GitHub

Ora vogliamo che il bot dica "Hello World" quando digitiamo "! Helloworld" nel canale di chat di Discord. Per fare ciò, dobbiamo creare una funzione di comando. Inizierà con il decoratore di comando. Successivamente definiamo la funzione helloworld. Il nome di questa funzione è esattamente come chiameremo la funzione da discord. La funzione richiede 1 argomento: ctx. Questo sarà il contesto del comando e Discord.py lo gestirà per noi. ctxconterrà molte cose che vorremmo sapere su una richiesta, incluso il canale Discord da cui proviene. Nella riga successiva utilizziamo la awaitparola chiave per attendere che il processo che esegue il nostro bot sia pronto. Il ctx.sendinvia il “Ciao Mondo!” messaggio di nuovo da dove è stato inviato il comando, come salvato nel contesto della richiesta.

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
view raw
tut_bot_command01.py hosted with ❤ by GitHub

Per la parte finale del nostro script, dobbiamo usare il runmetodo, passandogli il nostro token per connetterci e avviare il bot. Con quello aggiunto possiamo salvare e provare a eseguirlo.

# Run the bot
client.run(TOKEN)
view raw
tut_bot_run.py hosted with ❤ by GitHub

Per eseguire il nostro bot, apri la riga di comando. Passa alla directory in cui è stato salvato lo script utilizzando il comando cambia directory. Una volta nella directory corretta, esegui lo script.

$ cd "path\to\your\bot"
$ python tutorial_bot.py

Connected to bot: Tutorial Application Video 1
Bot ID: 7505311099577812556

Testare il tuo bot

Per testare il comando hello world che abbiamo scritto, vai al server Discord a cui abbiamo aggiunto il bot in precedenza. Sul pannello di destra, vedrai che il bot è ora nello stato online.

Per testare il comando, entra semplicemente !helloworldnel canale Discord. Il bot risponderà rapidamente!
Prossimi passi

Ora che hai le basi, ci sono molte altre cose che puoi fare con il tuo Discord bot. Oltre agli speciali metodi Discord forniti, puoi anche aggiungere qualsiasi codice Python tradizionale per eseguire operazioni prima di interagire nuovamente con il server Discord. Vuoi nascondere il tuo gettone? Dai un'occhiata al mio tutorial qui sotto:

Tieni d'occhio altri post relativi all'uso di Discord.py e alla creazione di robot Discord in Python. Se hai idee o richieste per altri tutorial, fammelo sapere nei commenti qui sotto.
Script Bot completo

# Imports
import discord
from discord.ext import commands

# Credentials
TOKEN = 'YOUR-TOKEN-HERE'

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')

client.run(TOKEN)
'''

    text_box = Text(
    w,
    height=50,
    width=31
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')

def turtle():
    w.title("CORSO TURTLE")
    label1.destroy()
    w.geometry("350x750")
    j=0
    r=0
    for i in range(100):
        c=str(333333+r)
        Frame(w,width=10,height=750,bg="#"+c).place(x=j,y=0)   
        j=j+10                                    
        r=r+0

    Frame(w,width=250,height=750,bg='#737373').place(x=50,y=50)
    message = '''
Disegnare una linea

L’immagine che hai visto prima è fatta solo di righe!
Come prima cosa, devi quindi imparare a tracciare una linea usando Python.

Per iniziare scrivi queste istruzioni:

from turtle import Turtle, Screen
tartaruga = Turtle()
sfondo = Screen()
tartaruga.forward(100)
Fare una curva

Hai scritto un programma per disegnare una linea. Bravo!
Adesso proviamo a disegnare una curva. Per farlo, il cursore non deve solamente muoversi in linea retta, ma anche a girare a destra o a sinistra.

Aggiungi al tuo programma le righe:

tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90) fa girare il cursore a destra di 90 gradi.

Allo stesso modo, potresti farlo girare a sinistra con tartaruga.left(90).
Se vuoi farlo ruotare un po’ di più, o di meno, ti basta modificare il valore dell’angolo di rotazione.

Completa il quadrato che hai iniziato a disegnare aggiungendo le righe di codice necessarie. Man mano aggiungi il codice, fai clic su Run per vedere il risultato. Continua a modificarlo finché non funziona correttamente.
Esercizi

Svolgi i seguenti esercizi:

    Disegna un rettangolo: 2 dei 4 lati devono essere più lunghi.
    Disegna un triangolo: di quanti gradi deve essere la rotazione?
    Disegna una croce: andare avanti e indietro è una buona soluzione.
    Disegna un cerchio

Cambiare i colori

Il colore di default della penna è il nero, e quello dello sfondo è il bianco. Puoi cambiare questi colori per rendere le forme del disegno realizzato con Python Turtle più espressive.

Leggi il programma scritto di seguito. Contiene le tre variabile R, G, e B.

from turtle import Turtle, Screen
tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)

R = 255
G = 255
B = 0

sfondo.bgcolor((R, G, B))

Le variabili sono un modo per salvare un valore e dargli un nome. Ad esempio, la variabile chiamata R ha il valore 255.

colormode(255) definisce uno spazio colore di 255 valori per ogni variabile, uno spazio cioè in cui ciascuna variabile può assumere un valore compreso fra 0 e 255. Di default è impostato a (1).

Lancia il programma e vedi cosa succede.
Cosa pensi rappresentino le variabili R, G, e B?

Puoi anche cambiare il colore con cui disegni. Lancia il programma scritto qui di seguito e vedi cosa succede:

from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
sfondo.colormode(255)
R = 255
G = 0
B = 124
tartaruga.color((R, G, B))
tartaruga.forward(100)
tartaruga.right(120)
tartaruga.forward(100)
Esercizi

Svolgi i seguenti esercizi:

    Completa il triangolo con un colore a tua scelta.
    Disegna un quadrato con i lati di quattro sfumature di rosso.
    Disegna una croce di quattro colori diversi.

Ripetizioni

Ripetere righe di codice è uno dei modi più rapidi per scrivere un programma. Spesso è infatti più efficiente ripetere righe di codice piuttosto che scrivere nuove istruzioni. Per esempio, il quadrato che hai creato prima usa la stessa istruzione ripetuta quattro volte, ma avresti potuto scriverla una sola volta e aggiungere un’altra istruzione che dica di ripeterla.

Per ripetere righe di codice si usano i loop.

In Python hai a disposizione due tipi di loop: il loop while e il loop for. Se vuoi che un blocco di codice venga ripetuto per sempre, o fino a che una certa condizione venga soddisfatta, il loop while è con ogni probabilità la scelta migliore. Se invece vuoi che il loop venga eseguito un numero specifico di volte, è meglio usare il loop for.

Nel caso qui di seguito, abbiamo usato il loop while True. Il codice interno al suo interno verrà ripetuto per sempre. Prova a eseguirlo per vedere come funziona, ma ricorda che non si fermerà da solo!

from turtle import Turtle, Screen    

turtle = Turtle()	  

while True:
    turtle.forward(1)
    turtle.right(1)

Nell’esempio che segue, abbiamo invece usato un loop for.

from turtle import Turtle, Screen

tartaruga = Turtle()

sfondo = Screen()
sfondo.colormode(255)

tartaruga.penup()

for i in range(8):
  tartaruga.write(i)
  tartaruga.forward(20)
  Un loop for ripete le istruzioni un certo numero di volte; in questo caso 8 volte. Al loop for è associata una variabile (che qui abbiamo chiamato i). Nel nostro esempio, i parte da 0 e aumenta di 1 ad ogni ciclo.

Utilizziamo questo loop per disegnare un quadrato:

from turtle import Turtle, Screen

tartaruga = Turtle()

for i in range(4):
  tartaruga.forward(100)
  tartaruga.right(90)

Copia questo codice e premi Run.
Al computer è stato chiesto di ripetere 2 instruzioni 4 volte per disegnare il quadrato.

Una volta creata una forma usando un loop, la puoi ripetere tutte le volte che vuoi inserendola in un altro loop. Questo è un modo fantastico per disegnare spirali.

Modifica il programma in questo modo:

from turtle import Turtle, Screen
tartaruga = Turtle()

for i in range(30):
    for i in range(4):
      tartaruga.forward(100)
      tartaruga.right(90)
    tartaruga.right(25)
    La spirale viene disegnata imponendo prima una rotazione e poi un movimento in avanti. Il blocco di codice per disegnare il quadrato è all’interno di un loop for che lo ripete 30 volte, ogni volta volta ruotando il cursore di 25 gradi in modo che alla fine venga creata una piacevole forma a spirale.
Esercizi

Svolgi i seguenti esercizi:

    Sei in grado di modificare il loop for per creare una spirale ancora più interessante a partire da una delle forme che hai creato prima?
    Aggiungi alcune righe di codice in cui modifichi le variabili R, G, e B per disegnare una spirale di più colori. Prova a creare una spirale arcobaleno.

Spirali ancora più belle

Prova a leggere il codice scritto di seguito e a indovinare cosa fa.

from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)

R = 255
G = 0
B = 0
sfondo.bgcolor((255, 255, 255))

for i in range(2000):
  G += 1
  B += 0.5
  R -= 1
  tartaruga.color((R, G, B))
  
  tartaruga.forward(i)
  tartaruga.right(98)

Copialo, premi Run e vedi se avevi ragione.

Avrai notato che ci vuole moltissimo tempo prima che il programma si concluda. Possiamo accelerare un po’ le cose aggiungendo una linea prima del loop for:

turtle.speed(0)

Lancia di nuovo il programma: dovrebbe essere un po’ più veloce.
Il nostro codice ha creato una spirale multicolore modificando i valori delle variabili R, G, e B. I colori sono comunque un po’ mono dimensionali. Riesci a migliorarlo?
Colori in loop

Per ottenere colori più interessanti, potresti scrivere una lunga lista di colori diversi, e continuare a cambiare i colori pescandoli dalla lista. In Python puoi creare una lista usando le parentesi quadre [ ].
Ecco un esempio di una lista di colori RGB:

colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]

Il prossimo passo è un po’ più difficile. Leggi il programma seguente e lancialo per vedere cosa succede.

from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)
sfondo.bgcolor((0, 0, 255))

tartaruga.speed(0)

colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]

for i in range(10):
  tartaruga.color(colours[i])
  tartaruga.forward(10)

La riga tartaruga.color(colours[i]) dice al programma di scegliere l’“iesimo” elemento nella lista. i va da 0 a 9.
E se volessimo una linea più lunga?
Prova a cambiare il numero di loop scrivendo range(20) e vedi cosa succede.
Hai ottenuto un errore?
Un operatore per risolvere il problema

Nell’esempio precedente, ti serve una maniera per continuare a vagliare in loop gli elementi nella lista, in modo che, quando i arriva a 9, ritorni all’inizio e peschi una seconda volta l’elemento 0 nella lista. È in casi come questo che l’operatore resto % può esserti utile.
Prova a leggere il programma scritto di seguito e a indovinare cosa fa.

print(18 % 6)

Premi Run e vedi se avevi ragione.

Prova a cambiare i numeri nel comando print. Ecco alcuni esempi da provare:

print(12 % 6)
print(6 % 6)
print(0 % 6)
print(13 % 6)
print(17 % 6)
print(1 % 6)
print(8 % 6)
print(11 % 6)

Hai capito cosa fa?
L’operatore % stampa il resto di una divisione. Per esempio, 15 ÷ 6 fa 2 con il resto di 3. Quindi 15 % 6 darebbe 3.

Possiamo usare questo operatore per risolvere il problema descritto in precedenza..

Guarda l’esempio scritto di seguito, e leggi con attenzione il codice per capire come viene utilizzato l’operatore resto.

from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)
sfondo.bgcolor((0, 0, 255))

tartaruga.speed(0)

colours = [(85, 211, 136), (197, 196, 126), (235, 233, 166), (25, 135, 222), (211, 64, 159), (159, 165, 106), (178, 160, 125), (36, 192, 70), (231, 184, 204), (63, 203, 219)]

for i in range(2000):
  tartaruga.color(colours[i % len(colours)])
  tartaruga.forward(i)
  tartaruga.right(98)
  Liste gigantesche

Ora puoi provare a creare una lista di colori un po’ più lunga rispetto a quella di prima. Per farlo puoi usare un loop while. A differenza di quanto accade con un loop for, un loop while va avanti fino a che non viene soddisfatta una certa condizione.

Guarda il programma scritto di seguito. Il loop while viene usato per aumentare gradualmente il valore di G fino a che raggiunge il valore 255. Ogni volta, i colori vengono aggiunti alla lista.

colours = [ ]
R = 255
G = 0
B = 0
while G < 255:
  colours.append((R, G, B))
  G += 5 
print(colours)

Saresti in grado di aggiungere altri 2 loop while per avere più colori?
Il primo dovrebbe diminuire gradualmente R fino a farle raggiungere il valore 0. Il secondo dovrebbe aumentare B fino a farle raggiungere 255.
Prova, ma non preoccuparti se non ci riesci: come farlo verrà comunque mostrato alla fine di questa risorsa.
In conclusione

Ora sei in grado di usare un loop while insieme al codice per costruire una spirale.

Leggi con attenzione il codice qui di seguito, e cerca di capire con esattezza cosa fa. Prova a modificare le variabili presenti nei loop, per vedere come viene modificato il risultato finale.

from turtle import Turtle, Screen

tartaruga = Turtle()
sfondo = Screen()

sfondo.colormode(255)

R = 255
G = 0
B = 0
sfondo.bgcolor((0, 0, 255))

tartaruga.speed(0)

colours = []

while G <= 255:
    colours.append((R, G, B))
    G += 1
while R >= 0:
    colours.append((R, G, B))
    R -= 1
while B < 255:
    colours.append((R, G, B))
    B += 1
while G > 0:
    colours.append((R, G, B))
    G -= 1
while R < 255:
    colours.append((R, G, B))
    R += 1

for i in range(3000):
  # La riga seguente fa cambiare di continuo il colore, anche se i è maggiore del numero di colori presenti nella lista
  tartaruga.color(colours[i % len(colours)])
  tartaruga.forward(i/3)
  tartaruga.right(119)
    '''

    text_box = Text(
    w,
    height=50,
    width=31
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')

def tkinter():
    w.title("CORSO TKINTER")
    label1.destroy()
    w.geometry("350x750")
    j=0
    r=0
    for i in range(100):
        c=str(333333+r)
        Frame(w,width=10,height=750,bg="#"+c).place(x=j,y=0)   
        j=j+10                                    
        r=r+0

    Frame(w,width=250,height=750,bg='#737373').place(x=50,y=50)
    message ='''
Esempi di base
Hello, world!

Un primo esempio fa comparire una finestra di dialogo (senza nulla dentro).

import tkinter 
root = tkinter.Tk()  
root.mainloop() 
Avremmo potuto ottenere lo stesso risultato importando direttamente nel namespace corrente le componenti di tkinter:

from tkinter import * 
root = Tk()  
root.mainloop() 

Quando il ciclo principale si esegue esso attende gli eventi che accadono nell'oggetto radice.

Se avviene un evento allora esso viene gestito e il ciclo prosegue, continuando la sua attesa per il successivo evento. L'esecuzione del ciclo continua sinché nella finestra radice non si verifica un evento «destroy» (ad esempio, quando viene chiusa la finestra). Quando la radice è distrutta, il ciclo di gestione degli eventi termina.

Se vogliamo aggiungere un'etichetta nella finestra, dobbiamo prima definirla e poi sistemarla (con il metodo pack o con altri) nella finestra principale o in un altro contenitore. Il processo serve a stabilire una relazione visuale tra il widget e il suo genitore. In sua assenza, il widget esiste ma non viene visualizzato.

from tkinter import * 
root = Tk()
MyLabel = Label(root, text="Hello, world!")
MyLabel.pack()
root.mainloop() 

GUI

Gli oggetti GUI (widget, da windows gadget) vengono organizzati in gerarchie. Nell'esempio, l'etichetta MyLabel è figlia dell'oggetto principale, root.

Per i widget possono essere definiti i valori di alcuni attributi in diversi modi. Il più semplice è di impostarli come se fossero valori di un dizionario:

from tkinter import * 
root = Tk()
MyLabel = Label(root, text="The quick brown fox jumps over the lazy dog.")
MyLabel['background']="#FFFFFF"
MyLabel['foreground']="red"
MyLabel.pack()
root.mainloop() 

GUI

Avremmo potuto impostare anche il testo scrivendo un codice simile al seguente:

MyLabel['text']="The quick brown fox jumps over the lazy dog."

Si può avere un po' di controllo su come i widget vengono sistemati all'interno della finestra usando l'attributo "side", come nell'esempio che segue:

from tkinter import * 
root = Tk()
MyLabel1 = Label(root, text="Prima etichetta.")
MyLabel1['background']="#FFFFFF"
MyLabel1['foreground']="red"
MyLabel1.pack({"side":"right"})
MyLabel1.pack()
MyLabel2 = Label(root, text="Seconda etichetta.")
MyLabel2['background']="#FFFFFF"
MyLabel2['foreground']="blue"
MyLabel2.pack({"side":"left"})
root.mainloop() 

GUI

Il metodo pack() serve ad accatastare i widget uno dopo l'altro a partire dalla posizione indicata. Vedremo ulteriori esempi più avanti.
Gestione degli eventi

Per i pulsanti è possibile impostare un gestore di eventi, in modo da richiamare una determinata funzione al clic del mouse.

from tkinter import * 

def MyButton_Click():
    print("Mi hai cliccato... (standard output)")
    StatusBar["text"]="mi ha cliccato... (status bar)"

root = Tk()

MyButton = Button(root, text="Fai clic qui")
MyButton['background']="#FFFFFF"
MyButton['foreground']="red"
MyButton['command']=MyButton_Click
MyButton.pack({"side":"top", "padx": 10, "pady": 20})

StatusBar = Label(root, text="...")
StatusBar['background']="#FFFFFF"
StatusBar['foreground']="blue"
StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

root.mainloop() 

GUI
prima…

GUI
dopo…
Input di testo

Per poter chiedere in input un testo all'utente, si può usare un widget di tipo Entry, che viene associato ad una variabile.

from tkinter import * 
def MyButton_Click():
    StatusBar["text"]=name.get()

root = Tk()
name = StringVar()
MyInputBox = Entry(root, textvariable=name)
MyInputBox.pack()
MyButton = Button(root, text="Fai clic qui")
MyButton['background']="#FFFFFF"
MyButton['foreground']="red"
MyButton['command']=MyButton_Click
MyButton.pack({"side":"top", "padx": 10, "pady": 20})
StatusBar = Label(root, text="...")
StatusBar['background']="#FFFFFF"
StatusBar['foreground']="blue"
StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

root.mainloop() 

GUI
Implementazione Object-Oriented

Per applicazioni con un minimo di complessità, conviene definire una propria classe, come nell'esempio seguente:

from tkinter import * 

class Application(object):
    def __init__(self, parent):
        self.name = StringVar()
        self.MyInputBox = Entry(parent, textvariable=self.name)
        self.MyInputBox.pack()
        self.MyButton = Button(parent, text="Fai clic qui")
        self.MyButton['background']="#FFFFFF"
        self.MyButton['foreground']="red"
        self.MyButton['command']=self.MyButton_Click
        self.MyButton.pack({"side":"top", "padx": 10, "pady": 20})
        self.StatusBar = Label(parent, text="...")
        self.StatusBar['background']="#FFFFFF"
        self.StatusBar['foreground']="blue"
        self.StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

    def MyButton_Click(self):
        self.StatusBar["text"]=self.name.get()

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()

Creazione e gestione dinamica dei widget

Può essere utile creare dinamicamente dei widget durante l'esecuzione del programma (ad esempio, a seconda dell'input dell'utente). Se si vogliono creare dei pulsanti, si pone il problema di come associare una funzione che gestisce gli eventi associati ai vari pulsanti (visto che il gestore di eventi è una funzione che non ha parametri). La soluzione, come nell'esempio seguente, è di creare una funzione dinamicamente (tramite la parola chiave lambda). Approfondiremo l'uso delle espressioni lambda più avanti, nella lezione 22. Vedremo anche, nella lezione 23, che attraverso functools.partial() si può ottenere lo stesso risultato in maniera leggermente più semplice.

from tkinter import *

def str2int(s):
    try:
        k=int(s)
        return k
    except:
        return 0

class Application(object):
    def __init__(self, parent):

        self.name = StringVar()
        self.buttons=[]
        self.parent = parent

        self.MyInputBox = Entry(parent, textvariable=self.name)
        self.MyInputBox.pack()

        self.MyButton = Button(parent, text="Fai clic qui")
        self.MyButton['background']="#FFFFFF"
        self.MyButton['foreground']="red"
        self.MyButton['command']=self.MyButton_Click
        self.MyButton.pack({"side":"top", "padx": 10, "pady": 20})

        self.StatusBar = Label(parent, text="...")
        self.StatusBar['background']="#FFFFFF"
        self.StatusBar['foreground']="blue"
        self.StatusBar.pack({"side":"bottom", "expand":"yes", "fill":"x"})

    def MyButton_Click(self):
        self.StatusBar["text"]=self.name.get()
        n=str2int(self.name.get())
        for i in range(n):
            b=Button(self.parent, text="pulsante " + str(i))
            b['background']='yellow'
            b['command']=self.BuildButtonAction(i)
            b.pack()
            self.buttons.append(b)

    def BuildButtonAction(self, number):
        return lambda : self.ChangeButtonColor(number)

    def ChangeButtonColor(self, number):
        self._SwitchColor(self.buttons[number])

    def _SwitchColor(self, button):
        button['background']='yellow' if button['background']=='red' else 'red'

def main():
    root = Tk()
    myapp = Application(root)
    root.mainloop() 

if __name__=='__main__':
    main()
'''

    text_box = Text(
    w,
    height=50,
    width=31
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')


def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #FF0000
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=turtle)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)
    myButton1.place(x=x,y=y)


bttn(100,375,'Turtle','#737373','#FD1F1F')

def bttn2(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton2['background'] = ecolor #FF0000
        myButton2['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton2['background'] = lcolor
        myButton2['foreground']= ecolor


    myButton2 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=tkinter)
                  
    myButton2.bind("<Enter>", on_entera)
    myButton2.bind("<Leave>", on_leavea)

    myButton2.place(x=x,y=y)


bttn2(100,320,'Tkinter','#737373','#ff9933')

def bttn3(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton3['background'] = ecolor #FF0000
        myButton3['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton3['background'] = lcolor
        myButton3['foreground']= ecolor

    myButton3 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=discordpy)
                  
    myButton3.bind("<Enter>", on_entera)
    myButton3.bind("<Leave>", on_leavea)

    myButton3.place(x=x,y=y)


bttn3(100,265,'Discord.Py','#737373','#ffff00')


w.mainloop()

