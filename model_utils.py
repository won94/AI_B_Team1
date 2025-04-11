
from model_utils import load_sentiment_model

classifier = load_sentiment_model()
text = "기분이 정말 좋아요!"
result = classifier(text)
print(result)
