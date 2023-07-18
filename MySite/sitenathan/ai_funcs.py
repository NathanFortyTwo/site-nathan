from tensorflow import errors
import numpy as np

from MySite.settings import model,vectorizer
def tweet_prediction(message):
    try:
        input_vect = vectorizer(message)
        res = model.predict(np.array([input_vect]))
    except : # if anything goes wrong, we return 0.5 and act like nothing happened lol
        res = np.array([[0.5]])
    return res
