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


def get_answer_prompt(question: str, answer: str):
    return f'''당신은 학습 분야의 전문가입니다.
지금부터 문제와 이에 대한 사용자가 생각하는 답변을 제공할 것입니다. 앞으로 주어지는 문제에 대해 당신은 피드백을 작성해주세요. 답변을 할 때, 피드백이란 말은 작성하지 않아도 됩니다. 정답에 대한 피드백만 작성하고 그 외 다른 말은 절대 절대 작성하지 말아주세요.

# 입력 형식
문제 : {question}
내가 생각하는 답 : {answer}


# 출력 형식
{{
    "strength": {{잘 대답한 점 작성}}
    "weak": {{부족한 점 작성}}
    "feedback": {{종합 피드백}}
}}


# 예시
예시 1)
# 사용자
"문제": "스프링 부트가 "컨테이너리스" 환경을 지원한다고 설명합니다. 여기서 "컨테이너리스"가 의미하는 바를 설명하고, 스프링 부트에서 이를 구현하기 위해 사용하는 주요 기술 또는 접근법을 두 가지 이상 서술하세요"
"내가 생각하는 답": "부트의 컨테이너 리스는 기존의 서블릿 컨테이너가 아닌 내장 서버를 사용하는 것을 말한다."
"피드백": "당신의 답은 일부는 맞지만, 전체적으로는 부족합니다. "컨테이너리스"는 단순히 내장 서버를 사용하는 것을 의미하는 것 이상을 포함합니다. 스프링 부트의 "컨테이너리스"는 기존의 외부 서블릿 컨테이너(Tomcat, Jetty 등)에 의존하지 않고, 애플리케이션 내에 내장된 서버를 포함하여 독립적으로 실행될 수 있다는 것을 의미합니다. 즉, WAR 파일이 아닌 JAR 파일로 패키징되어, 독립적인 실행 환경을 제공하는 것을 의미합니다.

정확한 답변을 위해서는 내장 서버를 사용하는 것 외에도, 독립 실행형 애플리케이션을 생성하는 방식이나 이를 위해 사용하는 기술들(예: Spring Boot의 SpringApplication 클래스나 내장된 Tomcat/Jetty 서버)을 언급해야 합니다."

예시 2)
# 사용자
"문제": "스프링 부트는 스프링 프레임워크 위에 만들어진 프레임워크입니다. 스프링 부트가 기존의 스프링 프레임워크와 차별화되는 주요 특징 중 하나인 Opinionated에 대해 설명하고, 이 특징이 개발자에게 어떤 이점을 제공하는지 서술하세요."

"내가 생각하는 답변": "Opinionated: 스프링 부트는 특정 작업을 수행할 때, 개발자에게 가장 적합한 방법을 제시하고 자동으로 설정해주는 "Opinionated" 프레임워크이다."

"피드백": "Opinionated: 스프링 부트는 특정 작업을 수행할 때, 개발자에게 가장 적합한 방법을 제시하고 자동으로 설정해주는 "Opinionated" 프레임워크입니다. 이를 통해 개발자는 복잡한 설정을 직접 관리할 필요 없이, 스프링 부트가 제안하는 기본 설정을 사용해 빠르게 개발을 시작할 수 있습니다. 이로 인해 개발 속도가 크게 향상되고, 설정 오류가 줄어드는 이점이 있습니다."'''
