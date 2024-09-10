
# Analysis of Mental Health and Addiction in Online Support Groups

## Overview

This project explores, understands, and predicts mental health and addiction outcomes by analyzing textual discussions from various support groups on Reddit. These discussions provide a rich dataset for uncovering patterns related to mental health issues and treatment efficacy, specifically during the challenging times of the COVID-19 pandemic.

## Installation and Setup

### Prerequisites

Ensure you have Python installed on your system. This project requires the following Python libraries: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `nltk`, and `wordcloud`. You can install these with the following command:

```bash
pip install pandas scikit-learn matplotlib seaborn nltk wordcloud
```

### Data

This analysis uses the Reddit Mental Health Dataset, which contains posts from 28 subreddits, focusing on 15 mental health support groups from 2018-2020. This dataset was selected to understand the impact of COVID-19 on mental health discussions online.

### Running the Project

The project is contained in a Jupyter notebook, which allows for interactive data analysis and visualization. To run the notebook:

1. Clone the repository or download the Jupyter notebook.
2. Navigate to the project directory.
3. Launch Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

4. Open the project notebook (`Analysis_of_Mental_Health_and_Addiction.ipynb`) in the Jupyter interface.

## Key Features and Components

- **Data Preparation and Cleaning**: Scripts for filtering irrelevant topics and ensuring high-quality inputs for models.
- **Feature Engineering**: Techniques to extract meaningful features from textual data, leveraging NLP methods like TF-IDF vectorization.
- **Machine Learning Modeling**: Clustering and classification models to predict outcomes based on the discussions, with a focus on advanced clustering strategies and nuanced text analysis.
- **Evaluation and Analysis**: Detailed evaluation of models to ensure effectiveness, using insights to propose recommendations for mental health support mechanisms.

## Key Findings and Insights

The project uncovers nuanced patterns within mental health discussions, emphasizing the complex nature of these conversations across various conditions. Key findings include the significant role of community support in mental health and addiction recovery, highlighted through advanced clustering and classification techniques.

## Challenges and Solutions

- **Variety and Complexity of Discussions**: Addressed through sophisticated NLP techniques and customized text feature engineering.
- **High-Dimensionality of Textual Data**: Managed by employing dimensionality reduction techniques and selective feature engineering.
- **Subjectivity and Ambiguity**: Tackled using sentiment analysis, clustering techniques, and context-aware NLP models.

## Advanced Data Preparation and Analysis Techniques

The project sets a benchmark in handling and analyzing complex datasets, particularly with a rich textual component. Innovations include unified dataset consolidation, advanced cleaning and preprocessing, feature engineering using NLP techniques, and the utilization of advanced clustering and classification methods.

## Future Directions

Future enhancements may focus on deeper integration of context-aware NLP models, exploring additional machine learning algorithms for improved predictive accuracy, and expanding the dataset to include more varied sources of mental health discussions.

## License

This dataset is made available under the Public Domain Dedication and License v1.0, subject to Reddit API terms.



Last updated on: 2024-04-02