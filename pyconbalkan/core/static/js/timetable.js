$(".btn-room").click(function() {
    // alert('start');
    let roomNumber = this.innerHTML;
    $(".btn-room").removeClass('button--yellow');
    $(".presentations").addClass('hidden');
    $("." + roomNumber).removeClass('hidden');
    $(".btn-" + roomNumber).addClass('button--yellow');
    // alert('end');
});