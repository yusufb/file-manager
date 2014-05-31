'''
Created on 8 Nis 2014

@author: ANIL
'''


def ftpConnection(adress,username,password):
    import ftplib
    try:    
        
        ftp = ftplib.FTP(adress)
        ftp.login(username,password)
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

def testFTPparams(host, port="", user="", passwd=""):
    host=unicode(host)
    port=unicode(port)
    user=unicode(user)
    passwd=unicode(passwd)
    print host, " - ", port, "", user, " - ", passwd
    ftpConnection(host + "" + port, user, passwd)
        
      
         
