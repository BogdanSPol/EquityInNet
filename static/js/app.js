$(function() {
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    items: 3,
    stagePadding: 150,
    center: true,
    loop: true,
    margin: 20,
    dots: false,
    lazyLoad: true,
    lazyLoadEager: 5,
    autoplay: true,
    autoplayTimeout: 2500,
    autoplayHoverPause: true,
    autoplaySpeed: 500,
  });
});