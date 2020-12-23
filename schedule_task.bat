@echo off

::if "%1" == "h" goto begin 
::mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
::begin
cmd.exe /c "D:\Code\DAD\venv\Scripts\python.exe D:\Code\DAD\wechatdaily.py"
shutdown -s -t 1000