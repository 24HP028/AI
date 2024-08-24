from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langserve import add_routes
from chain import chain 

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/prompt/playground")

# POST endpoint for /prompt/playground/ to handle chat requests
@app.post("/prompt/playground/")
async def handle_prompt_playground(request: Request):
    data = await request.json()  # POST 요청으로 들어온 JSON 데이터를 추출
    topic = data.get("topic")  # 클라이언트로부터 "topic"을 받아옴
    
    # topic이 제공되지 않았을 때 처리
    if not topic:
        return JSONResponse(content={"error": "Topic is required."}, status_code=400)
    
    # chain을 사용해 응답 생성 (동기적으로 호출)
    response = chain.invoke(topic)  # invoke 메서드를 사용하여 결과를 생성

    # 결과 반환
    return JSONResponse(content={"response": response})

# 필요에 따라 추가 라우트를 정의할 수 있습니다.

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
