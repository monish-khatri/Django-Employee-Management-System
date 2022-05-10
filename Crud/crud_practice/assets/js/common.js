$(document).ready(function(){
	$('.delete-multiple').hide()

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
				var dob = emp.date_of_birth.split("-")
				$('#date_of_birth').data('daterangepicker').setStartDate(dob[1]+'/'+dob[2]+'/'+dob[0]);
				$('#editEmployeeModal').modal('show')
            }
        });
        return false;
    });
	$(".team-edit").click(function(ev) {
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
				$("#editForm").attr('action','/employee/edit_team/'+ id)
				var team = data[0].fields
				$("#name").val(team.name)
				$("#status").val(team.status)
				$('#editTeamModal').modal('show')
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
				$("#view-name").val(emp.name)
				$("#view-email").val(emp.email)
				$("#view-phone").val(emp.phone)
				finalDate = DateFormatter(emp.date_of_birth)
				$("#view-date_of_birth").val(finalDate)
				$("#view-group").val(grp.name)
				$("#view-image").attr('src','/media/'+emp.image)
				$('#viewEmployeeModal').modal('show')
            }
        });
    });
	function DateFormatter(date){
		const unformatdate = new Date(date)
		const formatyear = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(unformatdate)
		const formatmonth = new Intl.DateTimeFormat('en', { month: 'long' }).format(unformatdate)
		const formatdate = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(unformatdate)
		return formatdate + ' '+ formatmonth + ' ' + formatyear
	}
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
				$("#editForm").attr('action','/employee/edit_admin/'+ id)
				var user = data[0].fields
				$("#edit-username").val(user.username)
				$("#edit-first_name").val(user.first_name)
				$("#edit-last_name").val(user.last_name)
				$("#edit-email").val(user.email)
				$("#edit-is_superuser").prop('checked', user.is_superuser);
				$("#edit-is_active").prop('checked', user.is_active);

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
				var user = data[0].fields
				var userType = "Normal User"
				var userActive = "In-active"
				if (user.is_superuser){
					userType = "Super User"
				}
				if (user.is_active){
					userActive = "Active"
				}
				$("#view-username").val(user.username)
				$("#view-email").val(user.email)
				$("#view-first-name").val(user.first_name)
				$("#view-last-name").val(user.last_name)
				$("#view-status").val(userActive)
				$("#view-type").val(userType)
				$('#viewUserModal').modal('show')
            }
        });
    });
	$('input[name="date_of_birth"]').daterangepicker({
		autoApply: true,
		singleDatePicker: true,
		showDropdowns: true,
		minYear: 1979,
		maxYear: parseInt(moment().format('YYYY')),
		startDate: "23/08/1998",
		locale: {
			"format": "DD/MM/YYYY",
		}
	});
});