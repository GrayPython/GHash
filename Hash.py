#Written by 《ERFAN》
#t.me/ErfanMAfshar

import hashlib,os
def main() :
    os.system('clear')
    print("---------------------------------")
    print("|                               |")
    print("|        Hash Generator         |")
    print("|                               |")
    print("|   {00} Generate               |")
    print("|   {99} Exit                   |")
    print("|                               |")
    print("---------------------------------")
    i = input("~~> ")

    def pyGreen(skk) : print("\033[92m {}\033[00m".format(skk))

    if i == "00" :
        print("-------------------------")
        print("                         ")
        print("  Choose your hash type  ")
        print("                         ")
        print("     1)Md5 Hash          ")
        print("     2)Sha1 Hash         ")
        print("     3)Sha256 Hash       ")
        print("     4)Sha512 Hash       ")
        print("     5)Sha224 Hash       ")
        print("     6)Sha384 Hash       ")
        print("                         ")
        print("-------------------------")

        hh = input("--> ")
        if hh == "1" :
            string = input("Enter Your Text: ")
            result = hashlib.md5(string.encode())
            pyGreen("Success!")
            print("Your MD5 Hash is --> \n", end="")
            print(result.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        elif hh == "2":
            string1 = input("Enter Your Text: ")
            result1 = hashlib.sha1(string1.encode())
            pyGreen("Success!")
            print("Your Sha1 Hash is --> \n", end="")
            print(result1.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        elif hh == "3":
            string2 = input("Enter Your Text: ")
            result2 = hashlib.sha256(string2.encode())
            pyGreen("Success!")
            print("Your Sha256 Hash is --> \n", end="")
            print(result2.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        elif hh == "4":
            string3 = input("Enter Your Text: ")
            result3 = hashlib.sha512(string3.encode())
            pyGreen("Success!")
            print("Your Sha512 Hash is --> \n", end="")
            print(result3.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        elif hh == "5":
            string4 = input("Enter Your Text: ")
            result4 = hashlib.sha224(string4.encode())
            pyGreen("Success!")
            print("Your Sha224 Hash is --> \n", end="")
            print(result4.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        elif hh == "6":
            string5 = input("Enter Your Text: ")
            result5 = hashlib.sha384(string5.encode())
            pyGreen("Success!")
            print("Your Sha384 Hash is --> \n", end="")
            print(result5.hexdigest())
            aa = input("\nPress Enter")
            if aa == "" :
                main()
        else :
            print("Please select the correct option!")
            aa = input("\nPress Enter")
            if aa == "":
                main()
    elif i == "99" :
        print("...GoodBye...")
        exit()
    else :
        print("Please select the correct option!")
        aa = input("\nPress Enter")
        if aa == "":
            main()
main()
