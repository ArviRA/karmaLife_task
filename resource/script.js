var status = true;
function validate()
{   var gender;
    var send_dict = {}
    var Emp;
    var dob = document.getElementById("dob").value;
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var male = document.getElementById("g1").checked;
    var female = document.getElementById("g2").checked;
    var employeStatus = document.getElementById("dropDown").value;
    if(fname !="" && lname!="")
    {
        send_dict["fname"] = fname;
        send_dict["lname"] = lname;
    }
    else
    {
        notVal("Name");
    }
    if(male == false && female == false)
    {
        notVal("Gender");
    }
    else if(male == true && female == false)
    {
        gender = "male"
        send_dict["gender"] = gender;
    }
    else
    {
        gender = "female"
        send_dict["gender"] = gender;
    }
    if (dob =="")
    {
        notVal("DOB");
    }
    else
    {
        send_dict["dob"] = dob;
    }
    if (employeStatus =="")
    {
    notVal("Employed");
    }
    else{
      send_dict["employed"] = employeStatus;  
    }
    if(status == true)
    {
    console.log(JSON.stringify(send_dict))
    }
}
function notVal(data)
{   status = false;
    alert("All fields are mandatory\nFill the "+data+" field");
    console.log(status)
}