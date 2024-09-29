 // TAILOR MADE FOR THE HOME OR INDEX WEBPAGE

  // Script for filtering products
    function filterSelection(category) {
      const products = document.querySelectorAll('.column');
      products.forEach(product => {
        if (category === 'all' || product.classList.contains(category)) {
          product.style.display = 'block';
        } else {
          product.style.display = 'none';
        }
      });
    }

    // Function to add item to cart
    function addToCart(itemName, itemPrice) {
      let cart = JSON.parse(localStorage.getItem('cart')) || [];
      cart.push({ itemName, itemPrice });
      localStorage.setItem('cart', JSON.stringify(cart));
      alert(itemName + " added to cart!");
    }

    // Redirect to checkout/cart page
    function redirectToCart() {
      window.location.href = 'checkout.html';
    }

    // Open Sign In page
    function openSignIn() {
      window.location.href = 'access.html';
    }

 // TAILOR MADE FOR THE ACCESS WEBPAGE

 // Get the modal
	var modal = document.getElementById('id01');

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
		}
	}

	function openForm() {
	document.getElementById("myForm").style.display = "block";
	}

	function closeForm() {
	document.getElementById("myForm").style.display = "none";
	}

// Handle Sign Up Form Submission
document.querySelector('.modal-content').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission

  // Collect form data
  const formData = {
    firstName: document.querySelector('input[name="first_name"]').value,
    surname: document.querySelector('input[name="surname"]').value,
    email: document.querySelector('input[name="email_address"]').value,
    contact: document.querySelector('input[name="contact_number"]').value,
    altContact: document.querySelector('input[name="alt_number"]').value,
    address: document.querySelector('input[name="location"]').value,
    password: document.querySelector('input[name="psw"]').value,
    username: document.querySelector('input[name="username"]').value
  };

  // Save user data (This should ideally be done server-side)
  localStorage.setItem('userData', JSON.stringify(formData));

  alert("Sign up successful! You can now sign in.");
  document.getElementById('id01').style.display = 'none'; // Close modal
});

// Handle Sign In Form Submission
document.querySelector('.form-container form').addEventListener('submit', function(event) {
  event.preventDefault();

  // Get input values
  const username = document.querySelector('input[name="username"]').value;
  const password = document.querySelector('input[name="psw"]').value;

  // Retrieve stored user data
  const storedUserData = JSON.parse(localStorage.getItem('userData'));

  // Check if credentials match
  if (storedUserData && storedUserData.username === username && storedUserData.password === password) {
    alert("Login successful!");
    window.location.href = 'index.html'; // Redirect to home page after login
  } else {
    alert("Invalid username or password.");
  }
});

 // TAILOR MADE FOR THE CHECKOUT WEBPAGE

// Assuming items and prices are stored in JS for dynamic updates

        // Example calculation
        let subtotal = 1050;  // Example subtotal
        let vat = subtotal * 0.15;
        let total = subtotal + vat;

        document.getElementById('subtotal').innerText = 'R' + subtotal.toFixed(2);
        document.getElementById('vat').innerText = 'R' + vat.toFixed(2);
        document.getElementById('total').innerText = 'R' + total.toFixed(2);
