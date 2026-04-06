# Indian Startup Funding Analysis

A complete exploratory data analysis of 3000+ Indian startup funding deals using **Python, Pandas, and NumPy**.
This project uncovers patterns in how Indian startups raise money, which sectors attract investors, and which cities dominate the ecosystem.

---

##  Objectives

* Identify the most active funding sectors
* Find which sectors receive the highest investment
* Analyze city-wise startup dominance
* Understand typical deal sizes
* Compare average vs median to detect skewness

---

##  Key Insights

* **Consumer Internet** → **589 deals** (most active sector)
* **eCommerce** → **$7.89B** (highest total funding)
* **Bangalore** → **582 deals** (startup capital of India)
* **Median deal size** → **$1.70M**
* **Average deal size** → **$18.43M** (skewed by outliers)
* **Largest deal** → **$3.90B** (major outlier)
* **Finance + FinTech** → **$3.20B** total funding

---

##  Visualizations

### Top 10 Sectors by Number of Deals

![Top Sectors](top_sectors.png)

### Top 10 Cities by Number of Deals

![Top Cities](top_cities.png)

### Top 10 Sectors by Total Funding

![Sector Funding](sector_funding_amount.png)

---

##  Tech Stack

* **Python** — Core programming
* **Pandas** — Data cleaning & analysis
* **NumPy** — Statistical computations
* **Matplotlib** — Data visualization

---

##  Approach

* Explored dataset structure (shape, columns, data types, null values)
* Removed irrelevant columns and focused on key features
* Cleaned funding amounts (removed commas, converted to numeric)
* Standardized inconsistent labels (e.g., *eCommerce variations*, *Bangalore/Bengaluru*)
* Compared **deal count vs total funding** for deeper insights
* Used **median vs mean** to detect skew caused by large outliers

---

##  Data Challenges

* Funding amounts stored as text (e.g., `"20,00,00,000"`)
* Lost **979 rows** due to invalid/missing values
* Inconsistent naming across sectors and cities
* Presence of extreme outliers affecting averages

---

##  Dataset

* **Source:** Kaggle — Indian Startup Funding
* **Columns Used:**

  * Startup Name
  * Industry Vertical
  * City Location
  * Investors Name
  * Amount in USD

---

##  Learnings

* Data cleaning has a massive impact on results
* Same dataset can tell different stories depending on analysis
* Median is often more reliable than mean in skewed data
* Small preprocessing decisions can significantly change insights

---
---

