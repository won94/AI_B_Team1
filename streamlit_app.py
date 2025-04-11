import streamlit as st

# 헤더
st.title("문장 감성 분석기")
st.write("이 앱은 입력한 문장의 감성을 분석하여, 긍정, 부정, 중립을 판단합니다.")

# 사용자 입력 받기
user_input = st.text_input("감성 분석할 문장을 입력하세요:")

# 분석 버튼 클릭 시
if st.button("분석하기"):
    if user_input:
        # 감성 분석 결과 출력 (모델이 없는 경우 임시 결과)
        # 모델이 준비되면 아래 부분을 모델 연동 코드로 바꿔주세요
        st.write("분석 결과는 아직 없습니다. 모델을 준비한 후, 결과를 표시할 예정입니다.")
        
        # 예시 결과 (모델이 준비되면 이 부분은 동적으로 바뀌게 됩니다)
        sentiment = "긍정적"  # 추후 모델을 기반으로 동적으로 결과를 결정
        
        if sentiment == "긍정적":
            st.write("🙂 긍정적인 문장입니다!")
        elif sentiment == "부정적":
            st.write("😞 부정적인 문장입니다.")
        else:
            st.write("😐 중립적인 문장입니다.")
    else:
        st.write("먼저 문장을 입력해주세요!")
