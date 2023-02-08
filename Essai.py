
import wikipedia
import pyperclip

choide = int(input("Welcome to Essai!\nType in a topic and allow us to write an essay in mere seconds!\nType 1 to go to breif description\nType 2 to go to more detailed\ntype 3 to go for the most detailed\ntype 4 to search if you have error\n"))
if choide == 1:

    wiki = input("Enter your topic!\n")
    summary = wikipedia.summary(wiki, sentences=2)
    print("")
    print(summary)
    pyperclip.copy(summary)
if choide == 2:

    wiki = input("Enter your topic!\n")
    summary = wikipedia.summary(wiki, sentences=10)
    print("")
    print(summary)
    pyperclip.copy(summary)
if choide == 3:
        wiki = input("Enter your topic!\n")
        summary = wikipedia.summary(wiki, sentences=1000)
        print("")
        print(summary)
        pyperclip.copy(summary)
if choide == 4:
    wiki = input("Enter your topic you are having errors with.\n")
    mainwiki = wikipedia.search(wiki)
    print(mainwiki)
    print("\nIf you are getting an error searching '"+wiki+"' then try using some specific identifiers like those above\n")
elif:
    print("INVALID CHOICE")
    