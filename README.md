# Indian Startup Funding Analysis 🇮🇳

A complete exploratory data analysis of 3000+ Indian startup funding deals using Python, Pandas and NumPy. Built as a first data science project to uncover patterns in how Indian startups raise money, which sectors attract investors, and which cities dominate the startup ecosystem.

---

## Questions I Set Out to Answer
- Which sector received the most funding deals?
- Which sector received the most money?
- Which city dominates the Indian startup scene?
- What does a typical funding deal look like?
- Is the average deal size an accurate representation of reality?

---

## Key Findings
- **Consumer Internet** dominated with **589 deals** — the most active sector by number of investments
- **eCommerce** received the most money — **$7.89 Billion** in total funding
- **Bangalore** is India's undisputed startup capital with **582 deals**
- The **typical deal size is $1.70 Million** (median) — much lower than the average of $18.43 Million
- The **largest single deal was $3.90 Billion** — a massive outlier that skews the average significantly
- **Finance + FinTech combined** received **$3.20 Billion** — making it the 4th biggest sector

---

## Charts

### Top 10 Sectors by Number of Deals
![Top Sectors](top_sectors.png)

### Top 10 Cities by Number of Deals
![Top Cities](top_cities.png)

### Top 10 Sectors by Total Funding Amount
![Sector Funding](sector_funding_amount.png)
---

### Step 6 — Understanding average vs median
NumPy gave me an average deal size of $18.43 Million but a median of only $1.70 Million. That huge gap told me something important — a few massive deals like the $3.90 Billion outlier were pulling the average way up. The median of $1.70 Million is the true picture of what a typical Indian startup raises. This is why financial reports always use median salary instead of average salary.

**Lesson learned:** When data has outliers, median is more honest than average. Always calculate both and compare them.

---

## Tools Used
- **Python** — core programming language
- **Pandas** — data loading, cleaning, grouping and analysis
- **NumPy** — statistical calculations (mean, median, max, min)
- **Matplotlib** — data visualization and chart generation

---

## Dataset
- **Source:** Kaggle — Indian Startup Funding
- **Original size:** 3044 records
- **After cleaning:** 2065 records
- **Columns used:** Startup Name, Industry Vertical, City Location, Investors Name, Amount in USD
