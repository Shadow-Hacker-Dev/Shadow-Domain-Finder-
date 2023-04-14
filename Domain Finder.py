
import os

try :
    import requests
except ImportError:
        print(" requests not found, downloading...")
        os.system("pip install requests")
try :
    import tldextract
except ImportError:
        print("tldextract not found, downloading...")
        os.system("pip install tldextract")
os.system ("clear")
blue =     "\033[94m"
print ('''


░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░

██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')
print (f"{blue}  Presents ")
print (f"{blue}  A Website checker and Domain Finder tool")
print('''




 ''')
def check_website():
    print ("Don't forget to enter the website link with Http/Https for the tool to work")
    url = input("Enter your website link: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        domain = tldextract.extract(url).domain
        print(f"[ ✓ ] Domain: {domain}")
    except requests.exceptions.RequestException as e:
        print("[ X ] Error: Website does not exist or cannot be reached.")
        
check_website()
