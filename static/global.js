

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
	var annotations = [];
	var offset = 7; // about half of highlight height (this gets top of annotation to top of highlight)
	var basePos = $('.billarea').offset().top;


	function arrangeAnnotations() {

		console.log('arrange');

		// move sidebar annotations into bootstrap column
		var sidebar = $('.annotations-list-uoc').detach();
		$('#submission').append(sidebar);

		// give sidebar height (it's contents are absolute so it has none)
		var billAreaHeight = $('.billarea').height();
		$('#submission').css('height',billAreaHeight + 'px');

		// annotation y position calculations - makes sure annotations don't overlap
		$('.annotator-wrapper .annotator-hl').each(function(index){

			var highlight = $(this);
			// var highlightId = highlight.attr('data-annotation-id');
			var highlightId = highlight.attr('class').split(' ')[0].trim();

			// placeAnnotation(index, highlight, highlightId, true);

			var highlightPos = highlight.offset().top;
			var annotationSelector = '#submission #annotation-' + highlightId;
			var highlightTop = highlightPos - basePos - offset;
			var annotationHeight = $(annotationSelector).height();

			loadAnnotation(index,highlightId,highlightTop,annotationHeight);

		});

	}

	


	// this is a custom tweak to the annotator.js library.
	// it's called from /static/annotatorjs/src/view_annotator.js line 231 when an annotation is created 
	function placeNewAnnotation (newAnnotation) {

		// first grab the newest highlight
		var newHighlights = $('.undefined.annotator-hl');
		function compare(a,b) {
		  if ( parseInt($(a).attr('id')) < parseInt($(b).attr('id')))
		    return -1;
		  if ( parseInt($(a).attr('id')) > parseInt($(b).attr('id')))
		    return 1;
		  return 0;
		}
		newHighlights.sort(compare);
		var highlight = $(newHighlights[newHighlights.length - 1]);

		
		var highlightId = highlight.id;
		var index = $('li.annotator-marginviewer-element').length - 1;
		var highlightPos = highlight.offset().top;
		var annotationSelector = '#submission #annotation-' + highlightId;
		var highlightTop = highlightPos - basePos - offset;
		var annotationHeight = $(annotationSelector).height();
		var isCollision = false;
		var targetTop = highlightTop;
		var targetBot = highlightTop + annotationHeight;

		testAnnotationCollision();

		function testAnnotationCollision() {
			for (var i=0; i<annotations.length; i++) {

				if (!isCollision) {
					var testAnnotation = annotations[i];
					var testTop = testAnnotation.topY;
					var testBot = testAnnotation.botY;

					if ( (targetTop >= testTop) && (targetTop <= testBot) || (targetBot >= testTop) && (targetBot <= testBot) ) {
						
						isCollision = true;
						targetTop = testBot + 15;
						targetBot = targetTop + annotationHeight;

					}
				}

			}

			if (!isCollision) {
				
				annotationTop = targetTop;

			} else {
				
				isCollision = false;
				testAnnotationCollision();

			}
			
		}




		$('#submission #annotation-' + highlightId).css('top', annotationTop + 'px');
		
		annotations.push({
			id: highlightId,
			highlightY: highlightTop,
			annotationHeight: annotationHeight,
			topY: annotationTop,
			botY: annotationTop + annotationHeight
		});	
		

	}




	function loadAnnotation(index,highlightId,highlightTop,annotationHeight) {

		var annotationTop = null;

		if (index==0) {
				
			annotationTop = highlightTop + offset;	

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
				annotationTop = targetTop + offset;
			}

		}

		$('#submission #annotation-' + highlightId).css('top', annotationTop + 'px');

		annotations.push({
			id: highlightId,
			highlightY: highlightTop,
			annotationHeight: annotationHeight,
			topY: annotationTop,
			botY: annotationTop + annotationHeight
		});	

	}

}

	// this is a custom tweak to the annotator.js library.
	// it's called from /static/annotatorjs/src/view_annotator.js line 231 when an annotation is created 
	/*
	function placeNewAnnotation (newAnnotation) {

		// console.log(newAnnotation);

		var highlightId = newAnnotation.highlights[0].id;
		var highlights = $('.annotator-wrapper .annotator-hl');
		var index = $('li.annotator-marginviewer-element').length - 1;

		var allIdsSame = true;
		for (var i=0; i<highlights.length; i++) {
			var isIdSameAsNewOne = $(highlights[i]).attr('id') == highlightId;
			if (isIdSameAsNewOne == false) {
				allIdsSame = false;
			}
		}

		// if first new annotation since page load
		if (allIdsSame) {

			for (var i=0; i<highlights.length; i++) {
				if ( $(highlights[i]).attr('data-annotation-id') === undefined ) {
					
					var highlight = $(highlights[i]);
					// $('#submission #annotation-' + highlightId).css('border','1px solid red');

					placeAnnotation(index, highlight, highlightId);	

				}
			}

		// if second or later annotation since page load
		} else {
			
			var highlight = $('.annotator-wrapper #' + highlightId);
			// $('#submission #annotation-' + highlightId).css('border','1px solid red');

			placeAnnotation(index, highlight, highlightId);	

		}	

	}
	*/


	// fourth param (alreadyExisting)
	// 		- true for just loading already existing annotations (like on page load)
	//		- false for placing new annotations (like user just saved a new annotation)
	/*
	function placeAnnotation(index, highlight, highlightId, alreadyExisting){

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

			// just loading already existing annotations (like on page load)
			if (alreadyExisting) {

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

			// placing new annotations (like user just saved a new annotation)
			} else {

				var isCollision = false;
				var targetTop = highlightTop;
				var targetBot = highlightTop + annotationHeight;

				testAnnotationCollision();

				function testAnnotationCollision() {
					for (var i=0; i<annotations.length; i++) {

						if (!isCollision) {
							var testAnnotation = annotations[i];
							var testTop = testAnnotation.topY;
							var testBot = testAnnotation.botY;

							if ( (targetTop > testTop) && (targetTop < testBot) || (targetBot > testTop) && (targetBot < testBot) ) {
								
								isCollision = true;
								targetTop = testBot + 15;
								targetBot = targetTop + annotationHeight;

							}
						}

					}

					if (!isCollision) {
						
						annotationTop = targetTop;

					} else {
						
						// TODO: Fix infinite recursion bug in here somewhere.  Step through.
						isCollision = false;
						testAnnotationCollision();

					}
					
				}

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
	*/

