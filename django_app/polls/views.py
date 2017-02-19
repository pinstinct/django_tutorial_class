from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from .models import Question, Choice


def index(request):
    # pub_date 컬럼(필드)를 기준으로 내림차순 정렬(-pub_date, 마이너스)한 결과를 latest_question_list에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


    # 템플릿으로 분리 (원리)
    # # 템플릿 loader를 이용해서 'polls/index.html'에서 템플릿을 가져옴
    # template = loader.get_template('polls/index.html')
    #
    # # 템플릿 파일에 전달할 context 객체를 정의
    # # 'latest_question_list' 키에 값을 할당
    # # 해당 키를 템플릿에서 사용
    # context = {'latest_question_list': latest_question_list, }
    #
    # # 템플릿에 context와 request 객체를 사용해 render한 결과를 반환
    # return HttpResponse(template.render(context, request))

    # 뷰를 직접구현
    # output = ', '.join([q.q_text for q in latest_question_list])
    # # 디버그 테스트
    # # request 객체 확인해보기
    # # request는 사용자가 요청할 때 담아보내는
    # output2 = ''
    # for q in latest_question_list:
    #     output2 += q.q_text + ', '
    # output2 = output2[:-2]
    #
    # return HttpResponse(output2)


def detail(request, question_id):
    """
    request.method == 'POST'일 때, 전달받은 POST객체에서
        'choice' 키 값을 HttpResponse로 되돌려준다.
        'choice' 키로 전달된 Choice 객체의 id를 이용해서
        해당 Choice 객체의 votes 값을 1 늘려주고 데이터베이스 업데이트
        완료되면 다시 Question detail 페이지로 이동

        1. request.Post['choice']의 값(Choice객체의 ID)을 이용해서 Choice 객체를 가져온다
        2. 해당 객체의 votes 값을 늘려주고, 데이터베이스에 변경사항을 업데이트
        3. redirect, question_id를 이용해서 detail 페이지로 다시 돌아간다
    아닐 경우 polls/detail.html을 render
    """
    if request.method == 'POST':
        # 1번
        try:
            choice_id = request.POST['choice']
            choice = Choice.objects.get(id=choice_id)

        except MultiValueDictKeyError:
            return HttpResponse('test')

        # 2번번
        choice.votes += 1
        choice.save()

        # 3번
        return redirect('polls:results', question_id=question_id)

    else:
        question = Question.objects.get(id=question_id)
        context = {
            'question': question,
        }
        return render(request, 'polls/detail.html', context)


def results(request, question_id):
    # 인자로 주어진 question_id에 해당하는 Question 객체를 context에 담아 render에 보낸다
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)




def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
