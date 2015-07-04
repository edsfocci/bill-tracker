

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




/* ------------------- setup annotation right sidebar --------------- */

if ( $('.billarea').length ) {

	// init vars for annotation y pos calculations
	var offset = 7; // about half of highlight height (this gets top of annotation to top of highlight)
	var annotations = [];
	var basePos = $('.billarea').offset().top;

	setTimeout(function(){

		// move sidebar annotations into bootstrap column
		var sidebar = $('.annotations-list-uoc').detach();
		$('#submission').append(sidebar);

		// give sidebar height (it's contents are absolute so it has none)
		var billAreaHeight = $('.billarea').height();
		$('#submission').css('height',billAreaHeight + 'px');

		// annotation y position calculations - makes sure annotations don't overlap
		$('.annotator-wrapper .annotator-hl').each(function(index){

			var highlight = $(this);
			var highlightId = highlight.attr('data-annotation-id');

			placeAnnotation(index, highlight, highlightId);

		});

	},1000);




	// this is a custom tweak to the annotator.js library.
	// it's called from /static/annotatorjs/src/view_annotator.js line 231 when an annotation is created 
	function placeNewAnnotation (newAnnotation) {

		var index = $('.annotator-wrapper .annotator-hl').length + 1;
		var highlightId = newAnnotation.highlights[0].id;
		var highlight = $('.annotator-wrapper #' + highlightId);

		var highlightSelector = '#' + highlightId;

		setTimeout(function(){
			$(highlightSelector).css('border','1px solid #ff0000');
		},2500);

		// placeAnnotation(index, highlight, highlightId);		

	}



	function placeAnnotation(index, highlight, highlightId){

		// prevents duplicate id entries (where highlight is broken into two with same id)
		if ( annotations.length && (annotations[index - 1].id == highlightId) ) {
			return;
		}

		var highlightPos = highlight.offset().top;
		var annotationSelector = '#submission #annotation-' + highlightId;
		var highlightTop = highlightPos - basePos - offset;
		var annotationHeight = $(annotationSelector).height();

		var annotationTop = null;

		if (index==0) {
				
			annotationTop = highlightTop;					

		} else {

			var prevIndex = index - 1;
			var prevAnnotation = annotations[prevIndex];
			var targetTop = highlightTop;
			var targetBot = highlightTop + annotationHeight;
			var prevTop = prevAnnotation.topY;
			var prevBot = prevAnnotation.botY;

			if ( (targetTop > prevTop) && (targetTop < prevBot) || (targetBot > prevTop) && (targetBot < prevBot) ) {
				annotationTop = prevBot + 15;
			} else {
				annotationTop = targetTop;
			}

		}

		annotations.push({
			id: highlightId,
			highlightY: highlightTop,
			annotationHeight: annotationHeight,
			topY: annotationTop,
			botY: annotationTop + annotationHeight
		});	

		$('#submission #annotation-' + highlightId).css('top', annotationTop + 'px');

	}

}