# 📊 Predictive Modeling of Social Media Virality Using Stochastic Processes

This repository supports a research project that explores how **stochastic processes** (e.g., Hawkes processes, Markov chains, Poisson models) can be applied to **predict tweet virality**, integrating temporal engagement dynamics with machine learning techniques.

> 🧠 Authored by **Rajan Shukla** | Missouri State University  

---

## 🎯 Research Summary

This study investigates how the virality of tweets can be predicted using a combination of stochastic modeling and machine learning.  
Key models used:
- **Hawkes Process** for bursty engagement patterns
- **Markov Chains** for engagement state transitions
- **Poisson Process** for modeling interaction rates
- **Random Forest Classifier** for virality prediction

The work relies on a **simulated dataset** designed to mimic real Twitter dynamics due to limitations on API access.

---

## 📂 Repository Contents

| File/Notebook                         | Description |
|--------------------------------------|-------------|
| `Stochastic_Modeling_Research.pdf`   | Final research paper |
| `research.ipynb`                     | Jupyter notebook with full modeling pipeline, plots, and analysis |
| `stochastic.py`                      | Script for loading and exploring the simulated dataset |
| `Simulated Dataset.csv` *(optional)* | Synthetic Twitter dataset |
| `*.png` (heatmaps, plots, etc.)      | Visual assets used in the paper and notebook |

---

## 📌 Key Findings

- 📈 **Random Forest classifier** achieved **68.2% accuracy** in predicting virality
- 🔁 **Hawkes parameters** revealed strong temporal clustering (µ = 1.13, α = 0.14, β = 0.33)
- 💬 **Sentiment** had a moderate positive correlation with virality
- 🔀 **Markov Chains** showed limited transitions into high-virality states
- 📊 **Likes**, **retweets**, and **Hawkes intensity** were top predictors of virality

---

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/stochastic-virality-model.git
cd stochastic-virality-model

# Launch Jupyter Notebook
jupyter notebook research.ipynb

# Run the dataset script
python stochastic.py
