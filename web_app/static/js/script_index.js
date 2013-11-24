$("#pump-it").click(function() {
    var night_club = $("#clubs").val();

    var data = {
      "night_club": night_club,
    };

    $.ajax({
        type:"POST",
        url:"/nightclub",
        data: JSON.stringify(data),
        contentType: 'application/json'
    });
});

