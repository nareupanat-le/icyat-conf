import pandas as pd
import json
import os

# 1. โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv('ICYAT_Database - AllData.csv')

# ลบแถวที่ไม่มีชื่อหรือปี (ป้องกันข้อมูลขยะ)
df = df.dropna(subset=['year', 'name'])

# สร้างโฟลเดอร์ data/ ถ้ายังไม่มี
if not os.path.exists('data'):
    os.makedirs('data')

# 2. สร้างไฟล์ JSON แบบรวมทุกปี (all_data.json)
all_data = df.to_dict(orient='records')
with open('data/all_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
print(f"สร้างไฟล์ all_data.json สำเร็จ! ({len(all_data)} รายการ)")

# 3. สร้างไฟล์ JSON แยกตามปี
unique_years = df['year'].unique()

for year in unique_years:
    # ดึงเฉพาะข้อมูลของปีนั้นๆ
    year_data = df[df['year'] == year].to_dict(orient='records')
    
    # ตั้งชื่อไฟล์ (เช่น "CYAT 2018" -> "2018.json")
    # ตัดเอาเฉพาะตัวเลขปีมาใช้ตั้งชื่อไฟล์ให้ดูสะอาดตา
    year_str = str(year).split()[-1]
    filename = f"data/{year_str}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(year_data, f, ensure_ascii=False, indent=2)
    print(f"สร้างไฟล์ {filename} สำเร็จ! ({len(year_data)} รายการ)")