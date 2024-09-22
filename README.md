# 📚 Book Recommendation System

## 📖 Overview
Welcome to the Book Recommendation System! This project utilizes the Nearest Neighbors algorithm to cluster users based on their book ratings. The core idea is that if one person has rated a book and another person has also rated it, they are likely similar in their reading preferences. Thus, we recommend books to users based on the ratings of similar users.

## 🔍 How It Works
1. **User-Book Matrix:** We create a matrix where:
   - **Columns** represent users
   - **Indexes** represent books
   - **Values** are the ratings given by users to the books.

2. **Filtering Criteria:**
   - We apply constraints to ensure quality recommendations:
     - **Users:** Only include users who have rated at least **200 books**.
     - **Books:** Only include books that have a minimum rating of **50**.

3. **Recommendation Process:** 
   - When a user has read a book that another user has not, the system recommends that book to the latter based on the similarity of their ratings.

## 🚀 Features
- Efficient clustering of users using the Nearest Neighbors algorithm.
- Personalized book recommendations based on user similarity.
- Filtered recommendations to ensure relevance and quality.

## Dataset
- You can get the data set from this link : https://www.kaggle.com/code/ruchi798/book-crossing-starter-notebook-and-eda/input

  


