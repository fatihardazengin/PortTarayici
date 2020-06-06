 #!/usr/bin/python3

import socket
import subprocess
import sys
from datetime import datetime

# Ekrani Temizler.
subprocess.call('clear', shell=True)

# Kullanicidan giriş ister.
remoteServer    = input("Taramak için uzak bir ana bilgisayar adresi girin : ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# # Taramak üzere olduğumuz ana bilgisayar hakkında bilgi içeren güzel bir baslık yazdırır.
print ("-" * 60)
print ("Lütfen Bekleyin , Uzak adres taranıyor ...", remoteServerIP)
print ("-" * 60)

# Taramanın ne zaman başladığını kontrol eder.
t1 = datetime.now()

# Bağlantı noktalarını belirtmek için range fonksiyonunu kullanma (burada 1 ile 1024 arasındaki tüm bağlantı noktalarını tarar).
# Ayrıca hataları yakalamak için hata işleme koyuldu.
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Ctrl+C komutu ile çıkış yaptınız.")
    sys.exit()

except socket.gaierror:
    print ('Ana makine adı çözümlenemedi , Çıkış yapılıyor')
    sys.exit()

except socket.error:
    print ("Sunucuya bağlanılamadı.")
    sys.exit()

# Tekrar zaman kontrol ediliyor.
t2 = datetime.now()

# İşlemin ne kadar sürdüğünü saptamak amacıyla zaman tekrar hesaplanıyor
total =  t2 - t1

# Ekrana bilgi yazılıyor.
print ('Tarama şu sürede tamamlandı : ', total)