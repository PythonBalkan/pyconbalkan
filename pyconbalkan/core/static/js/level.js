function radio() {
    var content = document.querySelector('input[name="level"]:checked');
    var label = document.getElementById('label_name');
    label.innerText = content.value + ":";


    $(content).each(function() {
        var idVal = $(this).attr("id");
        var level_value = $("label[id='"+idVal+"_value']");
        var label_value = document.getElementById('total');
        label_value.innerText = level_value.text();
    });
}
