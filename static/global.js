

/* -------------- nav click functionality ------------------- */

$('.navbar-collapse a').click(function(e){
	
	var clickedLink = $(this);
	var clickedLi = clickedLink.parent();
	var lis = $('.navbar-collapse li');

	var searchTerm = clickedLink.text().toLowerCase();
	console.log('run ajax for ' + searchTerm + ' here.');
	lis.removeClass('active');
	clickedLi.addClass('active');

	e.preventDefault();

    switch (searchTerm) {
        case "content": window.location = "/bills";
             break;
        case "subject": window.location = "/subjects";
             break;
        case "author": window.location = "/authors";
             break;
        default: break;
    }


});







/* -------------- search functionality ------------------- */







/* -------------- single bill view functionality ------------------- */

var lastClicked;

function toggleForm(sentence)
{
	var submissionForm = document.getElementById("submission");

	if (submissionForm.style.visibility != "visible")
	{
		submissionForm.style.visibility = "visible";
		sentence.style.backgroundColor = "yellow";
		lastClicked = sentence;
	}
	else
	{
		submissionForm.style.visibility = "hidden";
		lastClicked.style.backgroundColor = "inherit";
	}
}

function submitAnnotation(text)
{
	var annotationText = text.value;
	var submissionForm = document.getElementById("submission");

	submissionForm.style.visibility = "hidden";
	lastClicked.style.backgroundColor = "inherit";
	alert(annotationText + " submitted as annotation for sentence " + lastClicked.id + ".");
	text.value = "";

}




/* ------------ move annotation sidebar to bootstrap column  --------------- */

setTimeout(function(){

	// move sidebar annotations into bootstrap column
	var sidebar = $('.annotations-list-uoc').detach();
	$('#submission').append(sidebar);

	// grab highlight positions

	var basePos = $('.billarea').offset().top;
	console.log('basePos: ' + basePos);

	$('.annotator-wrapper .annotator-hl').each(function(){
		var highlightId = $(this).attr('data-annotation-id');
		var highlightPos = $(this).offset().top;
		var diffPos = highlightPos - basePos;

		console.log('data-' + highlightId + ': ' + highlightPos);

		// console.log('diff: ' + diffPos);

		// $('#submission #annotation-' + highlightId).css('margin-top',diffPos + 'px');

		// var annotationId = $(this).attr('data-annotation-id').val();
		// console.log(annotationId);
	});

},4000);