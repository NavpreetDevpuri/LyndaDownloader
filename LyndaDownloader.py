import time
import os
import sys
import requests
#url='https://www.lynda.com/Python-tutorials/Programming-Fundamentals-Real-World/418249-2.html'
quality=" "
fromfolder=1
if len(sys.argv)==5:
    fromfolder=int(sys.argv[4])
if len(sys.argv)>=4:
    url = sys.argv[1]
    savedir = sys.argv[2] + "Lynda"
    quality=sys.argv[3]
elif len(sys.argv) >= 3:
    url = sys.argv[1]
    savedir = sys.argv[2] + "Lynda"
elif len(sys.argv)>=2:
    url=sys.argv[1]
    savedir = sys.argv[0][:sys.argv[0].rfind('/')] + "Lynda"
else:
    url = input("Enter Lynda.com course link: ")
    savedir = sys.argv[0][:sys.argv[0].rfind('/')] + "Lynda"
#print(savedir, url, quality )
start_time = time.time()
print("Setting up...")
headerstr='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: keep-alive
Cookie: bcookie=4e1f52581ac449209ab75375714cb66a64050a3c29d745b3bfa5c45257519189; throttle-f9151a904e07fa0812b7b9fb20b6f1ab=1; throttle-66ae19c25d337eab52ef80bb97b39dd7=1; throttle-15140b06309e901a9d100062a23c334c=0; throttle-7566ffb605d4cb8c15225d8859a6efd3=1; throttle-b8b96eed8d81f42a88aadaadc5139c25=1; throttle-d3ebbd09ec7ecff8c4948ff79599614d=1; throttle-9620ede73ab0b3b8d0fe1e62763ad939=1; throttle-ad15fee1459e8f3e1ae3d8d711f77883=1; throttle-20fc2dfb0a81016faeebb960e94da216=1; _ga=GA1.2.1272953846.1560319018; _gid=GA1.2.773799910.1560319018; throttle-2fa0e9b608dffa03090202330a823d2c=1; throttle-54c678a5add39d58a7d7411cae569603=1; show-member-tour-cta=true; __utmz=203495949.1560319071.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); throttle-7f0c15d211a720cccfeff5e84db0ec6e=1; SSOLogin=OrgUrl=http%3A%2F%2Fwww.lynda.com%2Fportal%2Fsip%3Forg%3Dhoustonlibrary.org&OrgName=Houston%20Public%20Library; throttle-2b03d60a3a4380742663b5f4066e4d2a=1; player_settings_10663212_7=player_type=2&video_format=2&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=540; throttle-5348dd4a563290f2f066ced19befea6a=2; throttle-34d6c36979b1bc5f735cf8382b5963ae=1; throttle-81caf7c4bbc10c18b29b105cfcbcdbee=1; throttle-b8b1cb3ef236f57532c515db9614be44=1; throttle-a5ca6acbd2f547f2914c0b113231bee3=1; throttle-47481a8f590db61e7b4703e070ade640=1; throttle-9ecc4e578ac856334c0a44bd43f10619=1; throttle-257d98eb91c98e6e0656104d4aa74214=1; throttle-85975e5888b0a2a3d27c273fd5637879=1; throttle-cb8048294d8a62ec98a5d38754e4a964=1; throttle-39d6522a4d2286f461ab505a0559a74a=0; throttle-fcc41b5952df7ea0746eff3c71b72bc7=1; throttle-bf01e020137cb85eaa7a5e6a2f331834=1; throttle-cc6e24142c9b2f691b86349a86409bdb=1; tcookie=43d5b32a-326e-4b0e-9742-8530ccaede27; throttle-1541cf51b317649a0e2e58b81f433f80=1; signin-tooltip=2; player=%7B%22volume%22%3A0.8%2C%22muted%22%3Afalse%2C%22quality%22%3A720%2C%22continuousPlay%22%3Atrue%7D; __utmv=203495949.|1=Persona=Enterprise-User-Status-Active-Type-Regular=1^3=Product=lyndaLibrary=1; recentSearches=%5B%7B%22Name%22%3A%22javascript%22%7D%2C%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctjavascript%20essential%5Cn%5Ct%5Ct%5Ct%22%2C%22Type%22%3A4%7D%2C%7B%22Name%22%3A%22javascript%20essential%22%7D%5D; ncp=1; plugin_list=; __utma=203495949.1272953846.1560319018.1560449641.1560491103.4; __utmc=203495949; player_settings_0_7=player_type=2&video_format=2&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=0; LyndaAccess=LyndaAccess=6/13/2019 10:45:16 PM&p=0&data=9,12/11/2017,1,191505; LyndaLoginStatus=Member-Logged-In; litrk-srcveh=srcValue=or-search&vehValue=www.google.com&prevSrc=direct/none&prevVeh=direct/none; utag_main=v_id:016b4a42c83c000bf32fa93c08d30306800160600086e$_sn:11$_ss:1$_st:1560496476154$_pn:1%3Bexp-session$ses_id:1560494676154%3Bexp-session; token=614d2ff8-5dc0-42ae-bb5e-01988d387ffa,96fb3e9dd29bc628f1c848c65aabc83c,AdQ8oJQ6Yi6egY6LbGm2HtQ5xnrj7GsvQCwG+adCCt8QdYGd+Ef8Mk98/3vIJXoJki6kg/ZHiAHdDokwrNEISGINzDSh5RioYvBzSWqDXYSFT1HMz1rlFal2p++PsQdBlv15dzyJV75L6x+HWI7Ysg==; NSC_ed11_xxx-iuuqt_wt=ffffffff096d9e5145525d5f4f58455e445a4a423661'''
sp=headerstr.split('\n')
h={}
for i in sp:
    j=i.split(': ')
    h[j[0]]=j[1]

def validname(name):
    return name.replace('|', '').replace('>', '').replace('<', '').replace('"', '').replace('?', '').replace('*', '').replace(':', '').replace('/', '').replace('\\', '')


qualities=["360p","540p","720p"]
downloadedsize=0
def download():
    print("Downloading...")
    global data,courseId,courseName,exFileId,exFileName,exFileLink,quality,qualities,downloadsize,downloadedsize,isExFile
    #os.makedirs(savedir, exist_ok=True)
    os.makedirs(savedir+"/"+courseName+" "+qualities[quality], exist_ok=True)
    if isExFile:
        print(" [" + str(bytesToMb(getFileSize(exFileLink, h))) + "Mb] Exercise File: " + exFileName)
        dowloadFile(savedir+"/"+courseName+" "+qualities[quality]+"/"+exFileName+".zip",exFileLink,h)
    for i in range(data.__len__()):
        folderName = data[i][0]
        os.makedirs(savedir+"/"+courseName+" "+qualities[quality]+"/"+folderName, exist_ok=True)
        print(folderName + ":")
        for j in range(data[i][1].__len__()):
            videolink = data[i][1][j][1][1][quality]
            videoname = data[i][1][j][0]
            sizet=bytesToMb(data[i][1][j][1][2][quality])
            #downloadedsize+=sizet
            print("%17s   %s.mp4 " % ("["+qualities[quality]+": "+str(sizet)+"Mb]", videoname))
            dowloadFile(savedir+"/"+courseName+" "+qualities[quality]+"/"+folderName+"/"+videoname+".mp4",videolink)
    print(courseName+" "+qualities[quality]+": ["+str(round(downloadedsize,2))+"Mb]")

def bytesToMb(a):
    return round(a/1000000,2)

def getFileSize(link,h=None):
    r = requests.request('GET', link, headers=h, stream=True)
    return int(r.headers['Content-length'])

def dowloadFile(name,link,header=None):
    global downloadedsize,downloadsize
    r = requests.request('GET', link, headers=header, stream=True)
    f = open(name, 'wb')
    size=int(r.headers['Content-length'])
    sizet=0
    for chunk in r.iter_content(chunk_size=8192):
        s=len(chunk)
        sizet+=s
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
        status = round(sizet / size * 100, 3)
        downloadedsize+=s
        alloverp=round(downloadedsize/downloadsize*100,3)
        #print('\r     ' + str(status) + "% (" + str(round(sizet / 1000000, 2)) + "Mb/" + str(
            #round(size / 1000000, 2)) + "Mb)      [Allover:"+str(alloverp)+"% ("+str(round(bytesToMb(downloadedsize),2))+"Mb/"+str(round(bytesToMb(downloadsize),2))+"Mb)]", end=' ', flush=True)

        print('\r %.2f%% (%.2fMb/%.2fMb)  Allover:%.2f%% (%.2fMb/%.2fMb)' % (status , bytesToMb(sizet) , bytesToMb(size), alloverp, round(bytesToMb(downloadedsize),2),round(bytesToMb(downloadsize), 2)), end=' ', flush=True)

    print(" ")
    f.close()
#dowloadFile("yessss.mp4",'https://files3.lynda.com/secure/courses/661762/iphone_MP4/661762_01_03_XR30_MeasuringTime.mp4?cIYDwkTAaaR6fXWhNQPXMsxuWdPyB5j_vUkisfRv_NzNM_Ul6Gk73s1KkX7WsGXMDSSwZI-u5mp0Mqz-y5vYeZanotmJpShRosyCQR4tWvaySgJ_6QR8DGFc9QIyAqjeacZdP5hbW3wgGjzrxUD7YQEazgyXUP8SPrJ8b9geSWsVn3o49EdqPX8&c3.ri=3775934228715563001')
print("Connecting to Lynda.com...")
r = requests.request('GET', url, headers=h, stream=True)
html=str(r.content)
print("Collecting information...")
courseName=html[html.index('<h1'):html.index('</h1')].split('>')[1]
courseId=html[html.index("/"):html.index('ios')].split('>')[1][88:-3]
print("###"+courseName+"#####")
isExFile=True
try:
    start=html.index("exercise/")
except:
    isExFile=False
if isExFile:
    i = start
    while (True):
        i += 1
        if html[i] != '"':
            continue
        else:
            break
    exFileName = "exFile " + validname(courseName.replace(" ", "_"))
    exFileId = html[start + 9:i]
    exFileLink = 'https://www.lynda.com/ajax/course/' + courseId + '/download/exercise/' + exFileId
    exfilesize = getFileSize(exFileLink, h)
    print("Exercise File: " + exFileName + "   [" + str(bytesToMb(exfilesize)) + "Mb]")
list=html[html.index('course-toc toc-container autoscroll'):html.index('class="show-all"><span class="more ga"')].split('<li role="presentation"')
data=[]
t360=0
t540=0
t720=0
totalVideos=0
for i in range(fromfolder,list.__len__()):
    folderName=list[i][list[i].index('<h4'):list[i].index('</h4')].split('>')[1]
    print(folderName+":")
    data.append([validname(folderName),[]])
    videosList = list[i].split('row toc-items')[1].split('<li')
    totalVideos+=videosList.__len__()-1
    for j in range(1,videosList.__len__()):
        videoid = videosList[j][videosList[j].index('"') + 1:videosList[j].index('c') - 2]
        videoname = videosList[j][videosList[j].index('<a'):videosList[j].index('</a')].split('\\n')[1]
        for k in range(0, videoname.__len__()):
            if videoname[k] == " ":
                continue
            else:
                videoname = videoname[k:]
                break
        videoname = str(j) + ". " + videoname
        data[i-fromfolder][1].append([validname(videoname),[]])
        data[i-fromfolder][1][j-1][1].append(videoid)
        videodata=requests.request('GET','https://www.lynda.com/ajax/course/'+courseId+'/'+videoid+'/play', headers=h,stream=True).json()
        data[i - fromfolder][1][j - 1][1].append(
            [videodata[0]['urls']['360'], videodata[0]['urls']['540'], videodata[0]['urls']['720']])
        temp360=getFileSize(videodata[0]['urls']['360'])
        temp540=getFileSize(videodata[0]['urls']['540'])
        temp720=getFileSize(videodata[0]['urls']['720'])
        t360+=temp360
        t540+=temp540
        t720+=temp720
        data[i - fromfolder][1][j - 1][1].append([temp360,temp540, temp720])
        print("%45s   %s.mp4 " %("[360p:"+str(bytesToMb(temp360))+"Mb, 540p:"+str(bytesToMb(temp540))+"Mb, 720p:"+str(bytesToMb(temp720))+"Mb]",videoname))
if isExFile:
    print("Exercise File: "+exFileName+"   ["+str(bytesToMb(exfilesize))+"Mb]")
print(courseName+": Total Videos: "+str(totalVideos)+"    [360p:"+str(bytesToMb(t360))+"Mb, 540p:"+str(bytesToMb(t540))+"Mb, 720p:"+str(bytesToMb(t720))+"Mb ]")
data[0][0]="0. "+data[0][0]
while(not (quality=="0" or quality=="1" or quality=="2")):
        quality=input("Enter video quality (0 for 360p, 1 for 540p or 2 for 720p) : ")
quality=int(quality)
if quality==0:
    downloadsize=t360
elif quality==1:
    downloadsize=t540
else:
    downloadsize=t720
if isExFile:
    downloadsize+=exfilesize
download()
print("time elapsed: {:.2f}s".format(time.time() - start_time))