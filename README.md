# Daily Attendance Destroyer (DAD)
A windows automation python program to destroy the daily temperature attendance of HNU.

## Requirements
* [lackey](https://pypi.org/project/Lackey/)
* pywin32
* pywincon


## Get Started
### step 1 
You need **login** the WeChat.exe beforehand.
### step 2 
You need **set star mark** for the HNU subscriptions account so the HNU acconut will be the top of subscribtions list.
### step 3
Add the schedule_task.bat to the **Windows Task Scheduler** for automatic execution and shutdown everyday. If your python script was made in a virtual env, you should append the content of the bat to the activate.bat of your venv. 
### step 4
Just leave the annoying daily attendance to the DAD and keep the PC running when you leave office everyday.
