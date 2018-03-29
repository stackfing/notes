# # coding=utf8
# import string
# import os 
# import time
# import re
# import math
# import sys
# from optparse import OptionParser

# print "Test by gongjia start..."


# parser = OptionParser()
# parser.add_option("-i", "--input", dest="input",action="store_true",help="input x y for each file by user")
# parser.add_option("-q", "--quality", dest="q",action="store",help="input xvid q arg",default="24")
# parser.add_option("-v", "--vcodec", dest="vcodec",action="store",help="input video codec",default="x264")
# parser.add_option("-n", "--noaudio", dest="an",action="store_true",help="no audio")
# parser.add_option("-p", "--preset", dest="preset",action="store",help="",default="")
# parser.add_option("-m", "--maxWidth", dest="maxWidth",action="store",help="input max width for output video",default="")
# parser.add_option("-f", "--fileType", dest="fileType",action="store",help="",default="mp4")
# parser.add_option("-o", "--ogg", dest="ogg",action="store_true",help="user ogg instead of aac",default="")
# parser.add_option("-3", "--mp3", dest="mp3",action="store_true",help="user mp3 instead of aac",default="")
# parser.add_option("-1", "--pad", dest="pad",action="store_true",help="pad to 16:9",default="")
# parser.add_option("-s", "--src", dest="srcD",action="store",help="source dir",default="/home/fing/test/python/kuaishou/source")
# parser.add_option("-t", "--target", dest="targetD",action="store",help="target dir",default="/home/fing/test/python/kuaishou/out")
# parser.add_option("-w", "--workdir", dest="workdir",action="store",help="work dir",default="/home/fing/test/python/kuaishou")
# parser.add_option("-e", "--split", dest="split",action="store_true",help="split to multiple file with size")
# parser.add_option("-d", "--splitsize", dest="splitsize",action="store",help="split to multiple file with size",default="2")#Minutes
# parser.add_option("-j", "--prefix", dest="prefix",action="store",help="target file name prefix",default="")

# (options, args) = parser.parse_args()

# if options.srcD==None or options.srcD[0:1]=='-':
#     print 'srcD Err, quit'
#     exit() 
# # if options.targetD==None or options.targetD[0:1]=='-':
# #     print 'targetD Err, quit'
# #     exit() 
# # if options.fileType==None or options.fileType[0:1]=='-':
# #     print 'fileType Err, quit'
# #     exit() 
# # if options.workdir==None or options.workdir[0:1]=='-':
# #     print 'workdir Err, quit'
# #     exit() 
    
# #遍历videoin下的文件
# for root,dirs,files in os.walk(options.srcD): 
#     for name in files:
#         name= name.replace('[','''\[''')#对文件名中的[进行转义
#         newname =name[0: name.rindex('.')]      
#         print "Test newname: " + newname
#         print "Test name: " + name

        
        
# #运行
#         cmd ='cd /home/fing/test/python/kuaishou'';mkdir -p ffm;  rm -f ffm/ffm.txt ; csh -c "(ffmpeg -i '+options.srcD+'/' +name+ ' >& ffm/ffm.txt)"; grep Duration ffm/ffm.txt'
#         print cmd
#         (si, so, se) = os.popen3(cmd)
#         t=so.readlines()
#         reg='''''Duration\:\s(\d+)\:(\d+)\:([\d\.]+)'''  
#         duration=0#second
#         for line in t:
#             result = re.compile(reg).findall(line)
#             for c in result:
#                 print 'split file to',options.splitsize,'minutes, Duration:',c[0],c[1],c[2]
#                 duration = int(c[0])*3600 + int(c[1])*60+float(c[2])
#                 nameLength=int(math.log(int(duration / (int(options.splitsize)*60)) )/math.log(10)) + 1
#                 for i in range(int(duration / (int(options.splitsize)*60)) + 1):
#                     print i
#                     _t = ''
#                     if duration>int(options.splitsize)*60*(i+1):
#                         _t = str(int(options.splitsize)*60)
#                     else:
#                         _t = str(duration-int(options.splitsize)*60*i)
#                     cmd ='csh -c "' + "cd "+options.workdir+";touch ffm/output.log;(ffmpeg -y -i "+options.srcD+"/"+name+" -codec: copy -ss "+str(i*int(options.splitsize)*60)+" -t "+_t+" "+options.targetD+"/"+options.prefix+newname+'_'+string.replace(('%'+str(nameLength)+'s')%str(i),' ','0')+"."+options.fileType + ' >>& ffm/output.log)"'
#                     print cmd
#                     (si, so, se) = os.popen3(cmd)
#                     for line in se.readlines() :#打印输出
#                         print line

