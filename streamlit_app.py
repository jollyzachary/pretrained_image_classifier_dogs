import streamlit as st
from PIL import Image
from classify import predict_breed

# Set the title of the app
st.title('Dog Breed Classifier')

# Allow the user to upload an image file
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Open the image file
    img = Image.open(uploaded_file)
    # Display the uploaded image
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    # Predict the breed of the dog in the image
    breed = predict_breed(img)

    # Display the predicted breed
    st.write("Predicted breed: ", breed)

