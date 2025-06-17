import pandas as pd
import re

def weak_label(text):
    abnormalities = ['haemorrhage', 'haemorrhages', 'hematoma', 'traumatic', 'abnormal', 'stroke', 'contusion', 'fracture', 'mm']

    text = str(text).lower()
    return 1 if any(abnormal in text for abnormal in abnormalities) else 0

def extract_pathologies(text):
    abnormalities = ['haemorrhage','haemorrhages', 'hematoma', 'traumatic', 'fracture', 'stroke', 'contusion']

    text = str(text).lower()
    return [abnormal for abnormal in abnormalities if abnormal in text]

def extract_location(text):
    locations = ['frontal', 'temporal', 'parietal', 'occipital', 'cerebellum', 'basal ganglia']

    text = str(text).lower()
    return [loc for loc in locations if loc in text]

def extract_bleed_subcategory(text):
    subcategories = ['epidural', 'subdural', 'subarachnoid', 'intraventricular', 'contusion']

    text = str(text).lower()
    return [sub for sub in subcategories if sub in text]

def extract_measurement(text):
    text = str(text).lower()
    match = re.search(r'(\d+) ?mm', text)  # first match
    return match.group(0) if match else ''


def process_report(text):
    processed = {
        "Normal/Abnormal": weak_label(text),
        "Pathologies extracted- comma separated( Ex- sdh, haemorrhag, sah, Uncal Herniation)": ', '.join(extract_pathologies(text)),
        "Location & brain organ of Injury( Main brain body part/organ and location of abnormality)": ', '.join(extract_location(text)),
        "Bleed Subcateogy( If it contains bleed, which bleed subcategory- possible values ( epidural, subdural, subarchnoid, Contusion, Intraventricular, Hematoma) )": ', '.join(extract_bleed_subcategory(text)),
        "Measurement of the abnormality ( Volume in mm, length etc)": extract_measurement(text),
        "Midline shift - If yes, measurement of midline shift ( Ex- 3 mm)": extract_measurement(text),
    }
    return processed

def main():
    df = pd.read_csv('radiologists_report.csv')  # Change to your CSV file name
    
    for idx, row in df.iterrows():
        report = str(row['Radiologist Diagnosis'] or '')  # converts NaNs to ''
        processed = process_report(report)

        for key, value in processed.items():
            df.at[idx, key] = value

    df.to_csv('processed_report.csv', index=False)  # Saves processed CSV
    print("Processing complete! File saved as processed_report.csv")

if __name__ == "__main__":
    main()
