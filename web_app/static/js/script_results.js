$("#datepicker").datepicker({
    minDate: new Date(),
    beforeShowDay: function(date) {
        var day = date.getDay();
        return [day == 4 || day == 5 || day == 6];
    }
});

$("#pump-it").click(function() {
    var night_club = $("#clubs").val();
    var bartenders = $("#bartenders").val();
    var beers = $("#beers").val();
    var raw_date = $("#datepicker").val().split("/");
    var date = [raw_date[2], raw_date[0], raw_date[1]].join("-");

    var data = {
      "night_club": night_club,
      "bartenders": bartenders,
      "beers": beers,
      "date": date
    };

    $.ajax({
        type:"POST",
        url:"/pumped",
        data: JSON.stringify(data),
        contentType: 'application/json'
    });
});

