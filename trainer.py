# Import required libraries
import tensorflow as tf
import scipy
from tensorflow import keras

# Define the hyperparameters
batch_size = 2
num_epochs = 1000
learning_rate = 0.001

# Load the data using the ImageDataGenerator class
train_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    'archive',
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['daisy', 'rose', 'sunflower', 'tulip'])

test_data = test_datagen.flow_from_directory(
    'archive',
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['daisy', 'rose', 'sunflower', 'tulip'])

# Define the model architecture
model = keras.applications.resnet50.ResNet50(
    include_top=True,
    weights=None,
    input_shape=(224, 224, 3),
    classes=4)

# Compile the model
optimizer = keras.optimizers.Adam(lr=learning_rate)
model.compile(optimizer=optimizer,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_data, epochs=num_epochs)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_data)
print(f"Test accuracy: {test_acc}")

# Save the model
model.save('plant_id_model_2.h5')