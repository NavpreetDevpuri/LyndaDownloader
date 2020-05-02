import time
import os
import sys
import requests
import html
cookies = 'bcookie=c535c4dcac2948ada83a1bfba1e319d1a2c9face066045578e9f130be865efcd; throttle-f9151a904e07fa0812b7b9fb20b6f1ab=1; litrk-srcveh=srcValue=direct/none&vehValue=direct/none&prevSrc=&prevVeh=; throttle-b8b96eed8d81f42a88aadaadc5139c25=1; throttle-66ae19c25d337eab52ef80bb97b39dd7=1; throttle-54c678a5add39d58a7d7411cae569603=1; throttle-7566ffb605d4cb8c15225d8859a6efd3=1; throttle-20fc2dfb0a81016faeebb960e94da216=1; show-member-tour-cta=true; throttle-7f0c15d211a720cccfeff5e84db0ec6e=1; SSOLogin=OrgUrl=https%3A%2F%2Fwww.lynda.com%2Fportal%2Fsip%3Forg%3Ddetroitpubliclibrary.org&OrgName=Detroit%20Public%20Library; throttle-2b03d60a3a4380742663b5f4066e4d2a=1; player_settings_1995203661_7=player_type=2&video_format=2&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=540; throttle-5348dd4a563290f2f066ced19befea6a=2; throttle-34d6c36979b1bc5f735cf8382b5963ae=1; throttle-d3ebbd09ec7ecff8c4948ff79599614d=1; throttle-81caf7c4bbc10c18b29b105cfcbcdbee=1; throttle-3c6decaab331b0e589231f32fc4b9a84=1; throttle-b8b1cb3ef236f57532c515db9614be44=1; _ga=GA1.2.1213302327.1584204133; player=%7B%22volume%22%3A0.8%2C%22muted%22%3Afalse%7D; throttle-e0cb8e4541d2401ae2437d4836b8d8cd=1; throttle-9ecc4e578ac856334c0a44bd43f10619=1; throttle-85975e5888b0a2a3d27c273fd5637879=1; throttle-cb8048294d8a62ec98a5d38754e4a964=1; throttle-fcc41b5952df7ea0746eff3c71b72bc7=1; throttle-bf01e020137cb85eaa7a5e6a2f331834=1; throttle-cc6e24142c9b2f691b86349a86409bdb=1; tcookie=564c1c56-cb0d-435e-8b47-a72dff0d6250; throttle-9620ede73ab0b3b8d0fe1e62763ad939=1; throttle-ad15fee1459e8f3e1ae3d8d711f77883=1; NSC_tw5_xxx-iuuqt_wt=ffffffff096e9e2a45525d5f4f58455e445a4a423661; _gid=GA1.2.1114134994.1584342457; throttle-2fa0e9b608dffa03090202330a823d2c=1; signin-tooltip=1; plugin_list=; player_settings_0_7=player_type=2&video_format=2&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=0; token=a9523864-8c17-4847-a72f-0f63989acc17,0c63883c20557352fcb3ba228d73ecea,IfYnDGcuyChO6wF8OfaJq3Z8vnRNdLXAtfD71KAiaWxQZl0Z3FLG8MW/FBBflQRtgp3uycgluQiYIYl1d0x0lYdCYFJ8mhXIfWobiD+AZk2JG8ARlBJ53cn0rJQe8yoXHbBbHEC4zS4rhSJ59EmIQA==; LyndaAccess=LyndaAccess=3/16/2020 12:07:53 AM&p=0&data=9,11/8/2020,1,191505; LyndaLoginStatus=Member-Logged-In; _gat=1; recentSearches=%5B%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctpremiere%20pro%5Cn%5Ct%5Ct%5Ct%22%2C%22Type%22%3A4%7D%2C%7B%22Name%22%3A%22premiere%20pro%22%7D%2C%7B%22Name%22%3A%22%5Cn%5Ct%5Ct%5Ct%5Ct%5Cn%5Ct%5Ct%5Ct%5Ctarduino%5Cn%5Ct%5Ct%5Ct%22%2C%22Type%22%3A4%7D%5D; ncp=1'

