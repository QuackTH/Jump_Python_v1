# def gugu(n):
#     result = []
#     result.append(n * 1)
#     result.append(n * 2)
#     return(result)
# print(gugu(2))
# """반복이 너무 많다 반복문을 사용하자"""

# #해당 반복문을 gugu 함수에 적용해보자
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
    

def gugu(n):                    # 함수 선언
    result = []                 # 결과값은 리스트로 받겠다 선언
    i = 1                       # 변수 선언, 초기화 / 1로 초기화 하지않으면 컴퓨터는 메모리 어딘가에 저장된 i라는 이름의 상자를 찾아서 그 안에 든 값을 꺼내려고 
                                # 하는데 초기화 하지않을 경우 i가 대체 뭔데? 상태에 빠집니다. 컴퓨터에게 변수의 존재를 알리고, 공정한 레이스를 시작할 출발선을 그어주는 
                                # 작업"입니다. 이 출발선이 없으면 컴퓨터는 레이스 자체를 거부합니다.

    while i < 10:               # while문과 조건식
        result.append(n*i)      # 실행문 1 (명령문)/ 입력받은 n 에 i 를 곱해 추가합니다. / n 과 i를 곱한 결과값을 result 라는 리스트의 맨 뒤에 붙이는 동작을 수행
        i = i + 1               # 실행문 2 / - 할당문
    return result               # 반환문
print(gugu(2))                  # 출력문
    
