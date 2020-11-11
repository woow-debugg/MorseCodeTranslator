#Morse code translator
from MorseCodeText import *
import speech_recognition as sr

#Alphabet set to morse code characters in a dictionary format
LetterDict = {
"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", 
"F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---",
"K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---",
"P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", 
"U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", 
}

#Numbers set to morse code characters in a dictionary format
NumberDict = {
"0" : "-----",  "1" : ".----",  "2" : "..---",  "3" : "...--", 	"4" : "....-", 	
"5" : ".....",  "6" : "-....",  "7" : "--...", 	"8" : "---..", 	"9" : "----."
}

#Punctuation set to morse code characters in a dictionary format
PunctuationDict = {
"."	: ".-.-.-", ","	: "--..--", "?"	: "..--..", "'"	: ".----.", "!"	: "-.-.--", "/"	: "-..-.", 
"("	: "-.--.", ")" : "-.--.-", "&"	: ".-...", ":"	: "---...", ";"	: "-.-.-.", "="	: "-...-", "+" : ".-.-.", 
"-"	: "-....-", "_"	: "..--.-", "\"": ".-..-.", "$"	: "...-..", "@"	: ".--.-.", "¿"	: "..-.-", "¡" : "--...-"
}


#greet the user
print('Hello this is a Morse Code Translator!')
print('To work I\'m going to need some words to translate!')

#decides if the user wants to type something simple or use an imported string
#imported string being something copied and pasted into MorseCodeText.py
def Decide():
    ans = (input('Do you want to type the words? (y/n):'))
    if 'y' in ans:
        TranslateString()
    else:
        ans2 = (input("Do you want to speak into the computer and turn that into morse code? (y/n) :"))
        if 'y' in ans2:
            TranslateSpeech() 
        else:
            TranslateStringImport()


#The recognizer processes audio to be put into a useable text
r = sr.Recognizer()
def ProcessAudio():
    global audio_text
    with sr.Microphone() as source:
        print('Say something : ')
        audio = r.listen(source)
        try:
            audio_text = r.recognize_google(audio)
            print('So you said... {}'.format(audio_text))

        except:
            print('Sorry cannot identify your speech. :(')
            
         


#ask the user if they want to translate something else
def Continue():
    x = (input("Anything else to translate? (y/n) : ")).lower()
    if 'y' in x:
        Decide()
    else:
        quit()


#Gets the desired string to be translated
def TranslateString():
#get the string and split it into useable format
    WordList =(input('Type what you want to translate. : '))
    txt = (list(WordList.upper()))
    MorseList = []
    
    for letter in txt:
        if letter in LetterDict:
            x = (LetterDict[letter])
            MorseList.append(x + ' ')
            x = ()

        elif letter in NumberDict:
            y = (NumberDict[letter])
            MorseList.append(y + ' ')
            y = ()

        elif letter in PunctuationDict:
            z = (PunctuationDict[letter])
            MorseList.append(z + ' ')
            z = ()
        else:
            MorseList.append('/ ')
    print("".join(MorseList))
    MorseList = []
    WordList = ()
    txt = ()
    Continue()


#grab the string saved in the MorseCodeText.py and translate it 
def TranslateStringImport():
    txt = (list(WordList2.upper()))
    MorseList2 = []
    
    for letter in txt:
        if letter in LetterDict:
            x = (LetterDict[letter])
            MorseList2.append(x + ' ')
            x = ()

        elif letter in NumberDict:
            y = (NumberDict[letter])
            MorseList2.append(y + ' ')
            y = ()

        elif letter in PunctuationDict:
            z = (PunctuationDict[letter])
            MorseList2.append(z + ' ')
            z = ()
        else:
            MorseList2.append('/ ')
    
    print("".join(MorseList2))
    MorseList2 = []
    txt = ()
    Continue()


#Use ProcessAudio() to translate speech into text and then turn that into morse code
def TranslateSpeech():
    ProcessAudio()
    txt = (list(audio_text.upper()))
    MorseList3 = []
    
    for letter in txt:
        if letter in LetterDict:
            x = (LetterDict[letter])
            MorseList3.append(x + ' ')
            x = ()

        elif letter in NumberDict:
            y = (NumberDict[letter])
            MorseList3.append(y + ' ')
            y = ()

        elif letter in PunctuationDict:
            z = (PunctuationDict[letter])
            MorseList3.append(z + ' ')
            z = ()
        else:
            MorseList3.append('/ ')
    
    print("".join(MorseList3))
    MorseList3 = []
    txt = ()
    Continue()

Decide()