#import readline
cookies = input("Enter cookies string: ")
#readline.parse_and_bind("control-v: paste")
# url='https://www.lynda.com/Python-tutorials/Programming-Fundamentals-Real-World/418249-2.html'
quality = " "
url = " "
savedir = " "
print("Made by NavpreetDevpuri.")
print("Enjoy ;)")
fromfolder = 1
# print(sys.argv)
arglen = len(sys.argv)
i = 0;
while (i < arglen - 1):
    i += 1
    if sys.argv[i] == "-url":
        url = sys.argv[i + 1]
        i += 1
    elif sys.argv[i] == "-savedir" or sys.argv[i] == "-sd":
        savedir = sys.argv[i + 1]
        i += 1
    elif sys.argv[i] == "-quality" or sys.argv[i] == "-q":
        quality = sys.argv[i + 1]
        if quality == "2" or quality == "1" or quality == "0": continue
        if quality == "720p":
            quality = "2"
        elif quality == "540p":
            quality = "1"
        elif quality == "320p":
            quality = "0"
        i += 1
    elif sys.argv[i] == "-fromfolder" or sys.argv[i] == "-ff":
        fromfolder = int(sys.argv[i + 1])
        i += 1
    else:
        print(
            "invalid argumnets. Read about arguments on github: https://github.com/NavpreetDevpuri/LyndaDownloader\n Try angain :)")

if url == " ":
    print("Eg. https://www.lynda.com/Python-tutorials/Programming-Fundamentals-Real-World/418249-2.html")
    url = input("Enter Lynda.com course link: ")
if savedir == " ":
    savedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Lynda")
# print(savedir)
start_time = time.time()
print("Setting up...")
h = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookies}

def validname(name):
    return name.replace('|', '').replace('>', '').replace('<', '').replace('"', '').replace('?', '').replace('*',
                                                                                                             '').replace(
        ':', '').replace('/', '').replace('\\', '').replace("\r","").replace("\n","").replace("\t","")


qualities = ["360p", "540p", "720p"]
downloadedsize = 0


def download(nn=0):
    global data, courseName, quality, qualities, downloadsize, downloadedsize
    try:
        filer = open("temp.txt", "r")
        cont = filer.read()
        filer.close()
    except:
        cont=''
    temp=cont.split("\n")
    cont=''
    for i in range(temp.__len__()-1,-1,-1):
        if temp[i]!='':
            cont=temp[i]
            break
    #print(cont)
    tcourseName=""
    if cont != "":
        temp = cont.split(",")
        tcourseName = temp[0]
        downloadedsize = int(temp[1])
        nn = int(temp[2])
    if tcourseName != validname(courseName):
        nn=0
        downloadedsize=0
        filer = open("temp.txt", "w")
        filer.close()
    filew=open("temp.txt","a+")
    print("Downloading...")
    ct=nn
    courseName = validname(courseName)
    coursedir = os.path.join(savedir, courseName + " " + qualities[quality])
    os.makedirs(coursedir, exist_ok=True)
    mm=0
    for i in range(data.__len__()):
        folderName = validname(data[i][0])
        folderdir = os.path.join(coursedir, folderName)
        os.makedirs(folderdir, exist_ok=True)
        print(folderName + ":")
        for j in range(data[i][1].__len__()):

            try:
                data[i][1][j][1][1][quality]
            except:
                videolink = data[i][1][j][1][1][quality - 1]
                videoname = data[i][1][j][0]
                sizet = bytesToMb(data[i][1][j][1][2][quality - 1])
                print("%17s   %s.mp4 " % ("[" + qualities[quality - 1] + ": " + str(sizet) + "Mb]", videoname))
            else:
                videolink = data[i][1][j][1][1][quality]
                videoname = data[i][1][j][0]
                sizet = bytesToMb(data[i][1][j][1][2][quality])
                print("%17s   %s.mp4 " % ("[" + qualities[quality] + ": " + str(sizet) + "Mb]", videoname))
            if mm < nn:
                mm = mm+1
                continue
            dowloadFile(os.path.join(folderdir, videoname + ".mp4"), videolink)
            ct=ct+1
            #print('downloadedsize='+str(downloadedsize), "ct=",ct)
            filew.write(courseName+","+str(downloadedsize)+","+str(ct)+"\n")
            filew.close()
            filew = open("temp.txt", "a+")
    print(courseName + " " + qualities[quality] + ": [" + str(round(bytesToMb(downloadedsize), 2)) + "Mb]")
    filew.close()


