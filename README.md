# YummyClassifier
Classifies an image of food as yummy / not yummy,
along with the probability of yumminess.

Trained on r/foodporn and r/shittyfoodporn subreddits.

## Setup
```buildoutcfg
pip install fastbook
pip install torch
pip install graphviz
```

## Usage
```
python main.py path-to-image.jpg
```
Other image formats are supported.

## Testing
Unit tests are in `classifierTest.py`.