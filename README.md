# Information Extraction From Radiologist's report 
 
The aim is to automate the extraction of key information from radiologists’ reports.
We start from an Excel file with bleed reports, where each row corresponds to a patient’s radiology report.
From these reports, we need to extract:


- Normal/Abnormal
- Pathologies extracted- comma separated( Ex- sdh, haemorrhag, sah, Uncal Herniation)
- Location & brain organ of Injury( Main brain body part/organ and location of abnormality)
- Measurement of the abnormality ( Volume in mm, length etc)
- Midline shift - If yes, measurement of midline shift ( Ex- 3 mm)
- Bleed Subcateogy( If it contains bleed, which bleed subcategory- possible values {epidural, subdural, subarchnoid, Contusion, Intraventricular, Hematoma})


## Approach

**Word matching** :
- Started with simple keyword matching
- Looked for keywords in the radiologists’ reports to extract abnormalities

- `Issue`: It wasn't robust or accurate enough. It missed context and subtle abnormalities 

**DistilGPT-2, FLAN-T5, BioGPT** :
- Experimented with open-source large language models (100M parameters)

- `Issue`: These models were not proficient at understanding specialized radiology reports

**DeepSeek-R1 (1.3B parameters)**
- It performed considerably better at understanding context and retrieving information

- `Issue`: The main bottleneck was processing time, because we queried it row by row. The approach wasn't scalable for large datasets and resulted in slow processing speeds
