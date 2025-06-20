import nbformat

with open('../RAG_T5/RAG_without_fine_tuning.ipynb', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

if 'widgets' in nb.metadata:
    nb.metadata['widgets'] = {} 

with open('../RAG_T5/RAG_without_fine_tuning.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
