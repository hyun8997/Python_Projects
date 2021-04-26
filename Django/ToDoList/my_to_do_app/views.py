from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    todos = ToDo.objects.all()  # ToDo라는 객체를 통해 모두 가져오겠다
    content = {'todos' : todos}  # 이놈이 request로 넘어감
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    input = request.POST['todoContent']

    content = ToDo(contents = input)
    content.save()  # 객체 생성 컨텐츠를 넣어줌, ORM 방식에 의해 함수를 쓰면 알아서 sql문 동작
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse('createTodo page : ' + input)

def doneTodo(request):
    done_id = request.GET['todoNum']
    todo = ToDo.objects.get(id = done_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

def completeTodo(request):   # 위 함수는 아예 삭제, 얘는 불리안 써서 안보이게만
    complete_id = request.GET['todoNum']
    todo = ToDo.objects.get(id = complete_id)  #객체를 db에서 찾아서 가져오기
    todo.doDone = True  # doDone default False를 True로 변경
    todo.save()  # 저장, 업데이트가 없고 덮어쓰기임 인지
    return HttpResponseRedirect(reverse('index'))







