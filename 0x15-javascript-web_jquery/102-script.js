$(document).ready(function () {
  $("#btn_translate").click(function () {
    console.log("clicked");
    url = `https://hellosalut.stefanbohacek.dev/?lang=${
      $("#language_code").val()
    }`;
    $.get(url, function (data, success) {
      if (success) {
        $("div#hello").text(data.hello);
      } else {
        console.log("Err");
      }
    });
  });
});
