import re

# 1글자 패턴

## [] => 대괄호 안에 있는 것들 중 하나만 들어갈 수 있다는 표시. ex) [0123456789] : 0-9까지의 숫자 중 하나만 표현이 가능하다. 줄여서 [0-9] 또는 '\d'라고도 가능.
## 그럼 알파벳은 "[a-zA-z]" 알파벳 대/소문자 중 1글자
## 한글 1글자 : "[ㄱ-힣]"
## 문자열 시작 '^', 끝 '$'

# val = "01012341234"

# pattern = r"^01[016789][1-9]\d{6,7}$"
## 전화번호 표현 정규식!
## 시작과 끝을 정해주면, 위에서는 시작은 무조건 0으로 시작하고 끝날 땐 숫자로 끝난다는 표시.

def validate_phone_number(number):
    if not re.match(r'^01[016789][1-9]\d{6,7}$',number):
        return False
    return True

print(validate_phone_number('01012341234'))
print(validate_phone_number('1231111'))
