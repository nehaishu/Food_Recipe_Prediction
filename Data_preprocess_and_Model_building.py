#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Embedding, Dense
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences


# In[2]:


df = pd.read_excel('final_data.xlsx')


# In[3]:


df.head()


# In[4]:


df= df.applymap(lambda x: x.lower() if isinstance(x, str) else x)


# In[5]:


df = df.applymap(lambda x: x.replace(' ', '') if isinstance(x, str) else x)


# In[6]:


df.columns


# In[7]:


# Select the ingredient name columns
ingredient_names = list(df.columns)[:-1]  # Exclude the last column (output)

# Combine the ingredient names into a single text column
df['ingredients'] = df[ingredient_names].apply(lambda x: ' '.join(str(x)), axis=1)
y = df['output']


# In[8]:


df.head()


# In[9]:


df.ingredients


# # New Section

# In[10]:


# Perform label encoding on the labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y) # Label are mapped to unque numeic values


# In[11]:


y


# In[12]:


X_text = df['ingredients']


# In[13]:


# Split the dataset into training and testing sets
X_train_text, X_test_text, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=42)


# In[14]:


# Convert text to sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train_text) # Unique words are mapped to different unique numeric values  
X_train_sequences = tokenizer.texts_to_sequences(X_train_text) # Assign the values that are generated in above step for each word in each row for train data
X_test_sequences = tokenizer.texts_to_sequences(X_test_text)


# In[15]:


# Pad sequences to have the same length
max_sequence_length = max([len(seq) for seq in X_train_sequences])
X_train_padded = pad_sequences(X_train_sequences, maxlen=max_sequence_length) # maintains same len of sequence generated abve for all rows by adding a pad_value default is 0(i.e ready fr training)
X_test_padded = pad_sequences(X_test_sequences, maxlen=max_sequence_length)


# In[16]:


len(y)


# In[ ]:





# In[17]:


num_classes=len(np.unique(y)) # Total no of  unique labels


# In[18]:


# Create the ANN model with word embeddings
# ANN Model code
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
from keras.utils import to_categorical

# Convert the labels to categorical format
y_train_categorical = to_categorical(y_train, num_classes)

# Set the input and output dimensions
input_dim = len(tokenizer.word_index) + 1
output_dim = 100

# Create the model
model = Sequential()
model.add(Embedding(input_dim=input_dim, output_dim=output_dim, input_length=max_sequence_length))
model.add(Flatten())
model.add(Dense(20, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# In[19]:


model.summary()


# In[20]:


from keras.callbacks import ModelCheckpoint, EarlyStopping, CSVLogger

# Define the paths for saving checkpoints and the CSV log file
checkpoint_path = 'model_checkpoint.h5'
csv_log_file = 'training_log.csv'

# Define the callbacks
checkpoint_callback = ModelCheckpoint(checkpoint_path, monitor='val_loss', save_best_only=True)
#early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
#csv_logger_callback = CSVLogger(csv_log_file)


# In[21]:


y_test_categorical = to_categorical(y_test, num_classes)

# Fit the model with callbacks
model.fit(X_train_padded, y_train_categorical, epochs=20, batch_size=32, validation_data=(X_test_padded,y_test_categorical), callbacks=[checkpoint_callback])



# In[22]:


# Evaluate the model
y_test_categorical = to_categorical(y_test, num_classes)

loss, accuracy = model.evaluate(X_test_padded,y_test_categorical)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}") 


# In[23]:


y_test_categorical


# In[ ]:





# 

# In[24]:


X_test_padded.shape


# In[25]:


# Get predictions
predictions = model.predict(X_train_padded)

# Convert probabilities to class labels
predicted_labels = predictions.argmax(axis=1)

# Print predicted labels
print(predicted_labels)


# In[26]:


# Convert predicted labels to text
predicted_text_labels = label_encoder.inverse_transform(predicted_labels)

# Print predicted text labels
print(predicted_text_labels)


# In[ ]:





# In[49]:





# In[ ]:





# In[45]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:




