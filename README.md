# AI


### Port-Pilot chatbot I/O example

- How to Test
```
python chatbot_ex.py 'input'
```

- Output
```
{
    "status": 200,
    "message": "채팅 응답 성공",
    "body": {
        "chatMessage": "입항 신고 절차는 다음과 같습니다:\n1. 무역항의 수상구역 등 안으로 입항하는 경우에 신고합니다.\n2. 선박이 입항하기 전에 입항 예정 정보를 최초로 신고합니다.\n3. 실제 선박이 입항한 후에 최종적으로 입항을 신고합니다.\n\n또한, 선박에 탑승한 승무원/승객에 대한 성명, 국적, 승하선 일자, 승무원 직명, 여권번호 또는 선원수첩번호 등의 인적사항을 신고해야 합니다."
    }
}
```