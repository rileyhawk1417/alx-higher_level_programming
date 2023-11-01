let changed = false;
// Found this easier to use than writing a function within toggleClass
$(document).ready(function () {
  $("div#toggle_header").click(function () {
    $("div#toggle_header").toggleClass("red", changed);
    if ($("div#toggle_header").hasClass("green")) {
      $("div#toggle_header").removeClass("green");
      $("div#toggle_header").addClass("red");
      changed = true;
    } else {
      $("div#toggle_header").removeClass("red");
      $("div#toggle_header").addClass("green");
      changed = false;
    }
  });
});
