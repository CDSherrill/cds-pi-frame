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

// var Slides = ["pics/pic1.jpg", "pics/pic2.jpg"]
// alert("Got this: " + Slides[0] + " " + Slides[1]);


var whichSlide;
// get the last slide number from localStorage
var lastSlide = localStorage.getItem('slideshow_lastslide');
if (lastSlide == null) {
  whichSlide = Math.floor(Math.random()*Slides.length)-1;
}
else {
  whichSlide = parseInt(lastSlide);
}

function updateMainImage() {
  whichSlide++;
  if (whichSlide >= Slides.length) {
    whichSlide = 0;
  }
  var canvas = document.getElementById("mainimage");
  var context = canvas.getContext("2d");
  var theImage = new Image();
  theImage.src = Slides[whichSlide];
  theImage.onload = function() {
    context.fillStyle = "black";
    context.fillRect(0,0,canvas.width,canvas.height);
    var nw = theImage.naturalWidth;
    var nh = theImage.naturalHeight;
    var cw = canvas.width;
    var ch = canvas.height;
    var sw = nw / cw;
    var sh = nh / ch;
    if (nh <= ch && nw <= cw) {
      context.drawImage(theImage,(cw-nw)/2,(ch-nh)/2,nw,nh);
    }
    else { // need to scale something to fit
      if (sw >= sh) {
        fw = canvas.width;
        fh = Math.floor(nh / sw);
        context.drawImage(theImage,0,(ch-fh)/2,fw,fh); 
      }
      else {
        fh = canvas.height;
        fw = Math.floor(nw / sh);
        context.drawImage(theImage,(cw-fw)/2,0,fw,fh); 
      }
    }
  };
  setTimeout(updateMainImage, 10000);
  localStorage.setItem("slideshow_lastslide", whichSlide);
}



