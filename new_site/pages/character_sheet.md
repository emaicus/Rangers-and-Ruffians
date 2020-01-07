---
skip_header: true
---

<script src="../js/nunjucks.js"></script>
<html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="/new_site/css/iterated_char_sheet.css">
      <link href="https://fonts.googleapis.com/css?family=Cinzel+Decorative" rel="stylesheet">
      <link href='https://fonts.googleapis.com/css?family=Angkor' rel='stylesheet'>
  </head>
  <body>
    <div id="selection_area" class="selection_area">
    </div>
    <div id="character_sheet_area">
    </div>
    <div id="level_up_sheet_area">
    </div>
  </body>
</html>

<script>

  // Global character data dictionary (so we only have to hit the backend once.)
  var global_json = null;
  $.getJSON("/data/GENERATED/all_data.json", function(json) {
    global_json = json;
    nunjucks.configure('/new_site/templates', {autoescape: true });
    var content = nunjucks.render('character_selection_template.html', json );
    $( "#selection_area" ).html( content );
  
    $(function () {
        $('select').selectpicker();
    });


    updateCharacterSheet();
  })

  // Dynamically  change the character name on the sheet when the user types.
  function updateCharacterName(){
    var name = $( "#chosen_name" ).val();
    $("#characterName").text(name);
  }


  // Grab the name, race, class and other data for this character and render a sheet.
  function updateCharacterSheet(){
    if(global_json == null){
      console.log("ERROR: json not loaded.");
      return;
    }

    var name = $( "#chosen_name" ).val();
    var level_str = $( "#chosen_level" ).val();
    var level     = parseInt(level_str, 10);
    var rnr_race  = $( "#chosen_race" ).val();
    var rnr_class = $( "#chosen_class" ).val();
    var sheet_type= $( "#sheet_type" ).val();

    //Deep copy the character.
    var data = JSON.parse(JSON.stringify(global_json["characters"][rnr_race][rnr_class]));
    data["name"] = name;
    data["abilities"] = data["base_abilities"];


    for(i = 1; i <= level; i++){
      // Create the string representation of the level.
      var tmp_lvl_str = "level_" + i;
      // Make sure that the level is valid.
      if(!(tmp_lvl_str in data["levels"])){
        console.log("ERROR: Could not find level " + tmp_lvl_str + " for " + rnr_race + " " + rnr_class);
        continue;
      }
      console.log(tmp_lvl_str);
      // For every ability type in the current level
      for(ability_type in data["levels"][tmp_lvl_str]["abilities"]){
        // Add the ability type to data if it doesn't exist yet.
        if(!(ability_type in data["abilities"])){
          data["abilities"][ability_type] = {};
        }
        // Add every ability for the ability type to our data objects
        for(ability in data["levels"][tmp_lvl_str]["abilities"][ability_type]){
          data["abilities"][ability_type][ability] = data["levels"][tmp_lvl_str]["abilities"][ability_type][ability];
        }
      }
    }

    var character_sheet = "ERROR: Sheet did not render.";

    console.log(sheet_type);
    if(sheet_type == "v1_visual"){
      data["visualStats"] = true;
      character_sheet = nunjucks.render('character_sheet_template.html', data );
    } else{
      character_sheet = nunjucks.render('character_sheet_template.html', data );
    }
    $( "#character_sheet_area" ).html( character_sheet );
  }
</script>

