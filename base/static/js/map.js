$(document).ready(function () {
  var initMarkerCoords = null;
  var map = L.map('map').setView([-27.332449, -55.864679], 13);
  var marker = null;
  if (LAT && LNG) {
    initMarkerCoords = [parseFloat(LAT), parseFloat(LNG)];
    marker = L.marker().setLatLng(initMarkerCoords).addTo(map);
  }
  //
  function initMap() {
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap'
    }).addTo(map);
  }
  //
  initMap();
});