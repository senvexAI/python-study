## Type -> have method
- F-string : f-string을 사용하려면 문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수를 넣습니다. 
print(f"blah~ blah {variable1}")
- String
- Integer
- Float
- List : ["a","b","D"]
- Dictionary -> {"key1": "value", "key2": "value2"}
    In case of add or update -> dictionary["new key"]="new value"
- boolean: ONLY True or False
- Set

## Function
- print()
- type()
- len()
- input()
- range()
- sum()

## Definition
- Squre Bracket [] : 리스트, 인덱싱, 슬라이싱
- Parenthesis () : 함수 호출, 튜플
- Curly braces {} : 딕셔너리, 집합

## 1. 기본 데이터 타입

- **문자열(String)**  
  - 예: `"hello"`, `'world'`
  - f-string: `f"Hello, {name}!"`

- **정수(Integer)**  
  - 예: `10`, `-3`

- **실수(Float)**  
  - 예: `3.14`, `-0.5`

- **리스트(List)**  
  - 예: `["a", "b", "c"]`
  - 인덱싱/슬라이싱: `my_list[0]`, `my_list[1:3]`

- **딕셔너리(Dictionary)**  
  - 예: `{"key": "value", "age": 20}`
  - 값 추가/수정: `d["new_key"] = "new_value"`

- **불리언(Boolean)**  
  - `True`, `False`

- **집합(Set)**  
  - 예: `{1, 2, 3}`

---

## 2. 연산자(Operators)

- **산술**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **비교**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **논리**: `and`, `or`, `not`
- **할당**: `=`, `+=`, `-=`, `*=`, `/=`

---

## 3. 함수(Function)

- **정의**  
  ```python
  def 함수이름(매개변수):
      return 결과
  ```
- **호출**: `함수이름(인자)`

- **내장 함수 예시**  
  - `print()`, `type()`, `len()`, `input()`, `range()`, `sum()`

---

## 4. 조건문(Conditional)

```python
if 조건:
    ...
elif 조건:
    ...
else:
    ...
```

---

## 5. 반복문(Loop)

- **for문**
  ```python
  for i in range(5):
      print(i)
  ```
- **while문**
  ```python
  while 조건:
      ...
  ```

---

## 6. 리스트와 메서드

- **리스트에 값 추가/삭제**
  ```python
  my_list.append("new")
  my_list.remove("old")
  ```

- **예시: 특정 값 삭제**
  ```python
  countries = ["Colombia", "Peru", "Brasil", "Japan", "Argentina"]
  countries.remove("Japan")
  ```

---

## 7. 들여쓰기(Indentation)

- 반복문, 조건문 등에서 코드 블록은 반드시 들여쓰기(보통 4칸)로 구분

---

## 8. 예외 처리(Exception Handling)

```python
try:
    ...
except Exception as e:
    print(e)
```

---

## 9. 모듈, 패키지, 라이브러리

- **모듈(Module)**: 하나의 `.py` 파일
- **패키지(Package)**: 여러 모듈을 모아놓은 폴더(보통 `__init__.py` 포함)
- **라이브러리(Library)**: 여러 패키지/모듈의 집합 (예: NumPy, Pandas)

- **모듈 사용 예시**
  ```python
  import math
  print(math.sqrt(16))
  ```

---

## 10. 파일 경로와 작업 디렉토리

- 파이썬은 기본적으로 현재 작업 디렉토리에서 파일을 찾음
- 현재 디렉토리 확인:  
  ```python
  import os
  print(os.getcwd())
  ```

---

## 11. dir() 함수

- 객체의 모든 속성과 메서드 확인
  ```python
  print(dir("string"))
  print(dir(0))
  print(dir([]))
  print(dir({}))
  ```

---

## 12. 매직 메서드(Magic/Dunder Methods)

- `__add__`, `__len__`, `__getitem__` 등
- 예: `len(my_list)` → `my_list.__len__()`

---

## 13. 함수의 매개변수(Parameter)와 인자(Argument)

- **매개변수(Parameter)**: 함수 정의 시 사용
- **인자(Argument)**: 함수 호출 시 전달

  ```python
  def greet(name):  # name: 매개변수
      print("Hello, " + name + "!")

  greet("Alice")  # "Alice": 인자
  ```

---

## 14. API란?

- **API (Application Programming Interface)**
  - 프로그램 간 소통을 위한 규칙/도구
  - 예: 날씨 앱이 외부 서버에서 데이터 받아오기

- **동작 방식**
  1. 요청(request)
  2. 처리
  3. 응답(response)

- **활용 예시**
  - 날씨 정보, 지도, 결제 등

---

## 15. 실전 예시: 리스트에 결과 저장

```python
promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"Flavor: {flavor}"
    description = get_llm_response(prompt)
    promotional_descriptions.append(description)
```



## Argument vs Parameter in Function

- **Parameter**: 함수 정의(def)에서 사용하는 변수(placeholder).  
  - "A parameter is a variable in the function definition."
- **Argument**: 함수 호출(call) 시 실제로 전달하는 값.  
  - "An argument is the actual value supplied to the function."

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # "Alice" is the argument
```
- In this example, name is the parameter in the function definition, and "Alice" is the argument we pass to the function when calling it.

