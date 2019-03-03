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
  var canvas = document.getElementById("mainimage");
  var context = canvas.getContext("2d");
  var theImage = new Image();
  theImage.src = Slides[whichSlide];
  theImage.onload = function() {
    context.fillStyle = "white";
    context.fillRect(0,0,canvas.width,canvas.height);
    var nw = theImage.naturalWidth;
    var nh = theImage.naturalHeight;
    var sw = nw / canvas.width;
    var sh = nh / canvas.height;
    if (sw >= sh) {
      fw = canvas.width;
      fh = Math.floor(nh / sw);
      context.drawImage(theImage,0,(canvas.height-fh)/2,fw,fh); 
    }
    else {
      fh = canvas.height;
      fw = Math.floor(nw / sh);
      context.drawImage(theImage,(canvas.width-fw)/2,0,fw,fh); 
    }
  };
  setTimeout(updateMainImage, 10000);
}



