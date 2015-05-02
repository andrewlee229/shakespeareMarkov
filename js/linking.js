function submitSelection(){
	play_input = "Macbeth";
	persona_input = "Macbeth";
	//play_input = document.getElementById("play").value
	//persona_input = document.getElementById("persona").value,
	$.post("/process", {play: play_input, persona: persona_input})
	.done(function(data){
		console.log(data);
		//need to ask what proper way to pass to html is
		document.getElementById("generatedText").innerHTML = data;
	});
}