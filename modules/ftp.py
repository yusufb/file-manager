'''
Created on 8 Nis 2014

@author: ANIL
'''


def ftpConnection(adress,userName,password):
    import ftplib
    try:    
        
        ftp = ftplib.FTP(adress)
        ftp.login(userName,password)
        lines= ftp.nlst()
        print lines
        
    except ftplib.all_errors as e:
        print('An error has occured during ftp connection:',e)


ftpConnection("ftp.ygt.hol.es", "u255885439.pyhton", "123456")