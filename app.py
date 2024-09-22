import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the pre-trained models and data
with open('book_pivot.pkl', 'rb') as f:
    book_pivot = pickle.load(f)

with open('model.pkl', 'rb') as f:
    neighbor = pickle.load(f)

with open('book_data.pkl', 'rb') as f:
    book_data = pickle.load(f)

# Function to recommend books
def recommend_books(name):
    books = []
    try:
        name_index = np.where(book_pivot.index == name)[0][0]
        distances, suggestions = neighbor.kneighbors(book_pivot.iloc[name_index, :].values.reshape(1, -1), n_neighbors=6)
        for i in range(len(suggestions)):
            books.append(book_pivot.index[suggestions[i]])
        return list(books[0][1:])  # Exclude the input book itself
    except IndexError:
        return []

# Function to get image URLs of recommended books
def get_images(books_name):
    images_link = []
    for book in books_name:
        try:
            image_url = book_data[book_data['Book-Title'] == book]['Image-URL-L'].iloc[0]
            images_link.append((book, image_url))
        except IndexError:
            images_link.append((book, ''))  # Handle missing image URLs
    return images_link

# Streamlit app
st.title("Book Recommendation System")

# User input for book title
book_name = st.text_input("Enter a book name:")

if book_name:
    # Get recommended books
    recommended_books = recommend_books(book_name)

    # Check if we have recommended books
    if recommended_books:
        st.subheader("Recommended Books:")
        book_images = get_images(recommended_books)

        # Create a list of columns for the books and spaces
        columns = st.columns(len(book_images) * 2 - 1) # 0.2 is the spacer column, 1 is the book column

        # Display recommended books with images in a single line with spacing
        for idx, (title, image_url) in enumerate(book_images):
            col_idx = idx * 2  # Use every second column for books, others for spacing
            with columns[col_idx]:
                if image_url:
                    st.image(image_url, width=150, caption=title)
                else:
                    st.write(f"{title} (Image not available)")
    else:
        st.write("No recommendations found. Please check the book name.")
