<p align="middle">
  <img width="200px;" src="https://github.com/your-repo/logo.png" alt="Project Logo"/>
</p>

<h1 align="middle">Port MIS 민원 상담 AI 챗봇</h1>
<p align="middle">항만 물류 민원 상담의 효율화와 사용자 만족도를 향상시키는 AI 챗봇 프로젝트입니다.</p>

## 프로젝트 소개 📝

본 프로젝트는 항만 운영 업무 및 민원 업무를 처리하는 **Port-MIS(항만운영정보시스템)**을 기반으로, **민원 상담 서비스를 24시간 자동화**하여 상담원의 업무 부담을 줄이고 신속한 답변을 제공할 수 있도록 개발되었습니다. 이를 위해 **RAG(Retrieval-Augmented Generation)**와 파인 튜닝 기술을 결합하여 **Llama-3-PortMIS-Ko-8B** 모델을 사용합니다.

## 연구 발표 🏆

본 연구는 **"프롬프트 엔지니어링을 통한 RAG 기반 데이터셋 품질 개선과 파인 튜닝 적용 모델의 성능 비교 연구"**라는 제목으로 **ACK 2024 학회**에서 발표되었습니다. 연구의 주요 내용은 데이터셋 품질 향상 및 RAG+파인튜닝 모델의 성능 개선 효과를 중심으로 합니다.

## 기능 개요 🔍

- **데이터셋 생성 및 품질 개선**: Port-MIS 데이터의 PDF, OCR 이미지, CSV 파일 등을 전처리하여 Q&A 형식의 고품질 데이터를 구축하였습니다.
- **성능 평가**: RAGAS를 통해 생성된 데이터셋의 품질을 평가하고, Zero-shot 및 Few-shot 프롬프트를 비교하여 최적의 조합을 채택했습니다.
- **모델 테스트 및 성능 분석**: 모델의 성능을 Accuracy, BLEU Score, Response Time 지표로 평가하여 RAG+파인튜닝 모델이 가장 높은 성능을 나타냄을 확인했습니다.

## 데이터셋 평가 📈

RAGAS 라이브러리를 활용하여 생성된 데이터셋을 평가하였으며, Zero-shot과 Few-shot 프롬프트 방식을 비교하여 다음과 같은 성능 차이를 확인했습니다:

| Prompt Type | Model    | Faithfulness | Answer Relevancy | Context Recall | Context Precision | Answer Correctness |
|-------------|----------|--------------|------------------|----------------|-------------------|---------------------|
| Zero-shot   | GPT-4    | 0.7165       | 0.8207          | 0.9385         | 0.9692           | 0.9950              |
| Zero-shot   | GPT-4o   | 0.6837       | 0.7940          | 0.9231         | 0.9231           | 0.9845              |
| Few-shot    | GPT-4    | 0.7357       | 0.8120          | 0.9846         | 0.9692           | 0.9971              |
| Few-shot    | GPT-4o   | 0.7852       | 0.8078          | 1.0000         | 0.9846           | 0.9836              |

Few-shot 프롬프트 방식이 Zero-shot보다 전반적으로 더 높은 성능을 나타냈으며, 특히 Faithfulness 지표에서 큰 성능 차이를 보였습니다. 이러한 결과를 바탕으로 최종 데이터 생성 방식으로 **GPT-4o와 Few-shot 프롬프트** 조합을 채택하여 신뢰성 높은 고품질 데이터셋을 구축하였습니다.

## 기술 스택 💡

- **모델 아키텍처**: Llama-3-PortMIS-Ko-8B, RAG, LoRA, 4-bit Quantization
- **평가 도구**: RAGAS, BLEU Score
- **데이터 전처리**: PDF, OCR, CSV 등 다양한 포맷을 처리하여 LLM 학습에 최적화된 데이터셋 구축
- **최적화 기술**: Low-Rank Adaptation, Gradient Checkpointing

## 프로젝트 아키텍처 🏛

![LLM 학습 파이프라인](https://github.com/your-repo/path-to-architecture-diagram.png)

## 주요 성능 평가 결과 📊

| Model                      | Accuracy | BLEU Score | Response Time(s) |
|----------------------------|----------|------------|------------------|
| Base Model (Llama-3-Open-Ko-8B) | 63.3     | 0.42       | 2.5              |
| Llama-3-PortMIS-Ko-8B      | 75.4     | 0.83       | 2.8              |
| **RAG + Llama-3-PortMIS-Ko-8B** | **80.0** | **0.93**  | 3.2              |

## 기대 효과 🎉

**Port-MIS 민원 상담 챗봇**은 항만 물류 민원 서비스에서 **신속하고 정확한 답변**을 통해 **상담 업무 효율화**와 **사용자 만족도** 향상에 기여할 것입니다.

## 팀원 👨‍💻👩‍💻

| Name           | Role              | Team       | Email                       |
|----------------|-------------------|------------|-----------------------------|
| 김성언        | 팀장               | AI         | ykiki5778@inha.edu          |
| 박정현        | 팀원               | 프론트엔드, 백엔드 | anna010828@chungbuk.ac.kr   |
| 김산이        | 팀원               | 프론트엔드, 백엔드 | sanikani@chungbuk.ac.kr     |
| 유승미        | 팀원               | AI         | ysm0909@chungbuk.ac.kr      |
| 이수빈        | 팀원               | AI         | aksgdsmsehdan@o.cnu.ac.kr   |
| 박정규        | 멘토               | 프로젝트 총괄 | junggpark@lgcns.com         |

