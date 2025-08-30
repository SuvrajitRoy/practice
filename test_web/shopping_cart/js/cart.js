// Cart Logic
let cart = [];
let promoApplied = false;
let discountValue = 0;

// Add product to cart
function addToCart(productId) {
  const product = products.find(p => p.id === productId);
  const existingItem = cart.find(item => item.id === productId);

  if (existingItem) {
    existingItem.quantity++;
  } else {
    cart.push({ ...product, quantity: 1 });
  }
  updateCartUI();
}

// Update quantity
function updateQuantity(productId, newQty) {
  newQty = parseInt(newQty);
  if (isNaN(newQty) || newQty <= 0) {
    alert("Quantity must be at least 1!");
    return;
  }
  const item = cart.find(i => i.id === productId);
  if (item) {
    item.quantity = newQty;
  }
  updateCartUI();
}

// Remove all items
function clearCart() {
  cart = [];
  promoApplied = false;
  discountValue = 0;
  document.getElementById("promo-msg").textContent = "";
  updateCartUI();
}

// Calculate total
function calculateTotal() {
  let total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  if (promoApplied) {
    total -= total * discountValue;
  }
  return total.toFixed(2);
}

// ✅ Apply Promo Code
function applyPromoCode(code) {
  const msg = document.getElementById("promo-msg");

  if (promoApplied) {
    msg.textContent = "Promo code already applied!";
    msg.className = "text-red-600 mt-2 text-sm font-medium";
    return;
  }

  if (code === "ostad10") {
    discountValue = 0.1;
  } else if (code === "ostad50") {
    discountValue = 0.5;
  } else {
    msg.textContent = "Invalid Promo Code!";
    msg.className = "text-red-600 mt-2 text-sm font-medium";
    return;
  }

  promoApplied = true;
  msg.textContent = "Promo applied successfully!";
  msg.className = "text-green-600 mt-2 text-sm font-medium";
  updateCartUI();
}