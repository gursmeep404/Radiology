# Information Extraction From Radiologist's report 
 
The aim is to automate the extraction of key information from radiologists’ reports.
We start from an Excel file with bleed reports, where each row corresponds to a patient’s radiology report.
From these reports, we need to extract:

1. Normal/Abnormal
2. Pathologies extracted- comma separated( Ex- sdh, haemorrhag, sah, Uncal Herniation)
3. Location & brain organ of Injury( Main brain body part/organ and location of abnormality)
4. Measurement of the abnormality ( Volume in mm, length etc)
5. Midline shift - If yes, measurement of midline shift ( Ex- 3 mm)
6. Bleed Subcateogy( If it contains bleed, which bleed subcategory- possible values {epidural, subdural, subarchnoid, Contusion, Intraventricular, Hematoma})

