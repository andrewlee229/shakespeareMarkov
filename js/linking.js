var arr = ["A Midsummer Night's Dream", "Hamlet", "King John", "Macbeth", "Richard II", "Richard III", "Troilus and Cressida"];

$(document).ready(function(){
	for(i = 0; i < arr.length; i++){
		$("#plays").append('<option value="'+ arr[i] +'">'+ arr[i] +'</option>');
	}
	$('#plays').on('change', function() {
		var play_input = $(this).val();
		$.post("/get_personas", {play: play_input})
		.done(function(data){
			$("#personas").empty();
			$("#personas").append('<option value="">Select Persona</option>');
			var data = JSON.parse(data);
			for(i = 0; i < data.length; i++){
				var persona = data[i].toLowerCase().split(" ");
				if(persona.length > 1){
					persona = persona[0].charAt(0).toUpperCase() + persona[0].slice(1) + " " + persona[1].charAt(0).toUpperCase() + persona[1].slice(1);
				}
				else{
					persona = persona[0].charAt(0).toUpperCase() + persona[0].slice(1)
				}
				$("#personas").append('<option value="'+ data[i] +'">'+ persona +'</option>');
				
			}
		});
	});
});


function submitSelection(){
	play_input = document.getElementById("plays").value;
	persona_input = document.getElementById("personas").value;
	$.post("/generate_markov", {play: play_input, persona: persona_input})
	.done(function(data){
		console.log(data);
		document.getElementById("generatedText").innerHTML = persona_input + ".   " + data;
	});
}