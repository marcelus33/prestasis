$(document).ready(function () {
  var map = L.map('map').setView([-27.332449, -55.864679], 13);
  var marker = L.marker();
  var latInput = $('#id_latitud_ubicacion');
  var lngInput = $('#id_longitud_ubicacion');
  //
  if (LAT && LNG) {
    latInput.val(LAT);
    lngInput.val(LNG);
    marker.setLatLng([LAT, LNG]).addTo(map);
  }
  //
  function initMap() {
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap'
    }).addTo(map);
  }
  //
  function onMapClick(e) {
    var lat = e.latlng.lat;
    var lng = e.latlng.lng;
    latInput.val(lat);
    lngInput.val(lng);
    marker.setLatLng(e.latlng).addTo(map);
  }
  //
  initMap();
  map.on('click', onMapClick);
});