def bytesToMb(a):
    return round(a / 1000000, 2)


def getFileSize(link, h=None):
    r = requests.request('GET', link, headers=h, stream=True)
    return int(r.headers['Content-length'])


def dowloadFile(name, link, header=None):
    global downloadedsize, downloadsize
    r = requests.request('GET', link, headers=header, stream=True)
    f = open(name, 'wb')
    size = int(r.headers['Content-length'])
    sizet = 0
    for chunk in r.iter_content(chunk_size=8192):
        s = len(chunk)
        sizet += s
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
        status = round(sizet / size * 100, 3)
        downloadedsize += s
        alloverp = round(downloadedsize / downloadsize * 100, 3)
        print('\r %.2f%% (%.2fMb/%.2fMb)  Allover:%.2f%% (%.2fMb/%.2fMb)' % (
        status, bytesToMb(sizet), bytesToMb(size), alloverp, round(bytesToMb(downloadedsize), 2),
        round(bytesToMb(downloadsize), 2)), end=' ', flush=True)

    print(" ")
    f.close()


def getVideosLinks():
    print("Getting videos details...")
    global fromfolder, data, htmlstr, t360, t540, t720
    for i in range(data.__len__()):
        folderName = data[i][0]
        print(folderName + ":")
        # data.append([validname(folderName), []])
        for j in range(data[i][1].__len__()):
            videoid = data[i][1][j][1][0]
            videoname = data[i][1][j][0]
            # print(videoname,videoid)
            videodata = requests.request('GET',
                                         'https://www.lynda.com/ajax/course/' + courseId + '/' + videoid + '/play',
                                         headers=h).json()
            try:
                videodata[1]['urls']['720']
            except:
                try:
                    videodata[1]['urls']['540']
                except:
                    data[i][1][j][1].append(
                        [videodata[1]['urls']['360']])
                    temp360 = getFileSize(videodata[1]['urls']['360'])
                    temp540 = temp360
                    temp720 = temp360
                    print("%45s   %s.mp4 " % (
                        "[360p:" + str(bytesToMb(temp360)) + "Mb]", videoname))
                else:
                    data[i][1][j][1].append(
                        [videodata[1]['urls']['360'], videodata[1]['urls']['540']])
                    temp360 = getFileSize(videodata[1]['urls']['360'])
                    temp540 = getFileSize(videodata[1]['urls']['540'])
                    temp720 = temp540
                    print("%45s   %s.mp4 " % (
                        "[360p:" + str(bytesToMb(temp360)) + "Mb, 540p:" + str(bytesToMb(temp540)) + "Mb]", videoname))
            else:
                data[i][1][j][1].append(
                    [videodata[1]['urls']['360'], videodata[1]['urls']['540'], videodata[1]['urls']['720']])
                temp360 = getFileSize(videodata[1]['urls']['360'])
                temp540 = getFileSize(videodata[1]['urls']['540'])
                temp720 = getFileSize(videodata[1]['urls']['720'])
                print("%45s   %s.mp4 " % (
                    "[360p:" + str(bytesToMb(temp360)) + "Mb, 540p:" + str(bytesToMb(temp540)) + "Mb, 720p:" + str(
                        bytesToMb(temp720)) + "Mb]", videoname))

            t360 += temp360
            t540 += temp540
            t720 += temp720
            data[i][1][j][1].append([temp360, temp540, temp720])
    print(" ")
    if isExFile:
        print("Exercise File: " + exFileName + "   [" + str(bytesToMb(exfilesize)) + "Mb]")
    print(courseName)
    print(" Total Videos : " + str(totalVideos))
    print("    [360p:" + str(bytesToMb(t360)) + "Mb, 540p:" + str(
        bytesToMb(t540)) + "Mb, 720p:" + str(bytesToMb(t720)) + "Mb]")
    data[0][0] = "0. " + data[0][0]
    print(" ")


