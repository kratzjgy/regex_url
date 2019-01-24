from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    # request: HttpRequest
    # result = sum(map(int, numbers.split("/")))
    # result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(numbers)
    # return HttpResponse(result)

# int(x)안해주면 x를 문자로 받아오기 때문에 오류남.
# y,z의 기본 인자값을 0으로 줌으로써, x인자값만 입력했을 때에도 작동하도록 할 수 있다!!
# 위처럼 numbers로 해주고 url을 작성해주면 /123/14/123/123/ 와 같은 인자들을 하나의 통 문자로 받아온다. 그럼 각각의 숫자를 더해주려면?
# url에 빈 문자값이 포함되는 경우가 있을 것. 그러면 오류남. 위에 추가해준 lambda s: int( s or 0 ) --> false 일떄( 빈 값일 때 ) 0을 대입해준다.

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))
