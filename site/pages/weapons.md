---
skip_header: true
---

<script src="../js/nunjucks.js"></script>
<link rel="stylesheet" href="/site/css/two_sided_character_sheet.css">
<link rel="stylesheet" href="/site/css/weapons.css">

<div id="weapons_area">
</div>

<script>
  // Global character data dictionary (so we only have to hit the backend once.)
  var global_json = null;
  $.getJSON("/site/pages/GENERATED/ALT.json", function(json) {
    global_json = json;
    nunjucks.configure('/site/templates', {autoescape: true, web: {async:true}});
    console.log(json);
    nunjucks.render('weapons_page.html', 
                      { 
                        "data" : json["items"], 
                      }, function(err, content) {
                        if(err){
                          console.log(err);
                          return;
                        }
                        $( "#weapons_area" ).html( content );
                        return;
                      });

  })
</script>
