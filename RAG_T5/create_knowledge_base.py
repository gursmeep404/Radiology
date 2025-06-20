import pandas as pd

# Load the dataset
df = pd.read_excel("dataset.xlsx")

# Replace NaN with placeholder text
df = df.fillna("Unknown")

# Function to convert a row into a document for RAG
def row_to_document(row):
    return f"""Diagnosis: {row['Radiologist Diagnosis'].strip()}
Abnormal/Normal: {row['Abnormal/Normal'].strip()}
Pathologies Extracted: {row['Pathologies Extracted'].strip()}
Midline Shift: {row['Midline Shift'].strip()}
Location & Brain Organ: {row['Location & Brain Organ'].strip()}
Bleed Subcategory: {row['Bleed Subcategory'].strip()}"""

# Apply to each row and convert to a list
corpus = df.apply(row_to_document, axis=1).tolist()

# Write the corpus to a UTF-8 encoded text file
with open("rag_corpus.txt", "w", encoding="utf-8") as f:
    for line in corpus:
        f.write(line + "\n\n")