def getCoursedetails():
    global totalVideos, data
    for i in range(fromfolder, list.__len__()):
        folderName = html.unescape(list[i][list[i].index('<h4'):list[i].index('</h4')].split('>')[1])
        print(folderName + ":")
        data.append([(validname(folderName)), []])
        videosList = list[i].split('row toc-items')[1].split('<li')
        totalVideos += videosList.__len__() - 1
        for j in range(1, videosList.__len__()):
            temp = videosList[j].index('video-duration')
            videoduration = videosList[j][temp + 16:temp + 30].split('<')[0]
            videoid = videosList[j][videosList[j].index('"') + 1:videosList[j].index('c') - 2]
            videoname = (videosList[j][videosList[j].index('<a'):videosList[j].index('</a')].split('\\n')[
                            1]).split("\\")[0].strip() + " (" + videoduration + ")"
            for k in range(0, videoname.__len__()):
                if videoname[k] == " ":
                    continue
                else:
                    videoname = videoname[k:]
                    break
            videoname = str(j) + ". " + html.unescape(videoname)
            # print(videoname, videoid)
            data[i - fromfolder][1].append([validname(videoname), []])
            data[i - fromfolder][1][j - 1][1].append(videoid)
            print("   " + videoname)
    # print("geed "+str(data))


print("Connecting to Lynda.com...")
r = requests.request('GET', url, headers=h, stream=True)
htmlstr = str(r.content)
print("Collecting information...")
temp = htmlstr.index('timeRequired')
courseDuration = htmlstr[temp:temp + 55].split('>')[1].split('<')[0]
temp = htmlstr.index('data-course="')
courseName = validname(html.unescape(htmlstr[temp + 13:temp + 13 + htmlstr[temp + 13:temp + 144].index('"')] + " (" + courseDuration + ")"))
courseId = htmlstr[htmlstr.index("/"):htmlstr.index('ios')].split('>')[1][88:-3]
print("###" + courseName + "#####")
print("Getting course details...")
isExFile = True
try:
    start = htmlstr.index("exercise/")
except:
    isExFile = False
if isExFile:
    i = start
    while (True):
        i += 1
        if htmlstr[i] != '"':
            continue
        else:
            break
    exFileName = "exFile " + validname(courseName.replace(" ", "_"))
    exFileId = htmlstr[start + 9:i]
    exFileLink = 'https://www.lynda.com/ajax/course/' + courseId + '/download/exercise/' + exFileId
    exfilesize = getFileSize(exFileLink, h)
    print("Exercise File: " + exFileName + "   [" + str(bytesToMb(exfilesize)) + "Mb]")
list = htmlstr[
       htmlstr.index('course-toc toc-container autoscroll'):htmlstr.index('class="show-all"><span class="more ga"')].split(
    '<li role="presentation"')
data = []
t360 = 0
t540 = 0
t720 = 0
totalVideos = 0
getCoursedetails()

try:
    filer = open("temp.txt", "r")
    cont=filer.read()
    filer.close()
except:
    cont=""
tcourseName=""
#print(cont)
if cont != "":
    tcourseName = cont.split(",")[0]
if tcourseName != courseName:
    getVideosLinks()
    file = open("data.txt", "w")
    file.write(str(data) + "\n")
    file.write(str(t360) + "," + str(t540) + "," + str(t720) + "\n")
    file.close()
    filew = open("temp.txt", "w")
    filew.write(courseName + "," + str(0) + "," + str(0)+"\n")
    filew.close()


#if isExFile:
    #downloadsize += exfilesize
# print(data)
#download()

file=open("data.txt", "r")
contents =file.read()
file.close()
temp = contents.split("\n")
data = eval(temp[0])

t360, t540, t720 = temp[1].split(",")
t360=int(t360)
t540=int(t540)
t720=int(t720)
print("    [360p:" + str(bytesToMb(t360)) + "Mb, 540p:" + str(
        bytesToMb(t540)) + "Mb, 720p:" + str(bytesToMb(t720)) + "Mb]")
while (not (quality == "0" or quality == "1" or quality == "2")):
    quality = input("Enter video quality (0 for 360p, 1 for 540p or 2 for 720p) : ")
quality = int(quality)

if quality == 0:
    downloadsize = t360
elif quality == 1:
    downloadsize = t540
else:
    downloadsize = t720
download()
file = open("data.txt", "w")
file.close()
filew = open("temp.txt", "w")
filew.close()

print("time elapsed: {:.2f}s".format(time.time() - start_time))
input("Press any key to exit :)")
