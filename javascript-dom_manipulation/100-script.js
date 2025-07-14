document.addEventListener('DOMContentLoaded', function () {
  // Get all necessary elements
  const addItemBtn = document.getElementById('add_item');
  const removeItemBtn = document.getElementById('remove_item');
  const clearListBtn = document.getElementById('clear_list');
  const myList = document.querySelector('ul.my_list');

  // Add item function
  addItemBtn.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  // Remove last item function
  removeItemBtn.addEventListener('click', function () {
    const items = myList.querySelectorAll('li');
    if (items.length > 0) {
      myList.removeChild(items[items.length - 1]);
    }
  });

  // Clear all items function
  clearListBtn.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
