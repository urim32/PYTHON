$.ajax({

    type: "GET",
    url: "/get_images",
}).done(function (data) {
    let res = JSON.parse(data);
    for (let i = 0; i < res.length; i++) {
        let imgCreate = $("<img>");
        imgCreate.attr("src", res[i]);
        $("#img").append(imgCreate);


    }

});