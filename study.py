#coding: utf-8
#!/usr/bin/python
#-*- coding: utf-8 -*-
#下载一段时间的GNSS n文件
from ftplib import FTP

ftp = FTP()
ftp.connect("igs.gnsswhu.cn")
ftp.login()
print(ftp.welcome)

# 配置数据
year='2014'#年份
start='1'#开始年积日
end='2'#结束年积日
station="abpo"#测站名称
start=int(start)
end=int(end)
for i in range(start,end+1):
    print(i)
    ii=str(i)
    ii=ii.zfill(3)# zfill对字符串前补零   "RETR "
    filename=(station+ii+'0'+'.'+year[-2:]+'n.Z')
    print(filename)
    find=('/pub/gps/data/daily/'+year+'/'+str(ii)+'/'+year[-2:]+'n')
    print(find)
    try:
       ftp.cwd(find)
       fp = open(filename,'wb')
       ftp.retrbinary("RETR "+filename,fp.write)  #下载FTP文件
    except:
        print(下载数据+filename+失败)


    # ftp.login()
    # ftp.cwd(find)
    # fp = open(filename,'wb')
    # ftp.retrbinary(filename,fp.write)  #下载FTP文件









# ftp.cwd("/pub/gps/data/daily/2014/016/14n")
# #ftp.dir()
# list=ftp.nlst()

#获取文件索引和文件名
# for index,ai in enumerate(list):
#     print(index,ai)


#print(list)
#fp = open("abpo0160.14n.Z",'wb')
#ftp.retrbinary("RETR abpo0160.14n.Z",fp.write)  #下载FTP文件











