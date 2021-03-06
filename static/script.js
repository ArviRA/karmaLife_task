var status;

function validate() {
	var gender;
	status = true;
	var send_dict = {}
	var Emp;
	var dob = document.getElementById("dob").value;
	var fname = document.getElementById("fname").value;
	var lname = document.getElementById("lname").value;
	var male = document.getElementById("g1").checked;
	var female = document.getElementById("g2").checked;
	var employeStatus = document.getElementById("dropDown").value;
	if (fname != "" && lname != "") {
		send_dict["fname"] = fname;
		send_dict["lname"] = lname;
	} else {
		notVal("Name");
	}
	if (male == false && female == false) {
		notVal("Gender");
	} else if (male == true && female == false) {
		gender = "male"
		send_dict["gender"] = gender;
	} else {
		gender = "female"
		send_dict["gender"] = gender;
	}
	if (dob == "") {
		notVal("DOB");
	} else {
		send_dict["dob"] = dob;
	}
	if (employeStatus == "") {
		notVal("Employed");
	} else {
		send_dict["employed"] = employeStatus;
	}
	if (status == "true") {
		fetch('http://127.0.0.1:5000/insertEmployees', {
				method: 'POST',
				mode: 'cors',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(send_dict),
			}).then(response => {
				return response.json()
			})
			.then(response => {
				if (response.status == '200') {
					document.getElementById("fname").value = ""
					document.getElementById("lname").value = ""
					document.getElementById("g1").checked = false
					document.getElementById("g2").checked = false
					document.getElementById("dob").value = ""
					document.getElementById("dropDown").value = ""
					toast(1);
				} else {
					toast(0);
				}
			})
			.catch(Error => {
				toast(0)
			})
	}
}

function toast(data) {
	if (data == 1) {
		var x = document.getElementById("snackbar");

		// Add the "show" class to DIV
		x.className = "show";

		// After 3 seconds, remove the show class from DIV
		setTimeout(function () {
			x.className = x.className.replace("show", "");
		}, 3000);
	} else {
		document.getElementById("snackbar").innerHTML = "Something went wrong Try again"
		var x = document.getElementById("snackbar");

		// Add the "show" class to DIV
		x.className = "show";

		// After 3 seconds, remove the show class from DIV
		setTimeout(function () {
			x.className = x.className.replace("show", "");
		}, 3000);
	}

}

function notVal(data) {
	status = false;
	alert("All fields are mandatory\nFill the " + data + " field");
	//console.log(status)
}

function filter_table() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("emp_name");
	filter = input.value.toUpperCase();
	table = document.getElementById("tablecontent");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[0];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}