import requests, re, os
from bs4 import BeautifulSoup 
import pandas as pd


# @st.cache_resource 
def fetch_html_and_js(url): 
	try: 
		# URL에서 콘텐츠 가져오기 
		response = requests.get(url) 
		response.raise_for_status() # HTTP 오류 발생 시 예외 발생 
		
		# BeautifulSoup을 사용하여 HTML 파싱 
		soup = BeautifulSoup(response.text, 'html.parser') 
		all_content = soup.prettify() 
		return all_content 
		
	except requests.RequestException as e: 
		return f"오류 발생: {str(e)}"



# @st.cache_resource 
def remove_all_comments(code): 
	"""자바스크립트 및 HTML 코드에서 모든 주석을 제거합니다.""" 
	if not isinstance(code, str):
		return code  # code가 문자열이 아니면 그대로 반환
    
	# 주석 패턴 정의 
	comment_pattern = re.compile( 
		r''' 
		(<!--[\s\S]*?-->) # HTML 주석 
		|(/\*[\s\S]*?\*/) # 다중 행 자바스크립트 주석 ˜
		|(//.*?$) # 한 줄 자바스크립트 주석 
		''', 
		re.MULTILINE | re.VERBOSE 
	) 
	return re.sub(comment_pattern, '', code) 
	

# CSV 파일 로드
csv_file_path = '/Users/ainomis_dev/Desktop/ainomis/other/docs/filtered_malicious_urls.csv'  # 여기에 실제 파일 경로를 넣어주세요.
df = pd.read_csv(csv_file_path)


# 각 URL에 대해 데이터를 가져와 새로운 열로 추가
df['response_data'] = df['url'].apply(lambda url: remove_all_comments(fetch_html_and_js(url)))

# 결과 CSV 파일로 저장
output_file_path = 'docs/˜filtered_malicious_urls_with_responses.csv'
df.to_csv(output_file_path, index=False)

print(f"결과가 {output_file_path}에 저장되었습니다.")