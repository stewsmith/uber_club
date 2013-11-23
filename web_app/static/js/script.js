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
