document.addEventListener("DOMContentLoaded", () => {

  /* ===== HAMBURGER MENU ===== */
  const hamburger = document.querySelector(".hamburger");
  const nav = document.querySelector("header .nav");

  if (hamburger && nav) {
    hamburger.addEventListener("click", () => {
      nav.classList.toggle("active");
    });
  }

  /* ===== BUY NOW ALERT ===== */
  document.querySelectorAll(".btn1").forEach(btn => {
    btn.addEventListener("click", () => {
      alert("You are in Buy Now section");
    });
  });

  /* ===== CART (LOCAL STORAGE) ===== */
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const cartItems = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");

  function renderCart() {
    if (!cartItems || !cartTotal) return;

    cartItems.innerHTML = "";
    let total = 0;

    cart.forEach((item, index) => {
      const li = document.createElement("li");

      li.innerHTML = `
        <span>${item.name} - ₹${item.price} × ${item.quantity}</span>
        <button class="remove-btn">❌</button>
      `;

      li.querySelector(".remove-btn").onclick = () => {
        cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(cart));
        renderCart();
      };

      cartItems.appendChild(li);
      total += item.price * item.quantity;
    });

    cartTotal.textContent = `₹${total.toLocaleString()}`;
  }

  renderCart();

  document.querySelectorAll(".add-cart").forEach(btn => {
    btn.addEventListener("click", () => {
      const name = btn.dataset.name;
      const price = Number(btn.dataset.price);

      const found = cart.find(p => p.name === name);
      found ? found.quantity++ : cart.push({ name, price, quantity: 1 });

      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    });
  });

  /* ===== ANIMATION (IntersectionObserver) ===== */
  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  document
    .querySelectorAll(".cloth-item, .cl-card, .related-card")
    .forEach(el => observer.observe(el));

  /* ===== FINAL BUTTON ===== */
  const btn1 = document.getElementById("btn1");
  if (btn1) {
    btn1.addEventListener("click", () => {
      alert("You are in Shop Now section");
    });
  }
});
const slides = document.querySelectorAll('.banner-slide');
let currentSlide = 0;

if (slides.length > 0) {
  slides[0].classList.add('active');

  setInterval(() => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
  }, 5000);
}
