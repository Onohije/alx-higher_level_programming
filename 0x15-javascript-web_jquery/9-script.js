// Queries an API for wind speed in SF and replaces the text of the
// div#sf_wind_speed tag with the speed

$('document').ready(function () {
  const view = $('div#hello');
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      view.text(data.hello);
    }
  });
});
