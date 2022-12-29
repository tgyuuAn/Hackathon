import pandas as pd

file = r"12_04_01_E_공중화장실정보.csv"

df= pd.read_csv(file, encoding='cp949', usecols = ["WGS84위도", "WGS84경도","소재지도로명주소"]) #소재지도로명주소, 위도, 경도 데이터 추출
#소재지도로명 주소를 추출하는 이유는 남구데이터를 뽑기위하여 #cp949로 인코딩 한 이유는 utf-8로 이 파일을 읽지못하였기 때문

df=df.rename(columns={"소재지도로명주소":"div태그","WGS84위도":"위도","WGS84경도":"경도"}) #제목변경
df = df.dropna(axis=0) # 경도, 위도 값 없는 항목 제거

is_namgu = df["div태그"].str.contains("남구") #소재지도로명 주소에 남구가 포함된 데이터들을 추출
df=df[is_namgu] #is_namgu 조건식에 맞는 데이터들 추출

temp = []
for i in df["div태그"]:
    temp.append(f'<div style="padding:5px">{i}</div>')  #div태그 값에 양옆에 <div>태그 열고 닫기 텍스트 추가
df["div태그"]=temp

col1=df.columns[-2:].to_list()
col2=df.columns[:-2].to_list()
new_col=col1+col2
df=df[new_col]  #순서 재배치

df=df.drop_duplicates() # 중복 제거
df.to_csv("data.csv",index=False)
########