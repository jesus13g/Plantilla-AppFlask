// Función para mostrar los toasts (notificaciones emergentes)
function showToast(message, type) {
    var toast = $('<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">')
        .addClass(type)
        .html(`
            <div class="toast-body d-flex justify-content-between align-items-center">
                <span>${message}</span>
                <button type="button" class="btn-close ms-3 close-toast" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `);

    $('#toast-container').append(toast);

    toast.addClass('show');

    setTimeout(function() {
        toast.removeClass('show');
        setTimeout(function() {
            toast.remove();
        }, 500);
    }, 8000);
}


// Mostrar los mensajes de Flask automáticamente si están disponibles
$(document).ready(function() {
    $('#flash-messages .flash-message').each(function() {
        var message = $(this).data('message');
        var category = $(this).data('category');
        showToast(message, category);
    });
});