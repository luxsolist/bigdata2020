
var corona_count = "{{count_result.corona_count}}"
var congestion_count = "{{count_result.congestion_count}}"
jQuery(function($){
    for(var i=0; i<corona_count; i++){
        $(".corona").append('<img src="/static/tour/images/cough.png" id="cough_image">');
    }
    for(var i=0; i<congestion_count; i++){
        $(".congestion").append('<img src="/static/tour/images/car.png" id="car_image">');
    }
})


