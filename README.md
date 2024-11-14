# SAT Teacher Repository

This repository contains the code, datasets, and documentation for the **SAT Teacher** project, a chatbot-powered tool designed to help users understand and interact with Self-Attachment Theory (SAT). By integrating natural language processing (NLP) techniques and machine learning models, SAT Teacher enables users to ask questions about SAT and receive informative responses, even if they have no prior knowledge of the theory. 

## Project Overview

The **SAT Teacher** system is designed to provide answers to user queries about Self-Attachment Theory. This is achieved by embedding and indexing over 140 SAT-related question-answer pairs, each paired with semantically similar questions to improve the model’s coverage and accuracy. The system also incorporates Persian translations, allowing for localized use in Persian-speaking contexts.

Key features include:
1. **Question Answering**: Uses the Pars-BERT model to generate embeddings for SAT-related questions and retrieve relevant responses based on user queries.
2. **Spell Checking**: Detects and corrects spelling errors in user input.
3. **Data Augmentation**: Generates semantically similar questions to expand the dataset and enhance response accuracy.
4. **Translation**: Automatically translates text between Chinese and Persian for dataset preparation, ensuring diverse linguistic support.

## Directory Structure

- **Code**:
  - `QA_model.ipynb`: Implements the question-answering model using Pars-BERT embeddings and cosine similarity to find the best matching answers to user questions.
  - `SAT_embedding.py`: Contains functions for embedding generation using Pars-BERT, similarity calculation, and dataset preprocessing.
  - `Spell_checker.ipynb`: Implements a spell-checking feature in Persian, leveraging Hunspell to correct user input errors.

- **Dataset**:
  - `questions_dataset_final_persian.csv` and `questions_dataset_final.csv`: Datasets containing SAT-related questions, both in Persian and English.
  - `SATCorpus_persian_revised.csv`, `SATCorpus_persian.csv`, and `SATCorpus.csv`: Datasets containing SAT-related content, utilized for question-answering and embedding training.

- **Documentation**:
  - Contains various documentation files providing background on SAT and project structure. Notably, `SAT Teacher.docx` details the SAT Teacher integration and its purpose, methodology, and functionality.

- **Script**:
  - `Translation.py`: A script for translating CSV content from Chinese to Persian using Google Translate, with specific focus on SAT-related terminology.

## Model Architecture and Methods

### Embedding and Similarity Computation

The **SAT Teacher** model utilizes the Pars-BERT model to create embeddings for questions and answers in Persian. Cosine similarity is used to measure the alignment between user queries and the dataset questions, allowing the model to identify the most relevant response.

Given two vectors, \(\tau\) and \(\sigma\), cosine similarity is calculated as:

\[
\text{sim}(\tau, \sigma) = \frac{\tau \cdot \sigma}{\|\tau\| \|\sigma\|}
\]

This metric identifies the closest match in the dataset for the input query and returns the corresponding answer.

### Data Augmentation for Improved Coverage

To increase the system's ability to handle diverse user questions, additional similar questions are generated for each main query by:
- Adding common question starters and enders.
- Replacing key words with synonyms or contextually equivalent terms.

### Spell Checking

The spell-checking module uses Hunspell, adapted for Persian, to identify and suggest corrections for misspelled words in user queries, thus improving response relevance.

### Translation

For broader use, `Translation.py` provides translation capabilities between Chinese and Persian, with a focus on SAT terminology.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Essential packages: `transformers`, `torch`, `numpy`, `pandas`, `scikit-learn`, `hunspell`, `sentence_transformers`, `googletrans`

Install dependencies via:
```bash
pip install -r requirements.txt
```

### Running the Project

1. **QA Model**: Use `QA_model.ipynb` to run the main question-answering model, which processes user input, generates embeddings, and retrieves answers.
2. **Spell Checker**: Run `Spell_checker.ipynb` for spell-checking user input in Persian.
3. **Translation**: Execute `Translation.py` for translating datasets from Chinese to Persian.

### Example Usage

1. Load the question-answering notebook (`QA_model.ipynb`).
2. Run the spell-checking notebook to ensure input accuracy.
3. Input questions to retrieve relevant answers.

## Results and Evaluation

The model achieves an accuracy rate of over 80% on generated similar questions, demonstrating its effectiveness in retrieving relevant answers. Evaluation metrics, including cosine similarity, confirm the robustness of the SAT Teacher in handling varied user inputs.

## Future Enhancements

- Expanding the dataset with more question-answer pairs.
- Improving spell-checking accuracy for diverse user inputs.
- Adding more language support for SAT content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information. 

## Acknowledgments

This project leverages the Pars-BERT model by Hooshvare Lab and uses Google Translate for cross-linguistic support. Special thanks to the contributors of these technologies and datasets that support the SAT Teacher project.