import os
import re
import sys
import math
import time
import subprocess
from subprocess import run

def rename():
        i=0
        path="/home/fing/test/python/kuaishou/input";
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        for files in filelist:#遍历所有文件
            i=i+1
            Olddir=os.path.join(path,files);#原来的文件路径                
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                    continue;
            filename=os.path.splitext(files)[0];#文件名
            filetype=os.path.splitext(files)[1];#文件扩展名
            Newdir=os.path.join(path,str(i)+filetype);#新的文件路径
            os.rename(Olddir,Newdir)#重命名
rename()

class VideoDurationProcess:
    def __init__(self, filename):
        self.filename = filename
        return
    def preprocess(self, filename):
        #初始化参数
        vfilename = self.filename
        logname = ""
        durtxt = ""
        durtime = ""
        duration = 0
        #进程
        parameter = "ffmpeg -i " +sys.path[0]+"/"+vfilename + " -report"
        run(parameter,shell=True)
        logexists = False
        logdir = os.listdir()
        print ("读取视频信息...")
        print ("目前文件："+vfilename)
        while logexists == False:
            for logfile in logdir:
                extname = os.path.splitext(logfile)[1][1:]
                if extname == "log":
                    durfile = logfile
                    readlog = open(durfile,'rb')
                    content = readlog.read().decode("utf-8")
                    readlog.close()
                    os.remove(logfile)
                    readdur = content[content.rfind("Duration:"):content.rfind("start")-2]
                    print (readdur)
                    reg='Duration\:\s(\d+)\:(\d+)\:([\d\.]+)'
                    durtime = re.compile(reg).findall(readdur)
                    duration = int(durtime[0][0])*3600 + int(durtime[0][1])*60 + float(durtime[0][2])
                    print ("总时长："+str(duration)+"秒")
                    logexists = True
                    return duration
                else:
                    time.sleep(1)

class VideoCut:
    def __init__(self, filename):
        self.filename = filename
        return
    def process(self, filename, parttime):
        #初始化数据
        vfilename = "input/"+self.filename
        #可自定义输出后缀
        extvname = os.path.splitext(self.filename)[1][1:]
        #extvname = "mp4"
        durtime = VideoDurationProcess(vfilename).preprocess(vfilename)
        startat = 0
        #进程
        print ("预计分段数："+str(math.ceil(int(durtime) / int(parttime))))
        print ("-------------")
        for i in range(1,math.ceil(int(durtime) / int(parttime)+1)):
            print ("正在分割第"+str(i)+"段...")
            parameter = "ffmpeg -n -ss "+str(startat)+" -i "+vfilename+" -c copy -t "+str(parttime)+" output/"+self.filename+"_"+str(i)+"."+extvname
            run(parameter,shell=True)
            startat+=parttime
        print ("-----------已完成："+vfilename+"-----------")
        return
        

if __name__ == "__main__":
    #初始化介绍
    if os.path.exists("down.py"):
        print ("视频分割软件 by:Black")
        print ("-----------------------")
        print ("请将本文件及ffmpeg.exe放在同一目录下，")
        print ("并将要转换的视频放在input目录下")
    else:
        print ("请把ffmpeg放到本目录后重试...")
        pass
    #初始化参数

    if not os.path.exists("input"):
        os.mkdir("input")
    if not os.path.exists("output"):
        os.mkdir("output")
    parttime = input ("请输入每多少秒分一段：")
    print ("-----------------------")
    #获取文件&处理
    filesnames = os.listdir("input")
    for filename in filesnames:
        VideoCut(filename).process(filename, int(parttime))
    print ("全部处理完成！")
