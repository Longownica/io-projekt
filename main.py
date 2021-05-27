from classifier import Classifier
import sys
import os

if len(sys.argv) != 2:
    print("One and only one argument is needed - path to image. Exiting...")
    exit()

imagePath = sys.argv[1]
if not os.path.isfile(imagePath):
    print("You dummy! The file does not exist. You had one job...")
    exit()

classifier = Classifier()
yummy, probability = classifier.isYummyFromPath(imagePath)

if yummy:
    print("MMM! What a delicious meal! Probability it's yummy: %.5f" % probability)
    print("It would fit right in https://reddit.com/r/foodporn")
else:
    print("EWWW, disgusting!!!! Probability it's yummy: %.5f" % probability)
    print("Take that away to https://reddit.com/r/shittyfoodporn")