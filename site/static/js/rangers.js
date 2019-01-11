// $.backstretch("/static/images/city_by_the_shore.jpg");
  // var instance = M.Tabs.init(el, options);



$(document).ready(function(){
  $('.tabs').tabs();
});

$(document).ready(function(){
  $('.collapsible').collapsible();
});

// function printdiv(elem)
// {
//     var mywindow = window.open('', 'PRINT', 'height=800,width=600');
//     mywindow.document.write('<html><head>');
//     mywindow.document.write('  <link rel="stylesheet" href="/static/css/character_sheet.css" type="text/css" />');
//     mywindow.document.write('</head><body>');
//     mywindow.document.write(document.getElementById(elem).innerHTML);
//     mywindow.document.write('</body></html>');

//     mywindow.document.close(); // necessary for IE >= 10
//     mywindow.focus(); // necessary for IE >= 10*/

//     mywindow.print();
//     mywindow.close();

//     return true;
// }

function printdiv(divName) {
  var printContents = document.getElementById(divName).innerHTML;
  var originalContents = document.body.innerHTML;

  document.body.innerHTML = printContents;

  window.print();

  document.body.innerHTML = originalContents;
}