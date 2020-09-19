---
skip_header: true
---
<script src="../js/nunjucks.js"></script>
<html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link rel="stylesheet" href="/site/css/iterated_char_sheet.css">
      <link rel="stylesheet" href="/site/css/two_sided_character_sheet.css">
      <link href="https://fonts.googleapis.com/css?family=Cinzel+Decorative" rel="stylesheet">
      <link href='https://fonts.googleapis.com/css?family=Angkor' rel='stylesheet'>
  </head>
  <body>
    <div id="selection_area" class="selection_area">
    </div>
    <div class="noprint">
      <h4>Character Sheet Preview</h4>
      <p>
        Scales differently when printing.
      </p>
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
  $.getJSON("/site/pages/GENERATED/ALT.json", function(json) {
    global_json = json;
    nunjucks.configure('/site/templates', {autoescape: true });
    starting_values = parseGetRequest();
    var content = nunjucks.render('character_selection_template.html', {
                                                                        "chosen_race" : starting_values["race"],
                                                                        "chosen_class": starting_values["class"],
                                                                        "race_names"  : json["race_names"],
                                                                        "class_names" : json["class_names"]
                                                                      } );
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
    $("#front-character-name").text(name);
    $("#back-character-name").text(name);

    if(name == ""){
      $("#levelUpSheetCharacterName").text($( "#chosen_class" ).val() + " Level Up Sheet");
    }else{
      $("#levelUpSheetCharacterName").text(name + "'s Level Up Sheet");
    }
  }

  // merges new_dict into base
  function mergeAbilities(base, new_dict){
    for(ability_type in new_dict){
      // Add the ability type to data if it doesn't exist yet.
      if(!(ability_type in base)){
        base[ability_type] = {};
      }
      // Add every ability for the ability type to our data objects
      for(ability in new_dict[ability_type]){
        base[ability_type][ability] = new_dict[ability_type][ability];
      }
    }
    return base;
  }

  // combines new_dict's stats into base
  function mergeStats(base, new_dict){
    for(stat in new_dict){
      base[stat] += new_dict[stat]
    }
    return base;
  }

  // Grab the name, race, class and other data for this character and render a sheet.
  function updateCharacterSheet(){
    if(global_json == null){
      console.log("ERROR: json not loaded.");
      return;
    }

    var name = $( "#chosen_name" ).val();
    var level_str    = $( "#chosen_level" ).val();
    var level        = parseInt(level_str, 10);
    var rnr_subrace  = $( "#chosen_race" ).val();
    var rnr_subclass     = $( "#chosen_class" ).val();
    var sheet_type   = $( "#sheet_type" ).val();
    var rnr_race  = getRaceFromSubrace(global_json, rnr_subrace);
    var rnr_class = getClassFromSubclass(global_json, rnr_subclass);
    if(rnr_race === null){
      console.log("Error, race not found for " + rnr_subrace);
      return;
    }

    //Deep copy the data.
    var race_data  = JSON.parse(JSON.stringify(global_json["races"][rnr_race]["subraces"][rnr_subrace]));
    var class_data = JSON.parse(JSON.stringify(global_json["classes"][rnr_class]["subclasses"][rnr_subclass]));

    data = {}
    data["race"] = rnr_race;
    data["subrace"] = rnr_subrace;
    data["class"] = rnr_class;
    data["subclass"] = rnr_subclass;
    data["name"] = name;
    data["stats"] = class_data["base_stats"];
    data["abilities"] = mergeAbilities(race_data["abilities"], class_data["base_abilities"]);
    data["icons"] = class_data["icons"];


    for(i = 0; i <= level; i++){
      // Create the string representation of the level.
      var tmp_lvl_str = "level_" + i;
      // Make sure that the level is valid.
      if(!(tmp_lvl_str in class_data["levels"])){
        console.log("ERROR: Could not find level " + tmp_lvl_str + " for " + rnr_race + " " + rnr_class);
        continue;
      }
      data["abilities"] = mergeAbilities(data["abilities"], class_data["levels"][tmp_lvl_str]["abilities"]);
    }

    var character_sheet = "ERROR: Sheet did not render.";
    data["character_name"] = name;
    tmp_icons = {};
    tmp_icons["health"] = data["icons"][0][0];
    tmp_icons["action_points"] = data["icons"][1][0];
    tmp_icons["spell_power"] = data["icons"][2][0];
    tmp_icons["armor"] = data["icons"][3][0];
    tmp_icons["special"] = data["icons"][4][0];
    tmp_icons["copper"] = "token.svg"
    tmp_icons["silver"] = "two-coins.svg"
    tmp_icons["gold"] = "swap-bag.svg"
    tmp_icons["platinum"] = "shiny-purse.svg"
    tmp_icons["level"] = data["icons"][5][0];
    tmp_icons["luck"] = "horseshoe.svg";
    tmp_icons["health_dice"] = "heart-plus.svg";

    data["tmp_icons"] = tmp_icons;
    console.log(tmp_icons);
    if(sheet_type == "v1_visual"){
      data["visualStats"] = true;
      character_sheet = nunjucks.render('character_sheet_template.html', data );
    } else if(sheet_type == "v2"){
      character_sheet = nunjucks.render('two_sided_character_sheet.html', data );
    }
    else{
      console.log("in else with " + sheet_type)
      character_sheet = nunjucks.render('updated_character_sheet.html', data );
      //character_sheet = nunjucks.render('character_sheet_template.html', data );
    }
    $( "#character_sheet_area" ).html( character_sheet );


    var name_text =  name != "" ? name : rnr_subclass;
    level_up_sheet = nunjucks.render('level_up_sheet_template.html', {"levels" : class_data["levels"], "name" : name_text});
    $("#level_up_sheet_area").html(level_up_sheet);
  }

</script>

