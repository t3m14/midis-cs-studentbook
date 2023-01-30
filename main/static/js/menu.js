$(document).ready(function () {
    
    $("#flexSwitchCheckDefault").click(function () {
        if ($("#flexSwitchCheckDefault").is(':checked')){
            $("html").attr("data-bs-theme","light");
        } else {
            $("html").attr("data-bs-theme","dark");
        }
    });
    
});
