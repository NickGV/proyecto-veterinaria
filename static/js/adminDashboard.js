document.addEventListener('DOMContentLoaded', function () {
  const dropdownLinks = document.querySelectorAll('.dropdown-toggle');
  dropdownLinks.forEach(link => {
    link.addEventListener('click', function () {
      dropdownLinks.forEach(otherLink => {
        if (otherLink !== link) {
          const submenu = document.getElementById(otherLink.getAttribute('aria-controls'));
          if (submenu.classList.contains('show')) {
            new bootstrap.Collapse(submenu, { toggle: true });
          }
        }
      });
    });
  });
});
