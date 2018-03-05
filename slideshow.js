//
// slideshow.js
//
// Slideshow of pictures
//
// C. David Sherrill, March 2018
//

window.onerror = function (msg, url, lineNo, colunmNo, error) {
  var mainImage = document.getElementById("mainimage");
  var ermsg = msg;
  mainImage.innerHTML = ermsg;
  return false;
}

window.onload = updateMainImage;

var whichSlide = -1;

// var Slides = ["pics/pic1.jpg", "pics/pic2.jpg"]

// alert("Got this: " + Slides[0] + " " + Slides[1]);


function updateMainImage() {
  if (whichSlide == -1) {
    whichSlide = Math.floor(Math.random()*Slides.length);
  }
  else {
    whichSlide++;
  }
  if (whichSlide >= Slides.length) {
    whichSlide = 0;
  }
  var mainImage = document.getElementById("mainimage");
  mainImage.innerHTML = srcLine(Slides[whichSlide]);
  setTimeout(updateMainImage, 10000);
}

function srcLine(filename) {
  return '<img src="' + filename + '" />';
}


