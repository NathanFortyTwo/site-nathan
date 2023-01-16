
import numpy as np
#from MySite.settings import model,vectorizer



def tweet_prediction(message):
    input_vect = vectorizer(message)
    res = model.predict(np.array([input_vect]))
    return res
