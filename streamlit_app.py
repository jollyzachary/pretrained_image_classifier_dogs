import streamlit as st
from PIL import Image
from classifier import classifier

# Set the title of the app
st.title('Dog Breed Classifier')

# Allow the user to upload an image file
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Open the image file
    img = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    # Save the uploaded image to a temporary file and get the path of the file
    img_path = 'temp.jpg'
    img.save(img_path)

    # Predict the breed of the dog in the image
    # You can choose the model you want to use here
    breed = classifier(img_path, 'resnet')

    # Display the predicted breed
    st.write("Predicted breed: ", breed)
