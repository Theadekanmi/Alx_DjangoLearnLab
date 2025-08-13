// Main JavaScript file for Django Blog

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.message');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});