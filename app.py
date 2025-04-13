
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import plotly.express as px

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("nlp04/korean_sentiment_analysis_kcelectra")
    model = AutoModelForSequenceClassification.from_pretrained("nlp04/korean_sentiment_analysis_kcelectra")
    return tokenizer, model

def analyze_sentiment(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1).detach().numpy()[0]
    label_id = probs.argmax()

    # 모델이 제공하는 감정 라벨
    id2label = model.config.id2label
    fine_label = id2label[label_id]

    # 감정 라벨 → 긍/부정/중립 매핑
    fine_to_coarse = {
        '기쁨': '긍정', '사랑': '긍정',
        '슬픔': '부정', '분노': '부정', '혐오': '부정', '상처': '부정',
        '불안': '중립', '놀람': '중립', '당황': '중립', '중립': '중립'
    }

    coarse_label = fine_to_coarse.get(fine_label, "중립")
    return coarse_label, probs

def plot_sentiment_probs(probs, model):
    labels = list(model.config.id2label.values())
    fig = px.pie(
        names=labels,
        values=probs,
        title="감정 분석 세부 분포",
        color=labels
    )
    return fig

# ✅ Streamlit 앱 UI
st.title("🇰🇷 한글 문장 감성 분석기")

text = st.text_area("문장을 입력하세요:")

if st.button("감정 분석"):
    tokenizer, model = load_model()
    label, probs = analyze_sentiment(text, tokenizer, model)
    st.markdown(f"### 🔍 예측 결과: **{label}**")
    fig = plot_sentiment_probs(probs, model)
    st.plotly_chart(fig)
