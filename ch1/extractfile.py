import zipfile
zFile = zipfile.ZipFile('evil.zip')
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.split('\n')
    try:
        zFile.extract(pwd=password)
        print '[+] Password = '+password+'\n'
        exit(0)
    except Exception, e:
        pass
