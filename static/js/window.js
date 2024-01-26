const openDropdownButton = document.getElementById('openDropdownButton');
const dropdownContainer = document.getElementById('dropdownContainer');

openDropdownButton.addEventListener('click', function() {
  toggleDropdown();
});

function toggleDropdown() {
  dropdownContainer.style.display = dropdownContainer.style.display === 'none' ? 'flex' : 'none';
}