from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)$',views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$',views.mysum),
    url(r'^mysum/(?P<numbers>\d+)/$',views.mysum),
    # url(r'^sum/(?P<numbers>[\d/]+)$', views.mysum),
    # url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
]

# ?P 뒤로는 정규표현식 영역을 써준다. \d+ 는 \d(숫자)가 1개 이상 들어갈 수 있다는 것!
# 인자 세개인 url만 지정하면 3개가 주어졌을 때만 작동함. 그래서 1개,2개인경우의 url을 추가해주어야 함.
# 하나의 url로 많은 숫자가 주어진 경우를 처리하려면?
# 정규표현식으로 자유롭게 url 파싱이 가능하다!!
