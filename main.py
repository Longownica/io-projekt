import fastbook
import PyQt5
import uploader as uploader
from fastbook import *
from fastai.vision.all import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton


def main():

    Form, Window = uic.loadUiType("C:/Users/monik/Desktop/io_impl/dialog.ui")
    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()

    fastbook.setup_book()
    torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    torch.cuda.empty_cache()
    torch.device("cpu")
    new_learn = load_learner("C:/Users/monik/wykrywacz.pkl")

    #
    uploader = widgets.FileUpload()
    img = PILImage.create(uploader.data[0])
    #

    # rozpoznajemy obrazek we wczytanym modelu
    is_cat, _, probs = new_learn.predict(img)

    print(f"Is this a cat?: {is_cat}.")
    print(f"Probability it's a cat: {probs[1].item():.6f}")

if __name__ == "__main__":
    main()

def clicked():
    print("clicked")