function saveCharacter(char_data, spells) {
  console.log(char_data);
  console.log(spells);
  var char_data_str = JSON.stringify(char_data);
  var spell_str     = JSON.stringify(spells);
  console.log(char_data_str);
  console.log(spell_str);
  var request = new XMLHttpRequest();
  var URL = "/save_character?char_data=" + encodeURI(char_data_str)+"&spell_data=" + encodeURI(spell_str);
  request.open("GET", URL);
  request.setRequestHeader("Content-Type",
                           "text/plain;charset=UTF-8");
  request.send();

  var success = $("#save_success_alert");
  console.log(success);

  success.alert();
}