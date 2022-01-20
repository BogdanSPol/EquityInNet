/* Carousel */
$(function() {
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    items: 5,
    autoWidth: true,
    stagePadding: 10,
    center: true,
    loop: true,
    margin: 5,
    dots: false,
    lazyLoad: true,
    lazyLoadEager: 2,
    autoplay: true,
    autoplayTimeout: 2500,
    autoplayHoverPause: true,
    autoplaySpeed: 500,
  });
});

/* Range sliders */
$(document).ready(function(){
  $("#min_invest").ionRangeSlider({skin:"round",type:"double",grid:!0,min:0,max:1e3,from:100,to:750,postfix:" €"});
  $("#raised").ionRangeSlider({skin:"round",type:"double",grid:!0,min:0,max:1e2,from:25,to:90,postfix:" %"});
  $("#days_to_go").ionRangeSlider({skin:"round",type:"double",grid:!0,min:0,max:30,from:0,to:30});
  $("#score").ionRangeSlider({skin:"round",type:"double",grid:!0,min:0,max:10,from:0,to:10})
});