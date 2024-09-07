def get_summary_prompt(context: str):
    return f'''
# 요구 사항
- **html문서로 작성해주세요. 가독성을 고려해야 합니다.**
- **문장이 길다고 판단되면 다음 줄에 작성해주세요.**
- 내용: []에 오는 내용을 사람이 읽기 좋게 가독성을 고려해서 요약해주세요.
- 모르는 정보면 모른다고 답변해주세요.
- 답변 전 내용을 스스로 검증하고 대답해주세요.
- url을 제공해주는 경우 해당 url이 정상적인 http 상태를 반환하는 경우에만 제공해주세요
- 종결 어미는 '~이다'로 끝내주세요.
- '\n'보다는 태그를 이용한 줄바꿈을 이용해주세요 
- 코드가 포함된다면 ``` ``` 안에 작성해주세요

## 강의 목적
- 강의 목적 앞에는 "강의 목표: " 라는 말을 붙여주세요

## 용어 설명
- 강의에서 정의를 설명하는 부분을 정리해주세요
- {{용어 한국어명(영어명)}} : {{용어 설명}} 과 같이 정리해주세요
- 용어 설명에는 절대 절대 종결 어미를 붙이지 마세요

## 본문 요약
- 본문 요약 내용은 주제에 맞게 2개 이상으로 나누어 작성해주세요
- 강의 요약 내용은 p 태그로 보여주고 display: block style을 주어서 문장이 너무 길면 다음 줄에 나오도록 작성해주세요.
- 본문의 내용은 소주제에 따라 각각의 문단으로 정리해주세요.
- 각각의 본문 요약에 소제목을 작성해주세요
- 코드가 포함된다면 코드는 반드시 포함시켜주세요.
  - 코드는 ``` ``` 태그로 감싸서 작성해주세요
  - 기존 코드가 있고 이를 최적화할 수 있는 코드를 작성할 수 있다면 최적화된 코드를 함께 작성해주세요

## 강의 요약
- 10문장 이하로 작성해주세요
- 결론에는 강의의 가장 중요한 내용만 넣어주세요
- 개조식으로 작성해주세요
- ul 태그로 묶고 각 문장을 li 태그로 작성해주세요

### 관련 자료 추천
- [본문 요약] 위치에는 강의 내용을 정리한 글을 작성하고 이해를 돕는 내용을 추가해주세요.  
- 관련 레퍼런스에는 해당 강의 주제와 관련해서 더 공부하기 좋은 내용을 작성해주세요.
  - 책을 추천한다면 'https://search.kyobobook.co.kr/search?keyword={{책이름}}'을 답변해주세요
  - 공식 문서를 추천한다면 공식 문서의 url을 포함해서 답변해주세요
  - 관련 웹 사이트나 웹 문서를 추천한다면 해당 문서의 url을 포함해서 답변해주세요


# 답변 양식 예시
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
<h2>강의 목적</h2>
<ul>
    <li></li>
    <li></li>
</ul>
 
<h2>용어 정리</h2>
    <li></li>
    <li></li>
    <li></li>

<h2>본문요약</h2>
  <h3>본문요약1</h3>
  <p>본문 내용</p>
  <code>
    Member member = new Member();
    member.setId("member1");
    member.setUsername("회원1");
  </code>
  
  (최적화된 코드)
  <code>
    // 최적화되었거나 추천하는 코드를 작성
    // 추천하는 코드가 없다면 작성하지 않아도 됩니다
  <code>
    
    
  <h3>본문요약2</h3>
  <p>본문 내용</p>

<h2>결론</h2>
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>

<h2>관련 레퍼런스</h2>
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
<body>
</html>
---
내용: [{context}]
'''
