$("#clubs").on("autocompletechange", function() {
    var club = $("#clubs").val();
    $.ajax({
        type:"GET",
        url:"/clubs",
        data:{name: club},
        success: function(data) {
            $('#bartenders').empty();
            data.bartenders.forEach(function(o) {
                $('#bartenders').append("<option value='" + o + "'> " + o + " </option>");
            });
            $('#bartenders').attr("size", data.bartenders.length);
            $('#bartenders').attr("style", "display:block;");
        }
    });
});
