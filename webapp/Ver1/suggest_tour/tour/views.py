from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.paginator import Paginator
from django.template import loader, RequestContext
from .models import TourlistSite,AnalysisReseult
from .recommender import recommend
import json
import ast

# 메인뷰
def tour_first(request):
    mapx = request.session["gps_x"]
    mapy = request.session["gps_y"]
    category = 'none'
    dist = 'none'
    congestion = 'none'

    df = recommend(mapx, mapy, category, dist, congestion)

    try:
        df_to_json = df.reset_index().to_json(orient='records')
        tourlist = list(json.loads(df_to_json))

        #코로나
        for i in range(len(tourlist)):
            if tourlist[i]["corona_score"] < 0.001966:
                tourlist[i]["corona_count"] = 0
            elif tourlist[i]["corona_score"] < 0.015353:
                tourlist[i]["corona_count"] = 1
            elif tourlist[i]["corona_score"] < 0.029890:
                tourlist[i]["corona_count"] = 2
            else:
                tourlist[i]["corona_count"] = 3
        
        #혼잡도
        for i in range(len(tourlist)):
            if tourlist[i]["congestion_score"] < 0.425635:
                tourlist[i]["congestion_count"] = 1
            elif tourlist[i]["congestion_score"] < 0.473350:
                tourlist[i]["congestion_count"] = 2
            else :
                tourlist[i]["congestion_count"] = 3

        page = request.GET.get('page') #파라미터로 넘어온 현재 페이지값
        paginator = Paginator(tourlist, 9) # 한페이지에 9개씩 표시
        items = paginator.get_page(page) # 해당페이지에 맞는 리스트로 필터링
        content = {'tourlist':items }
    except AttributeError:
        content = {}
    except TypeError:
        content = {}


    return render(request, 'tour/index.html', content)

def tour_search(request):
    if request.POST:
        mapx =  float(request.POST.get('lat'))
        mapy =  float(request.POST.get('lng'))
        addr_info = request.POST.get('addr_info')
        category = request.POST.get('category')
        dist = request.POST.get('dist')
        congestion = request.POST.get('congestion')
    else:
        mapx = request.session["gps_x"]
        mapy = request.session["gps_y"]
        addr_info = request.session["address"]
        if request.session["category"]:
            category = request.session["category"]

        if request.session["dist"]:
            dist = request.session["dist"]
        
        if request.session["congestion"]:
            congestion = request.session["congestion"]

    df = recommend(mapx, mapy, category, dist, congestion)
    
     # 검색결과출력리스트
    search_category = {category == 'A' :'관광지',category=='B':'부대시설',category=='C':'숙박업소'}.get(True,'전체')
    search_dist = {dist == 5:'5km 이내',dist==10:'10km 이내',dist==20:'20km 이내',dist==30:'30km 이내'}.get(True,'전체')
    search_congestion = {congestion == 'A' :'쾌적',congestion=='B':'보통',congestion=='C':'혼잡'}.get(True,'전체')

    search_info = {"search_category": search_category,
                    "search_dist": search_dist,
                    "search_congestion": search_congestion,
                    "addr_info": addr_info}

    try:
        df_to_json = df.reset_index().to_json(orient='records')
        tourlist = list(json.loads(df_to_json))
        #코로나
        for i in range(len(tourlist)):
            if tourlist[i]["corona_score"] < 0.001966:
                tourlist[i]["corona_count"] = 0
            elif tourlist[i]["corona_score"] < 0.015353:
                tourlist[i]["corona_count"] = 1
            elif tourlist[i]["corona_score"] < 0.029890:
                tourlist[i]["corona_count"] = 2
            else:
                tourlist[i]["corona_count"] = 3
        
        #혼잡도
        for i in range(len(tourlist)):
            if tourlist[i]["congestion_score"] < 0.425635:
                tourlist[i]["congestion_count"] = 1
            elif tourlist[i]["congestion_score"] < 0.473350:
                tourlist[i]["congestion_count"] = 2
            else :
                tourlist[i]["congestion_count"] = 3

        page = request.GET.get('page') #파라미터로 넘어온 현재 페이지값
        paginator = Paginator(tourlist, 9) # 한페이지에 9개씩 표시
        items = paginator.get_page(page) # 해당페이지에 맞는 리스트로 필터링
        content = {'tourlist':items,
                    'search_info':search_info}

        request.session['gps_x'] = mapx
        request.session['gps_y'] = mapy
        request.session['category'] = category
        request.session['dist'] = dist
        request.session['congestion'] = congestion
    except AttributeError:
        content = {}
    except TypeError:
        content = {}

    return render(request, 'tour/index.html', content)


# 상세페이지뷰
def detail(request):
    if 'tour_id' in request.GET:
        positiveWord = []
        negativeWord = []
        commonWord = []
        corona_count = 1
        congestion_count = 1
        
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
        if analysisData.corona_score <= 0.001966:
            corona_count = 0
        elif analysisData.corona_score <= 0.015353:
            corona_count = 1
        elif analysisData.corona_score <= 0.029890:
            corona_count = 2
        else :
            corona_count = 3

        #혼잡도
        #A
        if analysisData.congestion_score < 0.425635:
            congestion_count = 1
            #B
        elif analysisData.congestion_score < 0.473350:
            congestion_count = 2
        else:
            congestion_count = 3

        count_result = {'corona_count':corona_count,
                        'congestion_count':congestion_count}

        content = {'tourData': tourData, 
        'analysisData':analysisData,
        'positiveWord':positiveWord,
        'negativeWord':negativeWord,
        'commonWord':commonWord,
        'count_result':count_result }

        return render(request, 'tour/detail.html',content )
    return HttpResponseRedirect('/tour/index.html')