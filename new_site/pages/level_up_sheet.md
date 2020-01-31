---
skip_header: true
---

<script src="../js/nunjucks.js"></script>
<link rel="stylesheet" href="/new_site/css/iterated_char_sheet.css">

<div id="selection_area">
</div>
<hr>
<div id="level_up_sheet_area">
</div>
  

<script>
  // Global character data dictionary (so we only have to hit the backend once.)
  var global_json = null;
  $.getJSON("/new_site/pages/GENERATED/ALT.json", function(json) {
    global_json = json;
    nunjucks.configure('/new_site/templates', {autoescape: true, web: {async:true}});
    starting_values = parseGetRequest();
    console.log(starting_values["class"]);
    nunjucks.render('selector_template.html', 
                      { 
                        "data" : json["class_names"], 
                        "id" : "chosen_class", 
                        "chosen" : starting_values["class"]
                      }, function(err,content) {
                        if(err){
                          console.log(err);
                          return;
                        }
                        $( "#selection_area" ).html( content );
                        $('select').selectpicker();
                        selectButtonUpdateHandler();
                        return;
                      });

  })

  function selectButtonUpdateHandler(){
    console.log("inside.");
    var subclass = $( "#chosen_class" ).val();
    console.log(subclass);
    var rnr_class = getClassFromSubclass(global_json, subclass);
    var class_data = JSON.parse(JSON.stringify(global_json["classes"][rnr_class]["subclasses"][subclass]));
    nunjucks.render('level_up_sheet_template.html', 
                    {
                      "levels" : class_data["levels"], 
                      "name" : subclass
                    }, function(err, content){
                      $("#level_up_sheet_area").html(content);
                    });
  }




</script>
