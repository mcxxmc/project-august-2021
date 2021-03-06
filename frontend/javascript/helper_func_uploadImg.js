let urlPostImage = 'http://localhost:8080/upload';  // must specify http to enable CORS
let urlPostImageFast = 'http://localhost:8080/prediction';

$(document).ready(function (e) {
    $('#form_img').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type:'POST',
            url: urlPostImage,
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                alert(data["r"])
                console.log("success");
                console.log(data);
            },
            error: function(data){
                alert("error!");
                console.log("error");
                console.log(data);
            }
        });
    }));

    $('#form_img_fast').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type:'POST',
            url: urlPostImageFast,
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                alert(data["r"])
                console.log("success");
                console.log(data);
            },
            error: function(data){
                alert("error!");
                console.log("error");
                console.log(data);
            }
        });
    }));
});
