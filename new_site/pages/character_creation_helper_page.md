---
skip_header: true
---

<script src="../js/nunjucks.js"></script>

<div id="selection_area">
</div>
<hr>
<div id="class_area">
</div>
  

<script>
  // Global character data dictionary (so we only have to hit the backend once.)
  var global_json = null;
  $.getJSON("/new_site/pages/GENERATED/ALT.json", function(json) {
    global_json = json;
    nunjucks.configure('/new_site/templates', {autoescape: true });
    var content = nunjucks.render('character_creation_helper_template.html', { "data" : json["roles"]["class_roles"] } );
    $( "#class_area" ).html( content );
    var content = nunjucks.render('role_selection_template.html', json["roles"]);
    $( "#selection_area" ).html( content );
    $('[data-toggle="tooltip"]').tooltip({
        trigger : 'hover',
        delay: { "show": 500}
    });
    updateRoles();
  })

  function toggleButton(button){
    if($(button).hasClass("btn-primary")){
      $(button).addClass('btn-secondary').removeClass('btn-primary');
    } else{
      $(button).addClass('btn-primary').removeClass('btn-secondary');
    }
    updateRoles();
  }

  function updateRoles(){    
    var selected_roles = new Array();

    $('.btn-primary').each( function( ) {
      selected_roles.push($(this).data("role"));
    });

    console.log(selected_roles);

    $(".rnr_class").each( function(){
      let roles = $(this).data("roles").trim().split(" ");
      let all_roles = true;
      for(index in selected_roles){
        role = selected_roles[index];
        if(!roles.includes(role)){
          all_roles = false;
          break;
        }
      }
      if(all_roles){
        $(this).show();
      } else{
        $(this).hide();
      }
    });
  }
</script>

