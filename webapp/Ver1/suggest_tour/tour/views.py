from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from django.template import loader, RequestContext
from .models import TourlistSite
from .recommender import recommend
import json


# 메인뷰
def index(request):
    mapx = request.session['gps_x']
    mapy = request.session['gps_y']

    if request.POST:
        mapx =  float(request.POST.get('lat'))
        mapy =  float(request.POST.get('lng'))

    df = recommend(mapx, mapy)

    df_to_json = df.reset_index().to_json(orient='records')
    tourlist = list(json.loads(df_to_json))

    page = request.GET.get('page') #파라미터로 넘어온 현재 페이지값
    paginator = Paginator(tourlist, 5) # 한페이지에 5개씩 표시
    items = paginator.get_page(page) # 해당페이지에 맞는 리스트로 필터링
    content = {'tourlist':items }

    request.session['gps_x'] = mapx
    request.session['gps_y'] = mapy

    return render(request, 'tour/index.html', content)


# 상세페이지뷰
def detail(request):
    if 'tour_id' in request.GET:
        positiveWord = []
        negativeWord = []
        commonWord = []
        corona_count = 1
        congestion_count = 1

        mapx = request.session['gps_x']
        mapy = request.session['gps_y']

        tourData = get_object_or_404(TourlistSite, tour_id=request.GET.get('tour_id'))
        analysisData = get_object_or_404(AnalysisReseult, tour_id=request.GET.get('tour_id'))

        #감성단어
        res = ast.literal_eval(analysisData.senti_word)
        for i in range(len(res)):
            if res[i][1] > 0:
                positiveWord.append(res[i][0])
            elif res[i][1] < 0:
                negativeWord.append(res[i][0])
            elif res[i][1] == 0:
                commonWord.append(res[i][0])
        
        #코로나
        if analysisData.corona_score > 0.015353:
            corona_count = 2
        elif analysisData.corona_score > 0.029890:
            corona_count = 3

        #혼잡도
        if analysisData.congestion_score > 0.425635:
            congestion_count = 2
        elif analysisData.congestion_score > 0.473350:
            congestion_count = 3


        count_result = {'corona_count':corona_count,
                        'congestion_count':congestion_count}

        #거리계산
        scale_data["dist"] = tour_data.apply(lambda x: haversine(cur_location, (x['mapy'], x['mapx'])), axis=1)

        content = {'tourData': tourData, 
        'analysisData':analysisData,
        'positiveWord':positiveWord,
        'negativeWord':negativeWord,
        'commonWord':commonWord,
        'count_result':count_result }

        return render(request, 'tour/detail.html',content )
    return HttpResponseRedirect('/tour/index.html')

