function fetchGreeting() {
  url = `https://hellosalut.stefanbohacek.dev/?lang=${
    $("#language_code").val()
  }`;
  $.get(url, function (data, success) {
    if (success) {
      console.log(data);
      $("div#hello").text(data.hello);
    } else {
      console.log("Err");
    }
  });
}

$(document).ready(function () {
  $("#btn_translate").click(fetchGreeting);
  $(document).on("keydown", function (event) {
    if (event.key === "Enter") {
      fetchGreeting();
    }
  });
});
