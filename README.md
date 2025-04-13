# 🇰🇷 한글 문장 감성 분석기 (Sentiment Analyzer for Korean)

## ✨ 프로젝트 개요
일상 속 문장에 담긴 감정을 자동으로 분석해주는 한글 감성 분석 웹앱입니다.  
사용자는 문장을 입력하면 해당 문장이 **긍정 / 부정 / 중립** 중 어떤 감정인지 분류하고,  
세부 감정 분포를 **원형 그래프**로 시각화합니다.

## 🧠 아이디어 배경
- 감정이 담긴 텍스트를 자동 분석하는 서비스는 많지만, **한국어에 특화된 감성 분석 도구는 드뭅니다.**
- 간단한 웹앱만으로 감성 결과를 확인할 수 있도록 기획했습니다.
- 한글 데이터에 적합한 모델을 직접 찾아 적용해보는 실습 목적도 포함됩니다.

## 🛠 사용한 기술 스택

| 분류 | 사용 도구 |
|------|-----------|
| 언어 | Python |
| 딥러닝 | PyTorch |
| NLP | Hugging Face Transformers |
| 웹 | Streamlit |
| 시각화 | Plotly |
| 배포 | Hugging Face Spaces |
| 모델 | nlp04/korean_sentiment_analysis_kcelectra |

## 👥 역할 분담
- 팀원 1: 모델 학습 및 전처리
- 팀원 2: Streamlit UI 구현
- **팀원 3 (나): 앱 통합, 시각화, Hugging Face 배포**

## 🧩 주요 구현
- 문장을 10개 세부 감정으로 분류 후 → 긍정/부정/중립 매핑
- Plotly로 감정 분포 시각화
- Hugging Face에 배포 완료

## 🖥 데모 링크
👉 [앱 실행하러 가기](https://huggingface.co/spaces/Yeowa-ksn/Sentiment-Streamlit-App)

## 🧪 사용법
1. 문장을 입력하고
2. `감정 분석` 버튼 클릭
3. 감정 결과와 원형 차트 확인

## 📝 피드백 받고 싶은 점
- 감정 매핑 방식
- 시각화 레이아웃 개선 아이디어
- 한글 감정 데이터 확장 아이디어

## 🗂 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py

