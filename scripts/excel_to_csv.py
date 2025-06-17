import pandas as pd

excel_file = 'Bleed_records_NLP.xlsx'

sheet_name = 0 

df = pd.read_excel(excel_file, sheet_name=sheet_name)

csv_file = 'radiologists_report.csv'
df.to_csv(csv_file, index=False)

print("Converted successfully.")
