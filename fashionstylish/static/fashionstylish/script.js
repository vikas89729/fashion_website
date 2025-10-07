let hamburger = document.querySelector(".hamburger");
let nav = document.querySelector("header .nav");
if (hamburger && nav) {
  hamburger.addEventListener("click", () => {
    nav.classList.toggle("active")
  });

} document.addEventListener("DOMContentLoaded", () => {
  let allbtn = document.querySelectorAll(".btn1");

  allbtn.forEach(element => {
    element.addEventListener("click", () => {
      alert("you are in buy now section");
    });
  });
});
document.addEventListener("DOMContentLoaded", () => {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  const cartitem = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");

  function renderCart() {
    cartitem.innerHTML = "";
    let total = 0;

    cart.forEach((p, index) => {
      let li = document.createElement("li");

      // Text container
      let span = document.createElement("span");
      span.textContent = `${p.name} - ₹${p.price} x ${p.quantity}`;

      // Remove button
      let removeBtn = document.createElement("button");
      removeBtn.textContent = "❌";
      removeBtn.style.background = "#ff4d4f";
      removeBtn.style.color = "white";
      removeBtn.style.borderRadius = "4px";
      removeBtn.style.border = "none";
      removeBtn.style.cursor = "pointer";
      removeBtn.addEventListener("click", () => {
        cart.splice(index, 1); // remove the item
        localStorage.setItem("cart", JSON.stringify(cart));
        renderCart();
      });

      li.appendChild(span);
      li.appendChild(removeBtn);
      cartitem.appendChild(li);

      total += p.price * p.quantity;
    });

    cartTotal.textContent = `₹${total.toLocaleString()}`;
  }

  renderCart();

  // Add to cart buttons
  document.querySelectorAll(".add-cart").forEach(btn => {
    btn.addEventListener("click", () => {
      const name = btn.dataset.name;
      const price = parseFloat(btn.dataset.price);

      // Check if product exists
      let existing = cart.find(p => p.name === name);
      if (existing) {
        existing.quantity += 1;
      } else {
        cart.push({ name: name, price: price, quantity: 1 });
      }

      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    });
  });
});






document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll(".cloth-item");

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.2 });

  items.forEach(item => {
    observer.observe(item);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".cl-card");

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, { threshold: 0.2 });

  cards.forEach(card => observer.observe(card));
});
let button=document.getElementById("btn1")
button.addEventListener(click=>{
alert(" you are a shop now section")
});