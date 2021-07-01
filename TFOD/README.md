## Summary
  - [Installation and Usage](#installation-and-usage)
  - [Sample Project](#sample-project)
  - [References](#references)
  
## Installation and Usage
1. Open Anaconda command prompt
2. Create new anaconda environment
```
conda create -n "tfod_project" python==3.8
```
3. Activate anaconda environment
```
conda activate "tfod_project"
```
4. Open the project
```
git clone https://github.com/AparGarg99/Tutorials.git
cd Tutorials/TFOD
```
5. [OPTIONAL] Install the required dependencies
```
pip install -r requirements.txt
```
&nbsp;&nbsp;&nbsp;&nbsp;*It's advisable to install the libraries on the go.*

6. Open jupyter notebook
```
jupyter notebook
```
7. Collect images using [1_Image Collection.ipynb](https://github.com/AparGarg99/Tutorials/blob/master/TFOD/1_Image%20Collection.ipynb)<br>
Big thanks for *tzutalin* for his handy tool [labelImg](https://github.com/tzutalin/labelImg).<br>
8. Train model using [2_Training and Detection.ipynb](https://github.com/AparGarg99/Tutorials/blob/master/TFOD/2_Training%20and%20Detection.ipynb)

## Sample Project
[RPSGame](https://github.com/AparGarg99/RPSGame) (rock-paper-scissors game)

## References
* MODEL DEV: https://www.youtube.com/watch?v=yqkISICHH-U&list=PLgNJO2hghbmid6heTu2Ar68CzJ344nUHy&index=4
* APP DEV: https://www.youtube.com/watch?v=ZTSRZt04JkY
