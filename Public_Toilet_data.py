import pandas as pd

file = r"C:\Users\atg06\.vscode\hackerton\12_04_01_E_공중화장실정보_2.csv"

df= pd.read_csv(file, encoding='cp949', usecols = ["소재지도로명주소","WGS84위도", "WGS84경도"]) #소재지도로명주소, 위도, 경도 데이터 추출
#소재지도로명 주소를 추출하는 이유는 남구데이터를 뽑기위하여

df = df.dropna(axis=0) # 경도, 위도 값 없는 항목 제거
is_namgu = df["소재지도로명주소"].str.contains("남구") #소재지도로명 주소에 남구가 포함된 데이터들을 추출

df = df[is_namgu] #is_namgu 조건식에 맞는 데이터들 추출