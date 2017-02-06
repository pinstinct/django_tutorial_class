from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


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
    # # 해당 키로 템플릿에서 사용
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
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
