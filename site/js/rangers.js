// Used to fake get requests.
function parseGetRequest() {
    var queryString = window.location.search.substring(1)
    var query = {};
    var pairs = (queryString[0] === '?' ? queryString.substr(1) : queryString).split('&');
    for (var i = 0; i < pairs.length; i++) {
        var pair = pairs[i].split('=');
        key = decodeURIComponent(pair[0]).replace(/"/g, '').replace(/-/g, ' ').replace(/_/g, ' ');
        val = decodeURIComponent(pair[1] || '').replace(/"/g, '').replace(/-/g, ' ').replace(/_/g, ' ');
        query[key] = val;
    }
    return query;
}

//Returns null on failure
function getRaceFromSubrace(base, subrace){
    var rnr_race = null;
    for(r in base["races"] ){
      if(Object.keys(base["races"][r]["subraces"]).includes(subrace)){
        rnr_race = r;
        break;
      }
    }
    return rnr_race;
}

//Returns null on failure
function getClassFromSubclass(base, subclass){
    var rnr_class = null;
    for(c in base["classes"] ){
      if(Object.keys(base["classes"][c]["subclasses"]).includes(subclass)){
        rnr_class = c;
        break;
      }
    }
    return rnr_class;
}

// Takes the user back.
function goBack() {
  window.history.back();
}
