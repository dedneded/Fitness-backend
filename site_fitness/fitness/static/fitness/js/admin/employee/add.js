$(document).ready(function(){
    strs = []
    role_delete = 0
    $('#table_modal :checkbox').change(function() {
        str = $(this).closest("tr").data("id");
        strs.push(str)

    });

    $('#edit_roles').on('submit', function (event){
        event.preventDefault();
        const csrf_token = $(this).find('[name=csrfmiddlewaretoken]').attr('value');
        //console.log($(this).attr('action'))
        $.ajax({
           url: $('#edit_roles').attr('action'),
           type: 'POST',
           data: {'roles': strs, 'csrfmiddlewaretoken': csrf_token},

           success: function (response){
               window.location.reload();
           },
           error: function (jqXHR){
               const response = jQuery.parseJSON(jqXHR.responseText)
               errors.handle_errors(response['message'], $('.errors_list'))
           },
       });


   });

   $("a#delete_role_button").click(function(){
        role_delete = $(this).closest("tr").data("id");
        
    });

   $('#delete_roles').on('submit', function (event){
   
        event.preventDefault();
        const csrf_token = $(this).find('[name=csrfmiddlewaretoken]').attr('value');
        
        $.ajax({
           url: $('#delete_roles').attr('action'),
           type: 'POST',
           data: {'role': role_delete, 'csrfmiddlewaretoken': csrf_token},

           success: function (response){
               window.location.reload();
           },
           error: function (jqXHR){
               const response = jQuery.parseJSON(jqXHR.responseText)
               errors.handle_errors(response['message'], $('.errors_list'))
           },
        });


    });

    
    
      
});