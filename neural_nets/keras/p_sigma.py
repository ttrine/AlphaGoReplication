from keras.models import Sequential
from keras.layers import convolutional

k = 152 # depth of convolutional layers

model = Sequential()
model.add(convolutional.Convolution2D(input_shape=(48, 19, 19), nb_filter=k, nb_row=5, nb_col=5,
                                      init='uniform', activation='relu', border_mode='same'))
for i in range(2,13):
    model.add(convolutional.Convolution2D(nb_filter=k, nb_row=3, nb_col=3,
                                          init='uniform', activation='relu', border_mode='same'))

model.add(convolutional.Convolution2D(nb_filter=1, nb_row=1, nb_col=1,
                                      init='uniform', activation='softmax', border_mode='same'))
