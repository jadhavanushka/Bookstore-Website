// Flash messages
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
      var alerts = document.querySelectorAll('.alert');
      alerts.forEach(function(alert) {
        alert.style.transition = 'opacity 0.5s ease-out';
        alert.style.opacity = '0';
        setTimeout(function() { alert.remove(); }, 500);
      });
    }, 2000);
  });
  
  