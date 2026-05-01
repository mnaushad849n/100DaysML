const themeToggle = document.querySelector("#themeToggle");

// Load saved theme when page opens
window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme === "dark") {
    document.body.classList.add("dark");
    themeToggle.textContent = "Light";
  } else {
    themeToggle.textContent = "Dark";
  }
});

// Toggle theme on button click
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");

  const isDark = document.body.classList.contains("dark");

  themeToggle.textContent = isDark ? "Light" : "Dark";

  localStorage.setItem("theme", isDark ? "dark" : "light");
});
