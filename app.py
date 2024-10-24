import requests, re
from bs4 import BeautifulSoup 


@st.cache_resource 
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
		return f"오류 발생: {str(e)}", "", "" 



@st.cache_resource 
def remove_all_comments(code): 

	"""자바스크립트 및 HTML 코드에서 모든 주석을 제거합니다.""" 
	# 주석 패턴 정의 
	comment_pattern = re.compile( 
		r''' 
		(<!--[\s\S]*?-->) # HTML 주석 
		|(/\*[\s\S]*?\*/) # 다중 행 자바스크립트 주석 
		|(//.*?$) # 한 줄 자바스크립트 주석 
		''', 
		re.MULTILINE | re.VERBOSE 
	) 
	return re.sub(comment_pattern, '', code) 
	
#all_content만 넣으면 됨 
url='https://example.com/' 
all_content = fetch_html_and_js(url)