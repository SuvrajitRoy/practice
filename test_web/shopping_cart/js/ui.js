// Display Products
function renderProducts() {
  const container = document.getElementById("product-list");
  container.innerHTML = products.map(product => `
    <div class="bg-white p-4 rounded shadow-md product-card">
      <img src="${product.image}" alt="${product.name}" class="w-full h-40 object-cover rounded">
      <h3 class="text-lg font-bold mt-2">${product.name}</h3>
      <p class="text-gray-600">${product.description}</p>
      <p class="text-lg font-semibold mt-2">$${product.price}</p>
      <button onclick="addToCart(${product.id})" 
        class="bg-blue-600 text-white px-3 py-2 mt-3 rounded hover:bg-blue-700">
        Add to Cart
      </button>
    </div>
  `).join("");
}

// Display Cart Items
function updateCartUI() {
  const cartItems = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");
  const cartCount = document.getElementById("cart-count");

  if (cart.length === 0) {
    cartItems.innerHTML = "<p>Your cart is empty.</p>";
    cartTotal.textContent = "0";
    cartCount.textContent = "0";
    return;
  }

  cartItems.innerHTML = cart.map(item => `
    <div class="flex justify-between items-center border-b pb-2">
      <div>
        <p class="font-bold">${item.name}</p>
        <p>$${item.price} x 
          <input type="number" min="1" value="${item.quantity}" 
            onchange="updateQuantity(${item.id}, this.value)" 
            class="w-16 border rounded text-center">
        </p>
      </div>
      <p class="font-semibold">$${(item.price * item.quantity).toFixed(2)}</p>
    </div>
  `).join("");

  cartTotal.textContent = calculateTotal();
  cartCount.textContent = cart.reduce((sum, item) => sum + item.quantity, 0);
}

// Event Listeners
document.getElementById("clear-cart").addEventListener("click", clearCart);
document.getElementById("checkout").addEventListener("click", () => {
  if (cart.length === 0) {
    alert("Your cart is empty!");
  } else {
    alert(`Checkout Successful! Total: $${calculateTotal()}`);
    clearCart();
  }
});

// ✅ Promo button event
document.getElementById("apply-promo").addEventListener("click", () => {
  const code = document.getElementById("promo-code").value.trim().toLowerCase();
  applyPromoCode(code);
});


// Initialize
renderProducts();
updateCartUI();


