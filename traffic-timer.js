//
// traffic-timer.js
//
// Set the timer for how long before we switch over to the traffic map
// Right now, we assume we're coming in from the weather map
//
// C. David Sherrill, June 2019
//

var dt = new Date();
var hours = dt.getHours(); // 0-23 military format
var mins = dt.getMinutes();
var fracHour = hours + (mins / 60.0);

// alert("Time is " + fracHour.toString() + " hours");

// how many times do we do the weather before we do the traffic?
var trafficEvery = 0;

if (fracHour > 7.5 && fracHour < 9.5) {
    trafficEvery = 1;
}
else {
    trafficEvery = 12;
}

var iter = 0;

var weatherCount = localStorage.getItem("weatherCount");
if (weatherCount == null) {
  iter = 0;
}
else {
  iter = parseInt(weatherCount);
}

var secsToRedirect = 10;

if ((iter % trafficEvery) == 0) {
  setTimeout(function(){window.location.href='trafficmap.html'},secsToRedirect*1000);
}
else {
  setTimeout(function(){window.location.href='canvas.html'},secsToRedirect*1000);
}

if (iter > 1000) {
  localStorage.setItem("weatherCount", 0);
}
else {
  localStorage.setItem("weatherCount", (iter+1));
}




