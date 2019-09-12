
// function Submit(){

document.getElementById('btn-1').addEventListener('click', function (){
    validateForm();
});
// }



function validateForm() {



    let REGIS = document.getElementById("REGIS-1").value;
    let BIRTHDATE = document.getElementById("BIRTHDATE-1").value;
    let GENDER = document.getElementById("GENDER-1").value;
    let Name = document.getElementById("Name-1").value;
    let CLASS = document.getElementById("CLASS-1").value;

    let List = [
        REGIS,
        BIRTHDATE,
        GENDER,
        Name,
        CLASS
    ]
    alert(List)

}