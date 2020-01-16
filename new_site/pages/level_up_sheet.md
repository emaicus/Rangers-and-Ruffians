---
skip_header: true
---

<script src="../js/rangers.js"></script>
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
  $.getJSON("/data/GENERATED/ALT.json", function(json) {
    global_json = json;
    nunjucks.configure('/new_site/templates', {autoescape: true });
    starting_values = parseGetRequest();
    console.log(starting_values["class"]);
    var content = nunjucks.render('selector_template.html', 
                                  { 
                                    "data" : json["class_names"], 
                                    "id" : "chosen_class", 
                                    "chosen" : starting_values["class"]
                                  } );
    $( "#selection_area" ).html( content );
    $('select').selectpicker();

    
    selectButtonUpdateHandler();
  })

  function selectButtonUpdateHandler(){
    var subclass = $( "#chosen_class" ).val();
    var rnr_class = getClassFromSubclass(global_json, subclass);
    var class_data = JSON.parse(JSON.stringify(global_json["classes"][rnr_class]["subclasses"][subclass]));
    var level_up_sheet = nunjucks.render('level_up_sheet_template.html', 
                                          {
                                            "levels" : class_data["levels"], 
                                            "name" : subclass
                                          });
    $("#level_up_sheet_area").html(level_up_sheet);
  }




</script>
