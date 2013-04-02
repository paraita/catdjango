$("#bouton_valider").button();
$('#prochain_indice').popover();
$("#prochain_indice").hide();
$("#bouton_valider").click(function() {
	var reponse = $("#text_reponse").val();
	if (reponse.toLowerCase() == "{{enigme.reponse}}".toLowerCase()) {
		alert("BRAVO !");
		$("#prochain_indice").css('visibility', 'visible');
		$('#prochain_indice').fadeIn();
	} else {
		alert("FAUX, réfléchis !");
	}
});