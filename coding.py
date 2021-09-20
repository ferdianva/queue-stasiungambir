def menu() :
    import os
    os.system("CLS")
    print("__________________________________________________________________________________________________________________________")
    print("__________##########___________#####__________#####_____________#####_____############_______####____##########___________")
    print("________####_____####________###____###______########_________########____####______###______####____####___####__________")
    print("_______####_______####______###______###_____####__####_____####__####____####_______###_____####____####____####_________")
    print("_______####________####____####______####____####___####___####___####____####________###____####____####_____####________")
    print("_______####________________####______####____####_____#######_____####____#############______####____####______####_______")
    print("_______####________________##############____####_______###_______####____#############______####____###########__________")
    print("_______####_______#####____####______####____####_________________####____####________###____####____####_____####________")
    print("_______####_________###____####______####____####_________________####____####_______###_____####____####______####_______")
    print("________####_______####____####______####____####_________________####____####______###______####____####______####_______")
    print("_________############______####______####____####_________________####____############_______####____####______####_______")
    print("=========================================[S\tT\tA\tT\tI\tO\tN]================================")
    print("_____########################____###########################____#########################____##################___________")
    print("_____####________________####____####___________________####____####_________________####____####___________####__________")
    print("_____####________________####____####___________________####____####_________________####____####____________####_________")
    print("_____####________________####____####___________________####____####_________________####____####_____________####________")
    print("_____####________________####____####___________________####____####_________________####____####______________####_______")
    print("_____########################____###########################____#########################____######################___**__")
    print("_____########################____###########################____#########################____######################__***__")
    print("_____########################____###########################____#########################____######################_****__")
    print("_____________________________****___________________________****_________________________****______________________*****__")
    print("____(O|O|O|O|O|O|O|O|O|O|O|O)____(O|O|O|O|O|O|O|O|O|O|O|O|O)___(O|O|O|O|O|O|O|O|O|O|O|O|O)__(O|O|O|O|O|O|O|O|O|O|O)*****__")
    print("     \nSelamat Datang Di Stasiun Gambir")
    print("             \nDaftar Layanan: ")
    print("[1] Daftar Nama Kereta Api")
    print("[2] Urutan Keberangkatan Kereta Api")
    print("[3] Detail Perjalanan Kereta Api")
    print("[4] Keluar dari Program")
    pil = int(input("Masukkan No Menu yang Anda Pilih : " ))
    pilihmenu(pil)

def pilihmenu(p) :
    if p == 1:
        namakereta()
    elif p == 2:
        output()
    elif p == 3:
        caridata()
    elif p == 4 :
        print("Anda telah keluar dari program.")
        print("Terima kasih atas kunjungan Anda.")
 

class queue:
    def __init__(self,max_size):
        print("Sebuah antrian di Stasiun Gambir dibuat dengan kapasitas:",max_size,"")
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__rear= -1
        self.__front= 0
        self.__back= 0
    
    
    def isempty(self):
        if self.__rear == 0:
            return True
        else :
            return False
    
    
    def isfull(self):
        if self.__rear == self.__max_size :
            return True
        else :
            return False   
    
    def enqueue (self,newdata) :
        if(self.isfull()):
            print("Maaf antrian penuh, KA ",newdata," tidak dapat memasuki antrian Stasiun Gambir")
            
        else:
            self.__rear += 1
            self.__elements[self.__rear] = newdata
            print(" ")
            print("\n KA ",newdata," masuk Stasiun Gambir.")
            
    def dequeue(self): #dari sini
        if self.isempty():
            print("Maaf, antrian pada Stasiun Gambir kosong.")
            return None
        else:
            datakeluar = self.__elements[self.__front]
            self.__elements[self.__front] = None
            self.__front = (self.__front+1) % self.__max_size
            #self.__rear = self.__rear-1
            print(" ")
            print("\n KA ",datakeluar," berangkat dari Stasiun Gambir.")
            return datakeluar
			
   
    def visualisasiqueue (self): 
        #print("\nVisualisasi Antrian KA di Stasiun Gambir\n") 
        for i in range(self.__max_size): 
            print("  	[%2d]	"%(self.__max_size - i),end=" ") 
        print()

        for i in range(self.__max_size + 1):
            print("-----------------",end=" ") 
        print()

        pointer = self.__rear
        for i in range (self.__max_size): 
            if self.__elements[i] == None: 
                print("  %10s   "%(""),end="")
            else:
                print("  %10s   "%(self.__elements[pointer]),end="") 
                pointer -= 1
        
        print("		>> [DEPAN]",end="") 
        print()

        for i in range(self.__max_size + 1):
            print("-----------------",end=" ") 
        

