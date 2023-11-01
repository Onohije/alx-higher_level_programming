// This code waits for the HTML document to be fully loaded then 
// changes the text color of the first header element to red.

document.addEventListener('DOMContentLoaded', function () {
  const header = document.getElementsByTagName('header');
  header[0].style.color = '#FF0000';
});
