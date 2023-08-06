# FILE STRUCTURE
 ┣ 📂algorithm <br>
 ┃ ┗ 📜detectFacialFeatures.py <br>
 ┣ 📂utils<br>
 ┃ ┣ 📜algorithm_utils.py<br>
 ┃ ┣ 📜drawAndCalculate.py<br>
 ┃ ┣ 📜preprocess.py<br>
 ┃ ┣ 📜print_utils.py<br>
 ┃ ┣ 📜shape_predictor_68_face_landmarks.dat<br> 
 ┃ ┗ 📜shape_predictor_81_face_landmarks.dat<br>
 ┣ 📜.gitignore<br>
 ┣ 📜main.py<br>
 ┗ 📜README.md<br>

# M-SHAPE PROJECT 
### Objectives 
Detect Forehead baldness by calculating the ratio between vertical lines length on 
- central forehead  
- left forehead  
- right forehead  

### Hypothesis
If the ratio between central & left & right is imbalanced (and passed our defined threshold), we could classify that the user has forehead baldness

### Challenges
- Picture orientation (object is skewed to an axis,  not centered)<br>
<img src="6.jpg" alt="81 points ref" width="600" height="700"/>


- Bad Contrast (can be overcomed by performing gamma correction)<br>

- Too Close<br>
<img src="1.jpg" alt="81 points ref" width="600" height="700"/>
- Over Exposed (on bangs)<br>
<img src="8.jpg" alt="81 points ref" width="500" height="700"/>


### Procedure

<!-- ![reference](){width: 200px; height: 200px;} -->
<img src="81_points_reference.jpg" alt="81 points ref" width="500" height="700"/>


Dlib is a deep learning library that has been compiled in C++. For model specification, dataset that has been trained on, see: http://dlib.net/

It reads a .dat file which is a model config that can detect facial landmarks on human face.
There are several computation that we are interested in: 

```python
distance = {
      "forehead_central_distance":0,
      "forehead_left_distance":0,
      "forehead_right_distance":0,
      "left_brow":0,
      "right_brow":0,
      "forehead2nose": 0, 
      "nose2chin": 0
    }
```

### Commands
for a list of images <br>
```python 
python main.py
```
for single images
```python 
python main.py --single=path_to_your_image
```

# FNC (Receding Hairline) PROJECT

### Commands
```python
python main.py --m_shape=False
```

### Results

Ratio will be printed in the results folder as.txt file

<img src="4.jpg" alt="81 points ref" width="600" height="700"/>
