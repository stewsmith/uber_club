$("#clubs").on("autocompletechange", function() {
    var club = $("#clubs").val();
    $.ajax({
        type:"GET",
        url:"/clubs",
        data:{name: club},
        success: function(data) {
            //Get bartenders
            $('#bartenders').empty();
            data.bartenders.forEach(function(o) {
                $('#bartenders').append("<option value='" + o + "'> " + o + " </option>");
            });
            $('#bartenders').attr("size", data.bartenders.length);
            $('#bartenders_div').attr("style", "display:block;");

            //Get beers
            $('#beers').empty();
            data.beers.forEach(function(o) {
                $('#beers').append("<option value='" + o + "'> " + o + " </option>");
            });
            $('#beers').attr("size", data.beers.length);
            $('#beers_div').attr("style", "display:block;");
        }
    });
});

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
    $.ajax({
        type:"POST",
        url:"/pumped",
        data:{
            night_club: night_club,
            date: date,
            bartenders: bartenders,
            beers: beers
        }
    });
});

