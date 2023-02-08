
import wikipedia
import pyperclip
import colorama
choide = int(input("Welcome to Essai!\nType in a topic and allow us to write an essay in mere seconds!\nType"+colorama.Fore.GREEN+" 1 "+colorama.Fore.WHITE+"to go to breif description\nType"+colorama.Fore.BLUE+" 2 "+colorama.Fore.WHITE+"to go to more detailed\ntype"+colorama.Fore.YELLOW+" 3 "+colorama.Fore.WHITE+"to go for the most detailed\ntype"+colorama.Fore.RED+" 4 "+colorama.Fore.WHITE+"to search if you have error\n"))
if choide == 1:

    wiki = input("Enter your topic!\n")
    summary = wikipedia.summary(wiki, sentences=2,auto_suggest=True)
    print("")
    print(colorama.Fore.GREEN+summary+colorama.Fore.WHITE)
    pyperclip.copy(summary)
if choide == 2:

    wiki = input("Enter your topic!\n")
    summary = wikipedia.summary(wiki, sentences=10,auto_suggest=True)
    print("")
    print(colorama.Fore.GREEN+summary+colorama.Fore.WHITE)
    pyperclip.copy(summary)
if choide == 3:
        wiki = input("Enter your topic!\n")
        summary = wikipedia.summary(wiki, sentences=1000,auto_suggest=True)
        print("")
        print(colorama.Fore.GREEN+summary+colorama.Fore.WHITE)
        pyperclip.copy(summary)
if choide == 4:
    wiki = input("Enter your topic you are having errors with.\n")
    mainwiki = wikipedia.search(wiki)
    print(mainwiki)
    print("\nIf you are getting an error searching '"+wiki+"' then try using some specific identifiers like those above\n")
