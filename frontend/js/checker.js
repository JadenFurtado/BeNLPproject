$(".check").click(function(){
    let encodedText = encodeURI($("#text").val());
    console.log(encodedText);
    $.ajax({
        url:"http://localhost:5000/api/corrections",
        data:{text:encodedText},
        type:"GET",
        success:function(data){
            console.log(data);
        }
    });
});