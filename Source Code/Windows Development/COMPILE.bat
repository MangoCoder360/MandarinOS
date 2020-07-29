pyinstaller -w -F -i mandarin.ico ActivationTool.py
pyinstaller -F -i mandarin.ico main.py
del /f main.spec
del /f ActivationTool.spec