 #!/bin/bash 
 
python3 -m venv tf2_venv
source tf2_venv/bin/activate
pip install --upgrade pip
pip install tensorflow-gpu==2.0.0
pip install jupyter
pip install opencv-python==4.1.2
pip install gast==0.2.2
pip install matplotlib
pip install scipy==1.4.1