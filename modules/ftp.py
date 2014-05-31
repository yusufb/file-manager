'''
Created on 8 Nis 2014

@author: ANIL
'''


def ftpConnection(adress,port,username,password):
    import ftplib
    try:    
        
        ftp = ftplib.FTP()
        ftp.connect(adress, port)
        ftp.login(username,password)
        print('Connection established')
        lines= ftp.nlst()
        print lines
        return ftp
    except ftplib.all_errors as e:
        print('An error has occured during ftp connection:',e)



def uploadFile(ftpConn,filePath,fileName):
    import ftplib
    try:
        ftp=ftpConn
        file = open(filePath,'rb')                  # file to send
        ftp.storbinary('STOR '+fileName, file)  
        print "Upload succesful"
    except ftplib.all_errors as e:
        print('An error has occured during file upload:',e)    
        
def downloadFile(ftpConn,filePath,fileName):
    import ftplib
    try:
        ftp=ftpConn
        file = open(filePath,'wb').write              
        ftp.retrbinary('RETR '+fileName, file)  
        print "Download succesful"
    except ftplib.all_errors as e:
        print('An error has occured during file upload:',e)

        
         
