# if문

# money = False
# if money:
#     print("택사룰 타고 가라")
# else:
#     print("걸어가라")



# x = 10
# y = 4
# if x = y:
#     print("True")
# else:
#     print("False")

# x = 3
# y = 2
# print(x == y)

# money = 1000
# card = True
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# a = 1 in [1, 2, 3, 4]
# print(a)

# b = 1 not in [1, 2, 3, 4]
# print(b)

# pocket = ["papaer", "cellphone", "money"]
# if "money" in pocket:
#     print("택시를 타고 가라")   
# else:
#     print("걸어가라")



#     pocket = ["paper", "cellphone", "money"]
# if "paper" in pocket:
#     print("택시를 타고 가라")   
# else:
#     print("걸어가라")



# pocket = ["money", "card"]
# if "money" in pocket:
#     print("가만히 있다")
#     pass
    
# else:
#     print("카드를 꺼내라")


# # elif
# pocket = ["paper", "cellphone"]
# card = True
# if "moneny" in pocket:
#     print("택시를 타고 가라")
# elif card:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")


# pocket = ["paper", "money", "cellphone"]
# if "money" in pocket: print("택시를 타라")
# else: print("카드를 꺼내라")

# while문
# 문장을 반복해서 수행해야하는 경우 while문을 사용한다

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무가 넘어갑니다.")


# # while문 예시 1
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다")
#         break


# # while문 예시 2
# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요 : "))
#     if money == 300:
#         print("커피를 받으세요.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름 돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("거슴돈 %d를 주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if  coffee == 0:
#             print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#             break


# # 홀수만 반복 출력하기
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue
#     print(a)

a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)