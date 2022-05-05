from ftplib import FTP

hostname = 'ftp.unicamp.br' 
username = ''
password = ''
ftp = FTP(hostname)
ftp.login(user=username,passwd=password)
ftp.cwd('/') 
entries = [] 
ftp.dir(entries.append)


ftp.cwd('/pub/FreeBSD')
ftp.retrbinary("RETR " + 'README.TXT' ,open('arquivo_readme.txt', 'wb').write)

'''
ftp.cwd('/pub/FreeBSD/releases/ISO-IMAGES/13.0') 
iso_file = 'FreeBSD-13.0-RELEASE-i386-dvd1.iso'
ftp.retrbinary("RETR " + iso_file ,open('freebsd.iso', 'wb').write)
'''

ftp.close() 


