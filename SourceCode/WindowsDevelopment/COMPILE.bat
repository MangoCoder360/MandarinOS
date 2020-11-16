pyinstaller -w -F -i Assets\mandarin.ico ActivationTool.py
pyinstaller -F -i Assets\mandarin.ico main.py
del /f main.spec
del /f ActivationTool.spec
del /Q build