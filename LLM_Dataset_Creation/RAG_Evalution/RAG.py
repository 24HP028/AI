import os
import json

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    answer_correctness,
    context_recall,
    context_precision,
)
from datasets import Dataset

# RAGAS 평가를 위한 평가 지표 설정
metrics = [
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
    answer_correctness,
]

# JSON 파일 경로 설정
file_path = '(2024)포트미스+가이드북.pdf_65_20240805.json'

# JSON 파일 읽어오기
with open(file_path, 'r', encoding='utf-8') as file:
    qa_dataset = json.load(file)

# 데이터 확인
for entry in qa_dataset:
    print(f"CONTEXT: {entry['CONTEXT']}")
    print(f"QUESTION: {entry['QUESTION']}")
    print(f"ANSWER: {entry['ANSWER']}\n")

# 평가를 위해 필요한 필드 추출
test_questions = [entry["QUESTION"] for entry in qa_dataset]
test_groundtruths = [entry["ANSWER"] for entry in qa_dataset]
contexts = [[entry["CONTEXT"]] for entry in qa_dataset]

# 평가 데이터셋 생성
response_dataset = Dataset.from_dict({
    "question": test_questions,
    "answer": test_groundtruths,  # 이 예제에서는 정답을 answer로 대체
    "contexts": contexts,
    "ground_truth": test_groundtruths
})

# dataset 첫 번째 데이터 확인
print(response_dataset[0])

# RAGAS 평가 수행
evaluation_results = evaluate(response_dataset, metrics, raise_exceptions=False)

# 평가 결과 출력
print("RAGAS 평가 결과:")
for metric_name, score in evaluation_results.items():
    print(f"{metric_name}: {score:.4f}")

