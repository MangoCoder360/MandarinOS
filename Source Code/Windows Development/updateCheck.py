import sentry_sdk
sentry_sdk.init("https://7cba374024ca45eb9b4fdef818721b52@o464050.ingest.sentry.io/5516881", traces_sample_rate=1.0)
def updateCheck(sysVer):
        import easygui
        import urllib2
        raw = urllib2.urlopen('https://raw.githubusercontent.com/MangoCoder360/MandarinOS/master/Dependencies/latestWinVer.txt')
        latestVer = raw.read()
        if latestVer == sysVer:
                easygui.msgbox("You are up to date with the latest version of MandarinOS!","Update Checker Tool")
        else:
                easygui.msgbox('You are not on the latest version of MandarinOS. You can download the latest version from GitHub.','Update Checker Tool')
