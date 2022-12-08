import tensorflow as tf
import keras
from keras import layers
from tensorflow import keras
from tensorflow.keras.layers import *
from tensorflow.keras import *
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.optimizers.schedules import ExponentialDecay



def training(train_data,test_data):

    training=train_data
    input = keras.Input(shape=(training.shape[1],))


    batch_size = 46
    encoding_dim = 115
    encoding_dim_2 = 167
    learning_rate = 1e-7

    epochs = 500
    encoded = layers.Dense(encoding_dim, activation='relu',activity_regularizer=tf.keras.regularizers.l2(learning_rate))(input)
    decoded = layers.Dense(encoding_dim_2, activation='sigmoid')(encoded)
    decoded = layers.Dense(encoding_dim, activation='sigmoid')(decoded)
    decoded = layers.Dense(training.shape[1], activation='sigmoid')(decoded)
    metrics = ['mse']
    model = keras.Model(input, decoded) 
    model.compile(optimizer='adam', loss='mse', metrics=metrics)
    print('\n--> Starting training')
    model.fit(training, training, batch_size = batch_size, epochs = epochs,
              validation_data=(training,training),shuffle=False, verbose = 0)

    print('\n--> Ending training')
    test_x_predictions=model.predict(test_data)

    mse_dense = tf.math.reduce_mean(tf.math.pow(test_data[:,:] - test_x_predictions[:,:], 2), axis = 1)
    
    return mse_dense