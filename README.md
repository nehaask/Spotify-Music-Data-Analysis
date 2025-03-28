# 🎧 Spotify Music Data Analysis

An end-to-end data analysis project on Spotify's massive dataset of 12 million songs using both Relational and Non-Relational Database Models. This project explores data modeling, normalization, preprocessing, and mining of association rules through frequent itemsets.

---

## 📌 About the Project

This project aims to analyze the Spotify dataset by exploring different data modeling strategies, normal forms, indexing, and pattern mining algorithms. It is divided into three key phases:

- **Phase 1:** Design and implementation of a Relational Model using PostgreSQL.
- **Phase 2:** Development of a Non-Relational counterpart using MongoDB, followed by a comparative study.
- **Phase 3:** Preprocessing, cleaning, and mining of the dataset using the Apriori Algorithm to discover patterns in the music data.

The dataset used contains metadata and features for over 12 million Spotify tracks, providing a large and rich base for analytical exploration.

---

## 🗂️ Dataset

- Source: [Spotify 12M Songs Dataset – Kaggle](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs)

---

## 🚀 Project Phases

### ✅ Phase 1 – Relational Modeling

- Designed an **Entity-Relationship Diagram (ERD)** based on the Spotify dataset.
- Created and populated tables in **PostgreSQL** using **DataGrip**.
- Mapped functional dependencies and identified opportunities for optimization via normalization.

### ✅ Phase 2 – NoSQL and Query Optimization

- Modeled the same dataset using **MongoDB** collections.
- Compared relational vs. non-relational data modeling approaches.
- Wrote complex SQL queries to derive insights from PostgreSQL.
- **Indexed** key columns to improve query retrieval times.
- Performed normalization:
  - **1NF (First Normal Form)**
  - **2NF (Second Normal Form)**
  - **3NF (Third Normal Form)**
  - **BCNF (Boyce-Codd Normal Form)**

### ✅ Phase 3 – Data Mining with Apriori

- Cleaned and preprocessed data using **PySpark** and **Python**.
- Applied the **Apriori Algorithm** to identify frequent itemsets.
- Created **Lattice Models** based on the mined association rules.
- Generated insights on track combinations, genre pairings, and more.

---

## 💻 Tech Stack & Tools

| Tool/Technology | Purpose |
|------------------|---------|
| **PostgreSQL**   | Relational database modeling and querying |
| **MongoDB**      | Non-relational document-based data modeling |
| **PySpark**      | Data preprocessing and scalable mining |
| **DataGrip**     | Database design and visualization |
| **Python**       | Data cleaning, scripting, and algorithm implementation |

---

## 📚 Key Concepts Explored

- Relational vs Non-Relational Database Design
- Functional Dependencies & Normalization (1NF → BCNF)
- Indexing for Query Optimization
- Association Rule Mining with Apriori
- Frequent Itemsets and Lattice Model Generation

---

## 🧠 Future Work

- Implement visual dashboards for music insights using Streamlit or PowerBI
- Explore clustering or recommendation algorithms using audio features
- Extend project to include time-series trends in song popularity

---

## 🤝 Contributions

Open to pull requests, suggestions, or collaboration ideas! Feel free to fork and build upon this project.

---

## 📫 Contact

If you have any questions or feedback, feel free to reach out via GitHub Issues

