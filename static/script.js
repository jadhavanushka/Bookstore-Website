// Flash messages

document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
      alert.style.transition = 'opacity 0.5s ease-out';
      alert.style.opacity = '0';
      setTimeout(function () { alert.remove(); }, 500);
    });
  }, 2000);
});


// toggle description

document.addEventListener('DOMContentLoaded', function() {
  const description = document.querySelector('.description');
  const button = document.querySelector('.show-more-btn');

  // Check if the description is short
  if (description.scrollHeight <= 125) {
      button.style.display = 'none';
  }
});


function toggleDescription() {
  const description = document.querySelector('.description');
  const button = document.querySelector('.show-more-btn');
  
  if (description.classList.contains('expanded')) {
      description.classList.remove('expanded');
      button.textContent = 'Show more';
  } else {
      description.classList.add('expanded');
      button.textContent = 'Show less';
  }
}

// submit forms
function placeOrder() {
  document.getElementById('checkout-form').submit();
}

function submitAddressForm() {
  document.getElementById('address-form').submit();
}
