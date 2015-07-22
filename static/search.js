var billTracker = angular.module("bill-tracker", []).config(function($httpProvider) {
    // http://django-angular.readthedocs.org/en/latest/csrf-protection.html
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

billTracker.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common["X-Requested-With"] = 'XMLHttpRequest';
}]);

billTracker.controller("BillController", function($scope, $window, $http) {

    // Retrieve bill with given id from database
    $http.get("/bills/"+ $window.bill_id).success(function (data) {
        $scope.bill = data[0]["fields"];
    });
});

billTracker.controller("BillsListController", function($scope, $http) {

    // Retrieve bills data from database
    $http.get("/get_bill_list").success(function (data) {

        var bills_list = [];
        for (index = 0; index < data.length; index++) {
            bills_list.push(data[index]["fields"]);
            bills_list[index]["id"] = data[index]["pk"];
            // Name of the bill is the first 1000 characters of its text.
            // Used for displaying in bill list.
            bills_list[index]["name"] = data[index]["fields"]["text"].substring(0, 1000);
        }
        $scope.bills = bills_list;
    });
});

billTracker.controller("AuthorListController", function($scope, $http) {

    // Retrieve authors (senators) data from database
    $http.get("/get_author_list").success(function(data) {

        var author_list = [];
        for (index = 0; index < data.length; index++) {
            author_list.push(data[index]["fields"]);
            author_list[index]["id"] = data[index]["pk"];
            author_list[index]["model"] = data[index]["model"];
        }

        $scope.authors = author_list;
    });
});

billTracker.controller("SubjectListController", function($scope, $http) {

    // Retrieve subjects data from database
    $http.get("/get_subject_list").success(function(data) {

        var subject_list = [];
        for (index = 0; index < data.length; index++) {
            subject_list.push(data[index]["fields"]);
            subject_list[index]["id"] = data[index]["pk"];
            subject_list[index]["model"] = data[index]["model"];
        }

        $scope.subjects = subject_list;
    });
});

billTracker.controller("BillsByAuthorController", function($scope, $window, $http) {

    // Retrieve bills authored by author with specified id
    $http.get("/get_author_bills", {params: {id: $window.author_id}}).success(function(data) {

        var bills_list = [];
        for (index = 0; index < data.length; index++) {
            bills_list.push(data[index]["fields"]);
            bills_list[index]["id"] = data[index]["pk"];
            // Name of the bill is the first 1000 characters of its text.
            // Used for displaying in bill list.
            bills_list[index]["name"] = data[index]["fields"]["text"].substring(0, 1000);
        }

        $scope.bills = bills_list;
    });
});

billTracker.controller("BillsBySubjectController", function($scope, $window, $http) {

    // Retrieve bills about specified subject
    $http.get("/get_subject_bills", {params: {id: $window.subject_id}}).success(function(data) {

        var bills_list = [];
        for (index = 0; index < data.length; index++) {
            bills_list.push(data[index]["fields"]);
            bills_list[index]["id"] = data[index]["pk"];
            // Name of the bill is the first 1000 characters of its text.
            // Used for displaying in bill list.
            bills_list[index]["name"] = data[index]["fields"]["text"].substring(0, 1000);
        }

        $scope.bills = bills_list;
    });
});

billTracker.filter('highlight', function($sce) {
    // object is bill/author/subject
  return function (object, search) {

      text = object.name;

      if (text && (search || angular.isNumber(search))) {
          text = text.toString();
          search = search.toString();
          text = text.replace(new RegExp(search, 'gi'), '<span class="highlighted">$&</span>');
      }

      switcher = {
          "annotation_app.senator": "authors",
          "annotation_app.subject": "subjects",
          "annotation_app.bill": "bills"
      }

      // Need to return as trusted html, otherwise angular throws "unsafe html" error
      return $sce.trustAsHtml('<li class="active"><a href="/' + switcher[object.model] +
          '/' + object.id + '/">'+ text + '</li>');
  }

});

billTracker.filter('highlightText', function($sce) {
    // object is bill text
  return function (object, search) {

      text = object.text;

      if (text && (search || angular.isNumber(search))) {
          text = text.toString();
          search = search.toString();
          text = text.replace(new RegExp(search, 'gi'), '<span class="highlighted">$&</span>');
      }
      // Need to return as trusted html, otherwise angular throws "unsafe html" error
      return $sce.trustAsHtml(text);
  }

});