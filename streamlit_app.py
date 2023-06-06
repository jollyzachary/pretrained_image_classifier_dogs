import streamlit as st
from PIL import Image
from classifier import classifier

# Set the title of the app
st.title('Dog Breed Classifier')

# Add a select box for the model selection
model_name = st.selectbox('Choose a model:', ('resnet', 'alexnet', 'vgg'))

# Add an explanation of the chosen model
if model_name == 'resnet':
    st.write("ResNet is a convolutional neural network that is 50 layers deep. It's a highly accurate model, but it can be slower and require more computational resources than other models.")
elif model_name == 'alexnet':
    st.write("AlexNet is a convolutional neural network that is 8 layers deep. It's less accurate than some other models, but it's faster and requires less computational resources.")
else:  # vgg
    st.write("VGG is a convolutional neural network that is 16 or 19 layers deep. It's a highly accurate model, but it's slower and requires more computational resources than other models.")

# Allow the user to upload multiple image files
uploaded_files = []
for i in range(3):  # Allow up to 3 images
    uploaded_file = st.file_uploader(f"Choose image {i+1}...", type="jpg", key=i)
    if uploaded_file is not None:
        uploaded_files.append(uploaded_file)

# Process each uploaded image
for i, uploaded_file in enumerate(uploaded_files):
    # Open the image file
    img = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(img, caption=f'Uploaded Image {i+1}.', use_column_width=True)

    # Save the uploaded image to a temporary file and get the path of the file
    img_path = f'temp{i}.jpg'
    img.save(img_path)

    # Predict the breed of the dog in the image
    breed, confidence = classifier(img_path, model_name)

    # Display the predicted breed and the confidence score
    st.write(f"Predicted breed for image {i+1}: {breed} (Confidence: {confidence*100:.2f}%)")

