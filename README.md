# Radiology Diagnosis Structuring

## Project Overview

In modern medical imaging, **radiologist diagnoses are often written in free text**, making them difficult for machine learning models to interpret directly. This project tackles that challenge — by **automatically extracting five key fields** from raw radiologist diagnosis notes using NLP, with the long-term goal of enabling **MRI+Label supervised learning pipelines**.

This project began with a raw Excel file — containing diagnosis text for multiple patients — and evolved into a fully fine-tuned language model pipeline that structures this data with remarkable accuracy.

---

## Objective

To build a robust NLP pipeline that converts free-form radiologist diagnosis text into structured labels across five fields:

- **Abnormal/Normal**
- **Pathologies Extracted**
- **Midline Shift**
- **Location & Brain Organ**
- **Bleed Subcategory**

---

## Approaches Tried

### 1. **Hardcoded Keyword Matching**
Tried simple Python scripts using manually crafted keyword lists. Results were shallow and unreliable — medical text is too nuanced for static rules.

---

### 2. **Pre-trained Transformers on Colab**
Tried small models like `flan-t5`, `bioGPT`, `distilgpt` via Google Colab and also tried using large models with billions of parameters , but below are the issues I faced: 

- Inference was slow.
- Larger models failed due to limited memory.
- Smaller models performed poorly and so did large models which I managed to load in colab
- Results were inconsistent due to size and training mismatch.

---

### 3.  **ChatGPT-powered Label Extraction**
When nothing worked — I passed the raw diagnosis data to **ChatGPT**, which successfully extracted all 5 fields with high consistency. This generated my **labeled dataset**, which became the foundation of everything that followed.

---

### 4. **Fine-tuning T5-small with K-Fold Cross Validation**
Fine-tuned `t5-small` on the labeled dataset using **5-fold cross validation**, then trained on full data for final evaluation.

*This was the first successful, scalable solution with measurable performance.*

---

### 5. **Retrieval-Augmented Generation (RAG) with TF-IDF + FAISS**
Converted all rows of the labeled dataset into **retrievable documents**. Implemented RAG-style pipeline where the model retrieves similar diagnosis text based on TF-IDF similarity and generates labels from that.

This approach was limited — the retrieved text often **overrides the actual input**, reducing generalization on unseen reports.

---

### 6. **Fine-tuning with RAG Pipeline**
Combined both concepts: Used retrieved context during fine-tuning, so the model **learns to generalize** over both original input and similar examples.

Surprisingly, this approach yielded **very low test loss (~0.07)** and strong generalization — even on unseen data.

---