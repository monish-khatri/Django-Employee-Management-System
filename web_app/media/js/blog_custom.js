$(document).ready(function(){
  
    $( document ).tooltip();

    $('#blogIndex').DataTable({
      "searching": false,
      "paging": false,
      "aoColumns":[
          {"bSortable": false},
          {"bSortable": false},
          {"bSortable": true},
          {"bSortable": true},
          {"bSortable": false}
      ]
    });
    $( "#accordion" ).accordion({
      collapsible: true,
    });
    $( ".widget" ).button();
    $( ".searchCat" ).selectmenu();
    $(function () {
      $('[data-toggle="tooltip"]').tooltip();
    })

    /** Select2 **/
    $("#id_blog_category").select2();
    $("#id_blog_tags").select2({
      tags: true,
    });
  });