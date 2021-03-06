from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense


#this right here is the brains of the machine.
#Sets up the multiple layers and input and output
#Will need to come back and tweak for improving specific performance on Space Invaders.



class ConvolutionalNeuralNetwork:

    def __init__(self, input_shape, action_space):
        self.model = Sequential()
        self.model.add(Conv2D(32,
                              8,
                              strides=(4, 4),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape,
                              data_format="channels_first"))
        self.model.add(Conv2D(64,
                              4,
                              strides=(2, 2),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape,
                              data_format="channels_first"))
        self.model.add(Conv2D(64,
                              3,
                              strides=(1, 1),
                              padding="valid",
                              activation="relu",
                              input_shape=input_shape,
                              data_format="channels_first"))
        self.model.add(Flatten())
        self.model.add(Dense(512, activation="relu"))
        self.model.add(Dense(action_space))
        self.model.compile(loss="mean_squared_error",
                           optimizer=RMSprop(lr=0.00025,
                                             rho=0.95,
                                             epsilon=0.01),
#Changed metrics=["accuracy"] to metrics=["acc"] to match call in ddqn_game_model.py on line 145
                           metrics=["accuracy"])
        self.model.summary()
