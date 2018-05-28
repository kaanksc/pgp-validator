import os
sistem=os.name
temaust="""
########################################################################
 ____   ____ ____   __     ___    _     ___ ____    _  _____ ___  ____  
|  _ \ / ___|  _ \  \ \   / / \  | |   |_ _|  _ \  / \|_   _/ _ \|  _ \ 
| |_) | |  _| |_) |  \ \ / / _ \ | |    | || | | |/ _ \ | || | | | |_) |
|  __/| |_| |  __/    \ V / ___ \| |___ | || |_| / ___ \| || |_| |  _ < 
|_|    \____|_|        \_/_/   \_\_____|___|____/_/   \_\_| \___/|_| \_\
                                                            #by kaanksc
########################################################################"""
def ekrantemizle():
    os.system("clear")
if sistem!="posix":
    print("Program sadece Linux için yazılmıştır")
    input("Çıkmak için [ENTER] tuşuna basın!")
else:
    while True:
        ekrantemizle()
        print(temaust)
        print("""1)PGP İmzası Onaylayın
2)Çıkış""")
        islem=input("#İşlem numarasını girin: ")
        if islem=="1":
            ekrantemizle()
            print(temaust)
            pgpkodu=input("Doğrulanmasını istediğiniz PGP İmzasını yazın( Çıkış=q): ")
            pgpkomutu="gpg –keyserver keys.gnupg.net –recv-keys "
            pgpislemi=pgpkomutu+pgpkodu
            if pgpkodu=="q":
                continue
            os.system(pgpislemi)
            print("PGP Kodu eklendi")
            input("Ana Menü = [ENTER]")
        elif islem=="2":
            exit()