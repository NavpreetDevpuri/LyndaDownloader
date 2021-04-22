###### By Navpreet Devpuri

**Notes**: 
 1. When using `LyndaDownloaderLearningPaths.py` then make sure you opened that learning path and clicked on button `Start learning`.
 2. Run Python script LyndaDownloader.py :) and download 'Exercise Files' manually.
 3. If some error occurred or stoped while downloading then just restart python script it will repause download.
 4. If you started downloading some course then finish it as soon as possible because after some time link will be expire.

### Step 1) register new card from [here](https://find.sonomalibrary.org/custom/web/registration/index.html) and get your card number. if you have an account then continue from step 3.
### Step 2) login by using card number and password [here](https://www.lynda.com/portal/sip?org=sonomalibrary.org)
### Step 3) open chrome's devloper option by pressing ctrl + shift + I then open networking tab and play any video then find 'play' in 'Request Headers' and copy cookies (bcooklie=....etc)
![step 3](https://raw.githubusercontent.com/NavpreetDevpuri/LyndaDownloader/master/screenshots/08.jpg)

## On windows
1. Download and install ***Python3.x.x*** from [link](https://www.python.org/downloads/windows/)
2. Make sure to check ***Add Python3 to PATH*** on first step of installation.
3. Open CMD and run command `pip3 install requests` or `pip install requests`

4. Know you can run python script on Windows

##### For example : 
```python 
python 'C:\Users\navpreetdevpuri\Downloads\LyndaDownloader.py'
or
python 'C:\Users\navpreetdevpuri\Downloads\LyndaDownloader.py' -url 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' -savedir 'C:\Users\navpreetdevpuri\Downloads\' -q 2 
```


## On Android (Its better to use Pydroid 3 instead of Termux)
##### You can also run this script in android (How to run python script on android ?)
1. Download and install **Termux** app. (remember to give *storage permission* from phone's settings and *turn off battery optimization* for Termux app to make app run long)
2. Run following commads : 
   -  `apt-get update`
   -  `apt-get install python`
   -  `pip install requests`
3. Know you can run python script on android<br>
-savedir or -sd argument is compulsory for android. 
##### For example : 
```python 
python '/storage/emulated/0/Download/LyndaDownloader.py' -savedir '/storage/emulated/0/Download/'
or
python '/storage/emulated/0/Download/LyndaDownloader.py' -url 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' -savedir '/storage/emulated/0/Download/' -q 2 
```


## On Linux
1. Run following commads to install Python: 
   -  `sudo apt-get update`
   -  `sudo apt-get -y install python3`
   -  `sudo apt-get -y install python3-pip`
   -  `sudo pip3 install requests` or `pip install requests`
2. Know you can run python script on Linux

##### For example : 
```python 
python3 '/home/navpreetdevpuri/Downloads/LyndaDownloader.py'
or
python3 '/home/navpreetdevpuri/Downloads/LyndaDownloader.py' -url 'https://www.lynda.com/C-tutorials/C-Essential-Training/772322-2.html' -sd '/home/navpreetdevpuri/Downloads/' -quality 720p 
```

### Optional arguments with python script
***If you run script without this arguments then It will ask this things on run time***<br/>
1. ***-url*** : **Url link** of Lynda course.
2. ***-savedir or -sd*** : Directory **location (Full path)** on your system where you want to save files (by default set to the same location as LyndaDownloader.py).
3. ***-quality or -q*** : **Video quality** (360p or 0, 540p or 1, 720p or 2).
4. ***-fromfolder or -ff*** : In case you want to download only few topics by entring **starting topic number** (by default set to 1 which means start download from 1st topic of course).
