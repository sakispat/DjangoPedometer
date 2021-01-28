$(function(){
    var $steps = $("#steps");
    var ctx = $steps[0].getContext("2d");
  	$.ajax({
    	url: $steps.data("url"),
    	success: function (data) {
          	new Chart(ctx, {
            	type: 'bar',
           	 	data: {
              		labels: data.days,
              		datasets: [{
                		label: 'Steps',
                		backgroundColor: 'blue',
                		data: data.steps
              		}]          
            	},
            	options: {
              		responsive: true,
              		legend: { position: 'top', },
              		title: {
                		display: true,
                		text: 'Steps Bar Chart'
              		}
            	}
          	});
    	}
  	});
});

$('#form').on('submit', function(e){
	e.preventDefault();
  	$.ajax({
       	type : "POST", 
       	url: "ajax-chart/", 
       	data: {
            datefrom : $('#datefrom').val(),
            dateto : $('#dateto').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            dataType: "json",
        },   
        success: function(data){
        	var steps = [];
        	steps.push(data.steps);
        	
        	var labels = data.days;

        	renderChart(steps, labels);


            $('#output').html(data.msg);
        },
        failure: function(){}
   	});
});

function renderChart(steps, days) {
	var $steps = $("#steps");
	var ctx = $steps[0].getContext("2d");
  	var myChart = new Chart(ctx, {
    	type: 'bar',
   	 	data: {
      		labels: days,
      		datasets: [{
        		label: 'Steps',
        		backgroundColor: 'blue',
        		data: steps[0]
      		}]          
    	},
    	options: {
      		responsive: true,
      		legend: { position: 'top', },
      		title: {
        		display: true,
        		text: 'Steps Bar Chart'
      		}
    	}
  	});
}
