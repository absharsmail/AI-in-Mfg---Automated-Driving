import numpy as np
WIDTH = 395
HEIGHT = 860

import tensorflow as tf
config = tf.compat.v1.ConfigProto(gpu_options = 
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
# device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
import numpy as np

from keras.models import Sequential
from keras.models import Model
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, EarlyStopping, ReduceLROnPlateau, TensorBoard
from keras import optimizers, losses, activations, models
from keras.layers import Convolution2D, Dense, Input, Flatten, Dropout, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D, Concatenate
from keras import applications
input_shape = (150, 300,3)
nclass = 9

base_model = applications.InceptionV3(weights='imagenet', 
                                include_top=False, 
                                input_shape=(150, 300,3))
base_model.trainable = True

add_model = Sequential()
add_model.add(base_model)
add_model.add(GlobalAveragePooling2D())
add_model.add(Dropout(0.5))

add_model.add(Dense(4096*2, 
                    activation='relu'))

add_model.add(Dense(4096*2, 
                    activation='relu'))

add_model.add(Dense(4096*2, 
                    activation='relu'))

add_model.add(Dense(4096, 
                    activation='relu'))
add_model.add(Dense(nclass, 
                    activation='softmax'))

model = add_model

model.compile(loss='categorical_crossentropy', 
              optimizer=optimizers.Adam(lr=1e-3, 
                                       ),
              metrics=['accuracy'])
model.summary()

cw={0: 0.49843931297086175, 1: 1.3119972469565966, 2: 1.5762273901808785, 3: 1.6694033935413246, 4: 1.9178771301012387, 5: 3.4231200897867566, 6: 9.15915915915916, 7: 135.55555555555554, 8: 0.24582104228121926}

import wandb
from wandb.keras import WandbCallback
wandb.init(project="introduction_wandb")

EPOCHS=100
import pandas as pd
import numpy as np
from random import shuffle
from keras.preprocessing.image import ImageDataGenerator


from sklearn.preprocessing import LabelEncoder

for d in range(EPOCHS):
    data_order = [i for i in range(1,62+1)]
    shuffle(data_order)
    print(d)
    for count,i in enumerate(data_order):
        
        try:
            file_name = 'E:/New folder/Data/niranjan/training_data-{}.npy'.format(i)
            # full file info
            train_data = np.load(file_name,allow_pickle=True)
            print('training_data-{}.npy'.format(i),len(train_data))
            
            import cv2
            X=np.zeros([450,150,300,3])
            test_x=np.zeros([50,150,300,3])
            
            Y=np.zeros([450,9])
            test_y=np.zeros([50,9])
            for i in range(len(train_data)):
                if i < 450:
                    a=train_data[i,0]
                    a=cv2.resize(a,(300,150))
                    X[i]=a
                    Y[i]=train_data[i,1]
                else:
                    a=train_data[i,0]
                    a=cv2.resize(a,(300,150))
                    test_x[i-450]=a
                    test_y[i-450]=train_data[i,1]

            X=np.asarray(X).astype(np.float32)
            Y=np.asarray(Y).astype(np.float32)
            
            test_x=np.asarray(test_x).astype(np.float32)
            test_y=np.asarray(test_y).astype(np.float32)
            if d%5==0:
                v=1
            else:v=0
            
            h=model.fit(X,Y, batch_size=2, epochs = 1, validation_data = (test_x, test_y),class_weight=cw,verbose=0,callbacks=[WandbCallback()])

            
            if count%10 == 0:
                print('SAVING MODEL!')
                model.save('ninna.h5')
                    
        except Exception as e:
            print(str(e))

