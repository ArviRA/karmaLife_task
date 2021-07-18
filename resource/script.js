function validate()
{   var gender;
    var dob = document.getElementById("dob").value;
    
    var fname = document.getElementById("fname").value;
    var male = document.getElementById("g1").checked;
    var female = document.getElementById("g2").checked;
    if(male == false && female == false)
    {
    
        //alert("Fill all the fields")
    }
    else if(male == true && female == false)
    {
        //alert("male")
        gender = "male"

    }
    else{
        //alert("female")
        gender = "female"
    }

    console.log(gender,dob);
}