import pandas as pd

csv_file_path = '/Users/ainomis_dev/Desktop/ainomis/other/docs/url_classification_241015.csv'
df = pd.read_csv(csv_file_path)

# malicious 만 필터링

# malicious_urls = df[df['label'] == 'Malicious']

malicious_urls = df[
    (df['label'] == 'Malicious') &
    (~df['classification'].str.contains('Error-Request', na=False)) &
    (~df['classification'].str.contains('Error-Unexpected', na=False)) &
    (~df['report'].str.contains('Error-Unexpected', na=False))
    (~df['report'].str.contains('Error-Request', na=False))
    ]


# 필터링 결과 새로운 csv파일로 저장
malicious_file_path = 'docs/filtered_malicious_urls.csv'
malicious_urls.to_csv(malicious_file_path, index=False)

print(f"{malicious_file_path} 파일 저장 성공")