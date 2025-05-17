Computer Vision Yolo11 - Object Detection
Description: Yolo11Nano from Ultralytics

Dataset: Visdrone from Ultralytics
---
## How to run:
###  Step 1: configure the environment

python -m venv .venv (Shell)

Run on terminal -> choose powershell.

Re-setup virtual environment (in case conflict code):

python -m venn .venv

(remember click add path "Yes" on the right corner of VSCode)

### Step 2: Download 

Run the .venv folder (on terminal) & select the interpreter

.venv/Scripts/Activate (then it must show the - greenstatus (venv))

Select the interpreter python'.venv':venv

If it got execution policy error, run:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Run the file (on terminal):

python run.py (CTRL + C on terminal --> to exit)

pip install ultralytics

***Confugure CUDA - with NVDIA GPU (working on venv must install, although the machine supports CUDA)

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (Shell)

### Step 3: import video --> python run.py to run the code
