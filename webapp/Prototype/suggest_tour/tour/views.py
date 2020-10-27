from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from .models import TourlistSite
from .recommender import recommend
import json


# 메인뷰
def index(request):

    # if request.is_ajax():
        # lat = float(request.GET.get('Lat'))
        # lng = float(request.GET.get('Lng'))
      
    df = recommend(37.3947464,127.1090181)
    df_to_json = df.reset_index().to_json(orient='records')
    tourlist = list(json.loads(df_to_json))
    page = request.GET.get('page') #파라미터로 넘어온 현재 페이지값
    paginator = Paginator(tourlist, 5) # 한페이지에 5개씩 표시
    items = paginator.get_page(page) # 해당페이지에 맞는 리스트로 필터링
    content = {'tourlist':items }

    return render(request,'tour/index.html',content)


# 상세페이지뷰
def detail(request):
    if 'contentid' in request.GET:
        item = get_object_or_404(TourlistSite, contentid=request.GET.get('contentid'))
        return render(request, 'tour/detail.html', {'item': item})
    return HttpResponseRedirect('/tour/index/')

def test(request):
    content = {'tourlist':TourlistSite.objects.all() }

    return render(request,'tour/test.html',content)

def get_latlng(request):

    lat = request.GET.get('Lat')
    lng = request.GET.get('Lng')
    print(lat,lng)
    
    return JsonResponse({'message':"위도: "+lat+" 경도: "+lng})