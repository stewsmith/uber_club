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
        contentType: 'application/json',
        success: function(data) {
          console.log(data);
          $('#bartendersandbeers').hide();

          $('#num_drinkers').text("Predicted number of drinkers: " + data.num_drinkers_on_date);
          $('#recommended_cover_fee').text("Recommended Cover Fee: $" + data.recommended_cover_fee);
          $('#MFratio').text("Male to Female Ratio: " + data.MF_ratio);
          var bartenders = data.top_three_bartenders;
          $('#top3bartenders').text("Top 3 bartenders: " + bartenders);
          var beers = data.bottom_three_beers;
          $('#bottom3beers').text("Beers to put on special: " + beers);
          $('#avgage').text("Average age of drinkers:  " + data.avg_age_on_date);
          $('#avgcoverfeerevenue').text("Cover fee revenue: $" + data.avg_cover_fee_revenue);
          $('#results').show();
        }
    });
});

