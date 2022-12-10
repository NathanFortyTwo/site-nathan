import pickle
from tensorflow import keras
import tensorflow as tf
from MySite.settings import BASE_DIR
import numpy as np

def get_vectorizer(path):
    from_disk = pickle.load(open(path, "rb"))
    new_v = keras.layers.TextVectorization.from_config(from_disk['config'])
    # You have to call `adapt` with some dummy data (BUG in Keras)
    new_v.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
    new_v.set_weights(from_disk['weights'])
    return new_v

def load_model(path):
    model = tf.keras.models.load_model(path)
    return model

def tweet_prediction(message):
    vectorizer = get_vectorizer(str(BASE_DIR)+"/sitenathan/IA/tweet_pred/tv_layer.pkl")
    input_vect = vectorizer(message)

    model = load_model(str(BASE_DIR)+"/sitenathan/IA/tweet_pred/Mymodel")
    res = model.predict(np.array([input_vect]))
    return res
