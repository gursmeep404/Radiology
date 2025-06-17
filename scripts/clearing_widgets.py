import nbformat

with open('../open_source_models/distillGPT_flan-t5_bioGPT.ipynb', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

if 'widgets' in nb.metadata:
    nb.metadata['widgets'] = {} 

with open('../open_source_models/distillGPT_flan-t5_bioGPT.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
