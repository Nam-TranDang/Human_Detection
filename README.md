# Human_Detection

Step 1: configure the environment


python -m venv .venv (Shell)


Win: .venv/Scripts/activate (Shell)


Step 2: Download 


pip install ultralytics (Shell)


***Confugure CUDA - with NVDIA GPU (working on venv must install, although the machine supports CUDA)

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (Shell)



Step 3: import video --> python run.py to run the code