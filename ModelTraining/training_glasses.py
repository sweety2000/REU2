import pickle
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

#load in features and labels
X=pickle.load(open('X.pkl', 'rb'))
y=pickle.load(open('y.pkl', 'rb'))

X = X/255 #work with smaller numbers

#look at X.shape so that we can see image size and dimensions

#intiate model
model = Sequential()

#for example, 64 feature maps and 3 dimensional
#relu activation
f_map = #amount of feature maps
dims = #3 for rgb or 1 for non-rgb

#create feature maps, then we pool
model.add(Conv2D(f_map, (dims, dims), activate = 'relu'))
model.add(MaxPooling2D((2,2)))

#second set of convolution
model.add(Conv2D(f_map, (dims, dims), activate = 'relu'))
model.add(MaxPooling2D((2,2)))

#flatten to 1D
model.add(Flatten())

#Dense layer
model.add(Dense(128, input_shape = X.shape[1:], activation = 'relu'))

#soft max for predictions
model.add(Dense(2, activation='softmax'))

#compile
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(X, y, epochs=5, validation_split=0.1)

newmodel = 'training_glasses.h5'
model.save(newmodel)
