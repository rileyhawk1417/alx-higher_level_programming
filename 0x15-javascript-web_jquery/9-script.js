url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
$.get(url, function (data, success) {
  if (success) {
    for (i in data.results) {
      $("div#hello").text(data);
    }
  } else {
    console.log("Err");
  }
});
