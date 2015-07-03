

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

if ( $('.billarea').length ) {

	setTimeout(function(){

		// move sidebar annotations into bootstrap column
		var sidebar = $('.annotations-list-uoc').detach();
		$('#submission').append(sidebar);

		// since right sidebar elements are absolute, right sidebar needs height or everything dissapears
		var billAreaHeight = $('.billarea').height();
		$('#submission').css('height',billAreaHeight + 'px');

		// init vars for annotation y pos calculations
		var basePos = $('.billarea').offset().top;
		var offset = 7; // about half of highlight height (this gets top of annotation to top of highlight)


		// TODO: Make sure annotations don't appear on top of each other!
		// annotation y pos calculations
		$('.annotator-wrapper .annotator-hl').each(function(){

			var highlightId = $(this).attr('data-annotation-id');
			var highlightPos = $(this).offset().top;
			var annotationSelector = '#submission #annotation-' + highlightId;
			var top = highlightPos - basePos - offset;
			// var annotationHeight = $(annotationSelector).height();

			$(annotationSelector).css('top', top + 'px');

		});

		/*
		// grab highlight positions

		// base position is top of document to .billarea since first annotation starts at .billarea
		var basePos = $('.billarea').offset().top;
		var offset = 7; // about half of highlight height (this gets top of annotation to top of highlight)
		var lastAnnotationBillAreaYPos = null;
		var newAnnotationBillAreaYPos = null;
		var topMargin = null;
		var distanceToBillArea = null;
		var distanceToTopOfLastAnnotation = null;

		// runs a little function on every highlight and sets every corresponding annotation to the same y position as its highlight 
		$('.annotator-wrapper .annotator-hl').each(function(){
			var highlightId = $(this).attr('data-annotation-id');
			var highlightPos = $(this).offset().top;
			var annotationSelector = '#submission #annotation-' + highlightId;
			var annotationHeight = $(annotationSelector).height();

			// first highlight's top margin is its highlight y position - base position, ie. distance from top of .billarea
			if (lastAnnotationBillAreaYPos == null) {

				distanceToBillArea = highlightPos - basePos - offset;
				marginTop = distanceToBillArea;
				$(annotationSelector).css('margin-top',distanceToBillArea + 'px');
				lastAnnotationBillAreaYPos = distanceToBillArea + annotationHeight;
				console.log('first run lastAnnotationBillAreaYPos: ' + lastAnnotationBillAreaYPos);
				console.log('');

			// all other highlights' top margins are distance from highlight y position to last highlight
			} else {

				distanceToBillArea = highlightPos - basePos;
				console.log('distanceToBillArea: ' + distanceToBillArea);
				console.log('starting lastAnnotationBillAreaYPos: ' + lastAnnotationBillAreaYPos);
				marginTop = distanceToBillArea - lastAnnotationBillAreaYPos - offset;
				$(annotationSelector).css('margin-top',marginTop + 'px');
				lastAnnotationBillAreaYPos = distanceToBillArea + annotationHeight;
				console.log('new lastAnnotationBillAreaYPos: ' + lastAnnotationBillAreaYPos);
				console.log('');

			}

		});

		*/

	},1000);

}