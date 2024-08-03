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

function submitProfileForm() {
  document.getElementById('profile-form').submit();
}

function populateAddressForm(address) {
  const modalTitle = document.getElementById('address_modal_title');
  if (address) {
      document.getElementById('address_id').value = address.address_id;
      document.getElementById('street').value = address.street;
      document.getElementById('city').value = address.city;
      document.getElementById('state').value = address.state;
      document.getElementById('country').value = address.country;
      document.getElementById('pincode').value = address.pincode;
      document.getElementById('is_default').checked = address.is_default;
      modalTitle.textContent = 'Edit Address';
  } else {
      document.getElementById('address-form').reset();
      document.getElementById('address_id').value = '';
      document.getElementById('is_default').checked = false;
      modalTitle.textContent = 'Add Address';
  }
}

document.addEventListener("DOMContentLoaded", function() {
  // Function to update URL query parameter
  function updateQueryParam(param, value) {
      var url = new URL(window.location);
      url.searchParams.set(param, value);
      history.pushState(null, null, url);
  }

  // Function to activate the correct tab based on query parameter
  function activateTabFromQuery() {
      var urlParams = new URLSearchParams(window.location.search);
      var tab = urlParams.get('tab');

      if (tab) {
          $('.list-group-item[href="#' + tab + '"]').tab('show');
      } else {
          // Default to the first tab if the tab parameter is not present
          $('.list-group-item:first').tab('show');
      }
  }

  // Listen for tab clicks and update the URL query parameter
  $('.profile-tabs a').on('click', function(e) {
      var tabId = this.hash.substring(1); // Get the tab id without the #
      updateQueryParam('tab', tabId);
  });

  // Activate the correct tab when the page loads
  activateTabFromQuery();
});
