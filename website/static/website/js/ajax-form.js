(function ($) {
    'use strict';
    var form = $('.contact-form'),
        message = $('.messenger-box-contact__msg'),
        submitButton = $('#submit-form'),
        form_data;

    // Setup CSRF token for all AJAX requests
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');
    
    // Set up CSRF token for AJAX requests
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Success function
    function done_func(response) {
        message.fadeIn().removeClass('alert-danger').addClass('alert-success');
        message.text("Your message was sent successfully!");
        setTimeout(function () {
            message.fadeOut();
        }, 3000);
        form.find('input:not([type="submit"]), textarea').val('');
        $('#subject').val(''); // Reset select box too
        
        // Re-enable the submit button and restore its text
        submitButton.prop('disabled', false).html('Send Message');
    }

    // fail function
    function fail_func(data) {
        message.fadeIn().removeClass('alert-success').addClass('alert-danger');
        message.text(data.responseText || "An error occurred. Please try again.");
        setTimeout(function () {
            message.fadeOut();
        }, 3000);
        
        // Re-enable the submit button and restore its text
        submitButton.prop('disabled', false).html('Send Message');
    }
    
    form.submit(function (e) {
        e.preventDefault();
        
        const requiredMsg = document.getElementById('required-msg');
        const fullName = document.getElementById("full_name");
        const email = document.getElementById("email");
        const subject = document.getElementById("subject");

        // Form validation
        if (!fullName.value || !email.value || !subject.value) {
            requiredMsg.classList.add('show');
            if (!fullName.value) fullName.classList.add("invalid");
            if (!email.value) email.classList.add("invalid");
            if (!subject.value) subject.classList.add("invalid");
            return false;
        }
        
        requiredMsg.classList.remove('show');
        fullName.classList.remove("invalid");
        email.classList.remove("invalid");
        subject.classList.remove("invalid");
        
        // Disable the submit button and change its text
        submitButton.prop('disabled', true).html('<i class="las la-spinner la-spin"></i> Sending...');

        // Create FormData for file upload
        var formData = new FormData(form[0]);
        
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: formData,
            processData: false,
            contentType: false,
            success: done_func,
            error: fail_func
        });
    });
    
})(jQuery);