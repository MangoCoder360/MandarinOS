def updateCheck(sysVer):
        import easygui
        import urllib2
        raw = urllib2.urlopen('https://raw.githubusercontent.com/MangoCoder360/MandarinOS/master/Dependencies/latestWinVer.txt')
        latestVer = raw.read()
        if latestVer == sysVer:
                easygui.msgbox("You are up to date with the latest version of MandarinOS!","Update Checker Tool")
        else:
                easygui.msgbox('You are not on the latest version of MandarinOS. You can download the latest version from GitHub.','Update Checker Tool')
