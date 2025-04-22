# GenAI Intensive Course with Gemini SDK

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

# 📝 Course / Labs Name

> 5-Day Gen AI Intensive Course with Google & Kaggle

---

## 📊 Dataset

- Source: ![Kaggle](https://www.kaggle.com/learn-guide/5-day-genai)

---

## ⚙️ Techniques / Concepts Covered
- Day 1: Foundational Models & Prompt Engineering;
- Day 2: Embeddings and Vector Stores/Databases;
- Day 3: Generative AI Agents;
- Day 4: Domain-Specific LLMs;
- Day 5: MLOps for Generative AI;

---

## 💡 Lessons Learned

- Capstone Project:
"You must demonstrate what you've learned in this course by applying it to a use case of your choosing in a Kaggle Notebook. You must demonstrate in your code at least three (3) of the generative AI capabilities you learned in this course (see the Gen AI capabilities section)."
Gen Ai Capabilities Applied:
- `AI Agent:` Build an AI Agent using Gemini SDK
- `RAG:` Use RAG in AI Agents
- `Function Calling`: Function Calling in AI Agents


---

## 📁 Project Organization


```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

