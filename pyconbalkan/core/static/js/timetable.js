$(".btn-room").click(function() {
    let roomNumber = this.innerHTML;
    $(".btn-room").removeClass('button--yellow');
    $(".presentations").addClass('hidden');
    $("." + roomNumber).removeClass('hidden');
    $(".btn-" + roomNumber).addClass('button--yellow');
});