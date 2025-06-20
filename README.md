![Start gif](./images/start.gif "brain_scan")

# Automated Extraction of Structured Labels from Radiologist Diagnoses

## Project Overview

In modern medical imaging, **radiologist diagnoses are often written in free text**, making them difficult for machine learning models to interpret directly. This project tackles that challenge — by **automatically extracting five key fields** from raw radiologist diagnosis notes using NLP, with the long-term goal of enabling **MRI+Label supervised learning pipelines**.

This project began with a raw Excel file — containing diagnosis text for multiple patients — and evolved into a fully fine-tuned language model pipeline that structures this data with remarkable accuracy.

# Dataset 

AIIMS dataset of diagnosis reports of brain MRI scans


## Objective

To build a robust NLP pipeline that converts free-form radiologist diagnosis text into structured labels across five fields:

- **Abnormal/Normal**
- **Pathologies Extracted**
- **Midline Shift**
- **Location & Brain Organ**
- **Bleed Subcategory**


## Approaches Tried

### 1. **Hardcoded Keyword Matching**
Tried simple Python scripts using manually crafted keyword lists. Results were shallow and unreliable — medical text is too nuanced for static rules.


### 2. **Pre-trained Transformers on Colab**
Tried small models like `flan-t5`, `bioGPT`, `distilgpt` via Google Colab and also tried using large models with billions of parameters , but below are the issues I faced: 

- Inference was slow.
- Larger models failed due to limited memory.
- Smaller models performed poorly and so did large models which I managed to load in colab
- Results were inconsistent due to size and training mismatch.


### 3.  **ChatGPT-powered Label Extraction**
When nothing worked — I passed the raw diagnosis data to **ChatGPT**, which successfully extracted all 5 fields with high consistency. This generated my **labeled dataset**, which became the foundation of everything that followed.


### 4. **Fine-tuning T5-small with K-Fold Cross Validation**
Fine-tuned `t5-small` on the labeled dataset using **5-fold cross validation**, then trained on full data for final evaluation.

*This was the first successful, scalable solution with measurable performance.*


#### 5-Fold Cross Validation (T5 Fine-tuning)

| Fold | Eval Loss |
|------|-----------|
| 1    |0.031592|
| 2    |0.032712|
| 3    |0.033307|
| 4    |0.025809|
| 5    |0.026952|

**Average Loss**: `0.0300744`

**Inference**:
The validation loss across all 5 folds is consistently low, with a slight variation between folds. This suggests that the model is:

- Stable across different data splits

- Not overfitting to a specific subset

- Learning meaningful patterns from the radiology diagnoses

These results gave confidence to proceed with full-dataset fine-tuning and RAG-style experimentation.


#### Fine-tuning on Full Data 

- **Final Test Loss**: `0.173415`

**Inference**:
- The jump from the low K-Fold losses (~0.03) to a slightly higher final test loss (~0.17) is expected since:

- The model is now exposed to completely unseen diagnosis styles.

- Real-world generalization is tougher without exact matches in training.

Still, the loss remains quite reasonable showing that the model has generalized decently to new radiologist reports after full training.

### 5. **Retrieval-Augmented Generation (RAG) with TF-IDF + FAISS**
Implemented a Retrieval-Augmented Generation setup using TF-IDF + FAISS, where each diagnosis text in the labeled dataset was treated as a retrievable document. At inference time, the system retrieved the most similar document for a given input and attempted to generate labels from that context.

Test Loss: `11.75273`

Inference:
This approach performed poorly — the extremely high loss reveals a critical flaw: the model relied entirely on the retrieved context without truly understanding or adapting to the current input. Since FAISS retrieves text based solely on vector similarity, the returned context was often not relevant enough for accurate prediction, especially for unseen or nuanced inputs.


### 6. **Fine-tuning with RAG Pipeline**
Here, the model was fine-tuned using retrieved documents as context. This way, the model learned during training how to interpret similar prior cases while grounding its predictions in the specific input at hand.

Test Loss: `0.1902`

Inference:
A significant improvement — nearly two orders of magnitude lower loss than the non-fine-tuned version. This shows that when retrieval is paired with supervised fine-tuning, the model learns to use similar examples as helpful context rather than as direct replacements.
This hybrid setup blends the generalization power of fine-tuning with the contextual awareness of RAG, resulting in more accurate, robust outputs even on unseen diagnoses.

