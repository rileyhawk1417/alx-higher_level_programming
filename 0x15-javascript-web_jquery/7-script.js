url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
$.get(url, function (data, success) {
  if (success) {
    $("div#character").text(data.name);
  } else {
    console.log("Err fetching the data");
  }
});
