$(document).ready(function(){
	$('.delete-multiple').hide()
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;
			});
			$('.delete-multiple').show()
		} else{
			checkbox.each(function(){
				this.checked = false;
			});
			$('.delete-multiple').hide()
		}
	});
	checkbox.click(function(){
		if(!this.checked){
			$('.delete-multiple').hide()
			$("#selectAll").prop("checked", false);
		}else{
			$('.delete-multiple').show()
		}
	});
	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			const cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	$(".employee-edit").click(function(ev) {
        ev.preventDefault();
        var url = $(this).data("form");
        var id = $(this).data("id");
		const csrftoken = getCookie('csrftoken');
		$.ajax({
            type: 'GET',
			headers: {'X-CSRFToken': csrftoken},
            url: url,
			dataType: 'json',
            success: function(data) {
				$("#editForm").attr('action','/employee/edit/'+ id)
				var emp = data[0].fields
				$("#name").val(emp.name)
				$("#email").val(emp.email)
				$("#phone").val(emp.phone)
				$("#group").val(emp.group)
				$("#edit-image").attr('src','/media/'+emp.image)
				$('#editEmployeeModal').modal('show')
            }
        });
        return false;
    });
	$(".employee-view").click(function(ev) {
        var url = $(this).data("form");
		$.ajax({
            type: 'GET',
            url: url,
			dataType: 'json',
            success: function(data) {
				var emp = data[0].fields
				var grp = data[1].fields
				console.log(grp.name)
				$("#view-name").val(emp.name)
				$("#view-email").val(emp.email)
				$("#view-phone").val(emp.phone)
				$("#view-group").val(grp.name)
				$("#view-image").attr('src','/media/'+emp.image)
				$('#viewEmployeeModal').modal('show')
            }
        });
    });
	$(".delete-single").click(function(ev) {
        var url = $(this).data("form");
		$("#deleteForm").attr('action',url)
    });

	$(".delete-multiple").click(function(ev) {
		var url = $(this).data("form");
		var deleteSelected = ''
		checkbox.each(function(){
			if(this.checked){
				deleteSelected += $(this).val() + ','
			}
		});
		if (deleteSelected != ''){
			$("#deleteForm").attr('action',url+deleteSelected)
			$('#deleteModal').modal('show')
		}
    });
	$(".clear-add-form").click(function(){
		$('#addForm').trigger("reset");
	})
	$(".user-edit").click(function(ev) {
        ev.preventDefault();
        var url = $(this).data("form");
        var id = $(this).data("id");
		const csrftoken = getCookie('csrftoken');
		$.ajax({
            type: 'GET',
			headers: {'X-CSRFToken': csrftoken},
            url: url,
			dataType: 'json',
            success: function(data) {
				$("#editForm").attr('action','/employee/edit_user/'+ id)
				var user = data[0].fields
				$("#username").val(user.username)
				$("#first_name").val(user.first_name)
				$("#last_name").val(user.last_name)
				$("#email").val(user.email)
				$("#is_superuser").val(user.is_superuser)
				$('#editUserModal').modal('show')
            }
        });
        return false;
    });
	$(".user-view").click(function(ev) {
        var url = $(this).data("form");
		$.ajax({
            type: 'GET',
            url: url,
			dataType: 'json',
            success: function(data) {
				var emp = data[0].fields
				var userType = "Normal User"
				if (emp.is_superuser){
					userType = "Super User"
				}
				$("#view-username").val(emp.username)
				$("#view-email").val(emp.email)
				$("#view-first-name").val(emp.first_name)
				$("#view-last-name").val(emp.last_name)
				$("#view-type").val(userType)
				$('#viewUserModal').modal('show')
            }
        });
    });
});