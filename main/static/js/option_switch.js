const toastLiveExample = document.getElementById('liveToast')
$(document).ready(function () {
    $("#btnradio1").click(function () {
        $(location).prop('href', 'theory')
        // location.reload();
    });
    $("#btnradio2").click(function () {
        $(location).prop('href', 'practice')
        // location.reload(); 
    });
    $("#btnradio3").click(function () {
        $(location).prop('href', 'answers')
        // location.reload(); 
    });
    const toast = new bootstrap.Toast(toastLiveExample)
    toast.show()
});
