
var uploader = document.querySelector(".file-upload")
var loader = document.querySelector(".loading")

loader.style.display = "none";

document.querySelector(".upload-btn").addEventListener('click', (eve) => {

    eve.preventDefault();

    uploader.click();
    uploader.onchange = (e) => {
        e.preventDefault();

        loader.style.display = "flex";

        var filepath = e.target.files;
        var data = new FormData()
        data.append("dfile", filepath[0])

        document.querySelector('.container').style.display = 'none';
        document.querySelector('.details').style.display = 'flex';

        fetch("/upload-file", {
            method: 'POST',
            body: data,
        }).then(
            (res) => res.json()
        ).then(
            (res) => {
                if(res["status"]==true){
                    // alert("found");
                    var ext=document.querySelector('.extension');
                    var details=document.querySelector('.description');
                    ext.innerHTML=res["extension"];
                    details.innerHTML=res["summary"];
                }
                else{
                    alert("Extension Not Found");
                }
                loader.style.display = "none";
            }
        ).catch(
            ()=>{
                alert("Error in Connection")
                document.querySelector('.container').style.display = 'flex';
                document.querySelector('.details').style.display = 'none';
                loader.style.display = "none";

            }
        );
    }
})