def caridata() :
    import os
    os.system("CLS")
    print("\nAnda Berada Pada Menu Detail Perjalanan Kereta Api")
    carikereta = str(input("\nCari Kereta Berdasarkan (Nama Kereta/Jam Keberangkatan/Relasi) : "))
    counter = 0
    if carikereta == "Nama Kereta" or carikereta == "nama kereta":
        print("Ketik nama kereta dengan huruf kapital!")
        print("Contoh: TAKSAKA (84)")
        keyword = input("Masukkan Nama Kereta: ")
        bukadata = open("data/datakereta.txt")
        for search_data in bukadata:
            if search_data.startswith(keyword):
                pecah = search_data.split(",")
                print("\nNama Kereta		: " + pecah [0])
                print("Jam Keberangkatan	: " + pecah [1])
                print("Tujuan Kereta		: " + pecah [2])
                print("Tekan [ENTER] untuk melanjutkan!")
                input()
                counter += 1
        if counter == 0:
            print("\nTidak ditemukan kereta dengan nama :" + keyword)
        bukadata.close() 
    elif carikereta == "Jam Keberangkatan" or carikereta == "jam keberangkatan" :
        print("Ketik jam keberangkatan secara DETAIL!")
        print("Contoh: 10:00 WIB")
        keyword3 = input("\nMasukkan Jam Keberangkatan : ")
        counter = 0
        number = 1
        bukadata = open("data/datakereta.txt")
        bukajdwl = bukadata.readlines()
        bukajdwl.sort()
        for i in bukajdwl:
            x = i.strip()
            y = x.split(",")
            z = y[0] + " " + y[1] + " " + y[2] + " "
            if keyword3 in z:
                print("Nama Kereta			: " + y[0])
                print("Jam Keberangkatan		: " + y[1])
                print("Relasi				: " + y[2] + "\n")
                counter += 1
                number +=1
        if counter == 0:
            print("\nTidak ditemukan data buku dengan jam keberangkatan : " + keyword3)
        bukadata.close()
    elif carikereta == "Relasi" or carikereta == "relasi" :
        print("Ketik relasi perjalanan secara DETAIL!")
        print("Contoh: GAMBIR-KIARACONDONG")
        keyword5 = input("\nMasukkan Relasi Perjalanan : ")
        counter = 0
        number = 1
        bukadata = open("data/datakereta.txt")
        bukajdwl = bukadata.readlines()
        bukajdwl.sort()
        for i in bukajdwl:
            x = i.strip()
            y = x.split(",")
            z = y[0] + " " + y[1] + " " + y[2] + " "
            if keyword5 in z:
                print("Nama Kereta			: " + y[0])
                print("Jam Keberangkatan		: " + y[1])
                print("Relasi				: " + y[2] + "\n")
                counter += 1
                number +=1
        if counter == 0:
            print("\nTidak ditemukan data dengan relasi : " + keyword5)
        bukadata.close()
    print("\nIngin melihat detail perjalanan lagi? (Ya/Tidak)",end="")
    crdata = input(" : ")
    if crdata == "ya" or crdata == "Ya":
        caridata()
    else :
        menu()

        # sampe sini
	
        
   
        
def namakereta() :
	import os
	os.system("CLS")
	print("				\n Berikut adalah nama-nama kereta: \n ")
	print("	BIMA (76)\n")
	print("	GAJAYANA (72)\n")
	print("	ARGO LAWU (8)\n")
	print("	TAKSAKA (84)\n")
	print("	ARGO LAWU (58A)")
	print('\n Tekan ENTER untuk kembali ke menu utama')
	input()
	menu()


def output() :
	import os
	os.system("CLS")
	Q1 = queue(5) 
	Q1.visualisasiqueue() 
	Q1.enqueue("BIMA (76)") 
	Q1.visualisasiqueue() 
	Q1.enqueue("GAJAYANA (72)")
	Q1.visualisasiqueue() 
	Q1.enqueue("ARGO LAWU (8)")
	Q1.visualisasiqueue() 
	Q1.enqueue("TAKSAKA (84)") 
	Q1.visualisasiqueue() 
	Q1.enqueue("ARGO LAWU (58A)")  
	Q1.visualisasiqueue()
	Q1.dequeue() 
	Q1.visualisasiqueue()
	Q1.dequeue() 
	Q1.visualisasiqueue()
	Q1.dequeue() 
	Q1.visualisasiqueue()
	Q1.dequeue() 
	Q1.visualisasiqueue() 
	Q1.dequeue() 
	Q1.visualisasiqueue()
	print('\n Tekan ENTER untuk kembali ke menu utama')
	input()
	menu()
