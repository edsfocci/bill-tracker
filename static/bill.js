// var selected;

window.onload = function() {
  // $("span").each(function() {
  //   $(this).click(function() {
  //     if (selected) {
  //       $(selected).toggleClass("selected-sentence");
  //       $(this).toggleClass("selected-sentence");
  //       selected = this;
  //     } else {
  //       $(this).toggleClass("selected-sentence");
  //       selected = this;
  //     }
  //   });
  // });

  // $("center").each(function(){
  //   $(this).replaceWith('<div style="text-align:center;">' + $(this).html() +
  //     '</div>');
  // });

  var csrftoken = $.cookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  // var billarea = new Annotator($(".billarea"));
  var billarea = $(".billarea").annotator();
  var propietary = 'demoUser'
  billarea.annotator('addPlugin', 'Permissions', {
    user: propietary,
    permissions: {
      'read': [propietary],
      'update': [propietary],
      'delete': [propietary],
      'admin': [propietary]
  },
  showViewPermissionsCheckbox: true,
  showEditPermissionsCheckbox: false
  });

  // margin side-tab and scrollbar
  billarea.annotator('addPlugin', 'AnnotatorViewer');
  $('#anotacions-uoc-panel').slimscroll({height: '100%'});

  billarea.annotator('addPlugin', 'Store', {
    // The endpoint of the store on your server.
    prefix: '/annotations',

    urls: {
      // These are the default URLs.
      create:  '/',
      read:    '/:id',
      update:  '/:id',
      destroy: '/:id',
      search:  '/search'
    },

    // Attach the uri of the current page to all annotations to allow search.
    annotationData: {
      'bill_id': window.bill_id,
      // 'uri': 'http://this/document/only',
    },

    // // This will perform a "search" action when the plugin loads. Will
    // // request the last 20 annotations for the current url.
    // // eg. /store/endpoint/search?limit=20&uri=http://this/document/only
    // loadFromSearch: {
    //   'limit': 20,
    //   'uri': 'http://this/document/only'
    // }
  });

  // FYI: Tags are space-separated, not comma-separated
  // (Learned that from experience)
  billarea.annotator('addPlugin', 'Tags')

  // Bill-info: Helper functions
  var showAuthors = function() {
    var auth_size = window.authors.length;
    var auth_half = Math.ceil(auth_size / 2);

    var auth_left = window.authors.slice(0, auth_half);
    var auth_right = window.authors.slice(auth_half, auth_size);

    $('#billinfo-left').html(auth_left.join('<br />'));
    $('#billinfo-right').html(auth_right.join('<br />'));
  };

  var showSubjects = function() {
    var subj_size = window.subjects.length;
    var subj_half = Math.ceil(subj_size / 2);

    var subj_left = window.subjects.slice(0, subj_half);
    var subj_right = window.subjects.slice(subj_half, subj_size);

    $('#billinfo-left').html(subj_left.join('<br />'));
    $('#billinfo-right').html(subj_right.join('<br />'));
  };


  // Bill-info: Main code
  var billTrackerUrl = window.location.origin;

  window.billInfoLoaded = false;
  $.post(billTrackerUrl + '/bills/get-bill-info/',
    {  bill_id: window.bill_id, format: 'json' },
    function(data) {
      data = $.parseJSON(data)
      window.authors = data.authors
      window.subjects = data.subjects

      if ($('#btn-authors').hasClass("btn-selected")) {
        showAuthors();
      } else if ($('#btn-subjects').hasClass("btn-selected")) {
        showSubjects();
      }

      window.billInfoLoaded = true;
  });

  $('#btn-authors').click(function (e) {
    $('#btn-subjects').removeClass("btn-selected");
    $('#btn-authors').addClass("btn-selected");

    if (window.billInfoLoaded) {
      showAuthors();

    } else {
      $('#billinfo-left').html("Loading...");
    }
  });

  $('#btn-subjects').click(function (e) {
    $('#btn-authors').removeClass("btn-selected");
    $('#btn-subjects').addClass("btn-selected");

    if (window.billInfoLoaded) {
      showSubjects();

    } else {
      $('#billinfo-left').html("Loading...");
    }
  });
};
