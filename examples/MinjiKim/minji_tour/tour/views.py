from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import TourInfo


# 메인뷰
def index(request):
    tourlist = TourInfo.objects.all()
    page = request.GET.get('page') #파라미터로 넘어온 현재 페이지값
    paginator = Paginator(tourlist,5) # 한페이지에 5개씩 표시
    items = paginator.get_page(page) # 해당페이지에 맞는 리스트로 필터링
    content = {'tourlist':items }

    return render(request,'tour/index.html',content)

# 상세페이지뷰
def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(TourInfo, pk=request.GET.get('id'))
        return render(request, 'tour/detail.html', {'item': item})
    return HttpResponseRedirect('/tour/index/')