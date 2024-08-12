import os

import click
import pandas as pd
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from autorag.data.qacreation import generate_qa_llama_index, make_single_content_qa

root_path = os.path.dirname(os.path.realpath(__file__))
prompt = """다음은 Port-MIS(해운항만물류정보시스템) 가이드북 내용입니다. 
Port-MIS(항만운영정보시스템, Port Management Information System)는 전국의 28개 무역항에 대하여 선박의 입항신고, 항만 내 시설사용, 관제사항, 화물반출입, 세입징수, 출항신고 등 모든 항만운영업무 및 민원업무를 처리하는 시스템입니다.

가이드북의 내용을 보고 사용자가 Port-MIS를 이용하는데에 있어 궁금할 만한 질문을 만드세요.
반드시 Port-MIS(해운항만물류정보시스템)과 관련한 질문이어야 합니다.
당신이 Port-MIS와 관련된 내용을 잘 알고 있는 전문가라고 생각하세요.
가능한 한 Port-MIS 가이드북 관련 규정과 지식을 최대한 활용하여 질문과 답변을 생성해주세요.

만약 주어진 내용이 Port-MIS와 관련되지 않았다면, 
'Port-MIS와 관련 없습니다.'라고 질문을 만드세요.

'''
Port-MIS 가이드북은 다음과 같은 내용으로 구성되어 있습니다. 참고해주세요. :
        포트미스 주요 서비스/이용 환경/회원가입 절차, 
        입·출항 선박에 대한 선박제원 등록,
        (변경) 절차 업무 흐름,
        외항선 민원신고 절차,
        내항선 민원신고 절차,
        외항선입항(출항)신고(최초,변경),
        승무원/승객명부,
        강제도선 면제신청,
        예선사용 면제신청,
        선박평형수신고,
        선박보안정보통보신고,
        저속운항선박지원신청,
        저속운항선박 인센티브 신청,
        항만시설사용허가신청서(선석신청),
        항만시설사용료(정박료)면제신청,
        위험물 반입신고 / 일람표신고,
        통합화물신고,
        외항입항(출항)신고(최종),
        항만시설사용신고(화물료),
        화물료 대납경비 청구,
        국가관리연안항신고 및 연안항 화물료 신고,
        서북도서출항신고,
        월정료선박사용신청,
        선박수리신고 신청 / 선박수리허가 신청,
        상계/환급 신청,
        포트미스 히스토리,
        부록 신고서식,
        항만시설 사용료 디지털 방식 
'''

Port-MIS 가이드북 내용:
{{text}}

생성할 질문 개수: {{num_questions}}

예시:
[Question]: 월정료선박 사용신청을 할 때 1년 선납시 어떤 혜택을 받을 수 있습니까?
[Answer]: 월정료선박 사용신청을 할 때 1년 선납시 사용료 10%를 할인받을 수 있습니다.

[Question]: 대한민국 항만에 입항하기 위해 선박은 어떤 정보를 제출해야 하나요?
[Answer]: 대한민국 항만에 입항하기 위해 선박은 선명, IMO 번호, 국적, 총톤수, 입항항만, 입항예정시각, 선박보안등급, 국제선박보안증서 번호와 유효기간, 발급기관명, 그리고 최근 기항한 10개 항만에 대한 보안정보를 제출해야 합니다.

사용자가 Port-MIS 가이드북을 통해 얻고자하는 내용과 관련이 없는 경우 예시:
[Question]: Port-MIS와 관련 없습니다.
[Answer]: Port-MIS와 관련 없습니다.

결과:
"""


@click.command()
@click.option('--corpus_path', type=click.Path(exists=True),
              default=os.path.join('data', 'corpus_new.parquet'))
@click.option('--save_path', type=click.Path(exists=False, dir_okay=False, file_okay=True),
              default=os.path.join('data', 'qa_new.parquet'))
@click.option('--qa_size', type=int, default=5)


def main(corpus_path, save_path, qa_size):
    
    load_dotenv()
    
    corpus_df = pd.read_parquet(corpus_path, engine='pyarrow')
    llm = OpenAI(model='gpt-4o', temperature=0.5)
    qa_df = make_single_content_qa(corpus_df, content_size=qa_size, qa_creation_func=generate_qa_llama_index,
                                   llm=llm, prompt=prompt, question_num_per_content=2) # content가 58개이므로 58*2=116개 질문 생성
    # delete if the output question is '포트미스와 관련 없습니다'
    qa_df = qa_df.loc[~qa_df['query'].str.contains('포트미스와 관련 없습니다')]
    qa_df.reset_index(drop=True, inplace=True)
    qa_df.to_parquet(save_path)


if __name__ == '__main__':
    main()