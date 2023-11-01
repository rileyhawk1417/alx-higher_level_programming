url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(url, function (data, success) {
  if (success) {
    for (i in data.results) {
      $("UL.list_movies").append(`<li>${data.results[i].title}</li>`);
    }
  } else {
    console.log("Err");
  }
});
