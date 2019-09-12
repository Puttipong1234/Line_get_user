


window.onload = function (e) {
    liff.init(function() {
        validateForm();
    });
};


function validateForm() {



    document.getElementById('btn-1').addEventListener('click', function () {

        const REGIS = document.getElementById("REGIS-1").value;
        const BIRTHDATE = document.getElementById("BIRTHDATE-1").value;
        const GENDER = document.getElementById("GENDER-1").value;
        const Name = document.getElementById("Name-1").value;
        const CLASS = document.getElementById("CLASS-1").value;

        liff.sendMessages([{
            type: 'text',
            text: `ยืนยันการลงทะเบียน ${Name} เพศ ${GENDER} เกิดวันที่ ${BIRTHDATE} เลขประจำตัว ${REGIS} ได้ลงทะเบียนเรียน ${CLASS} `
        }]).then(function () {
            window.alert("Message sent");
        }).catch(function (error) {
            window.alert("Error sending message: " + error);
        }).then(function(){
            liff.closeWindow();
        });
    });


}