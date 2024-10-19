    const dashButton = document.getElementById('cartItemDash');
    const plusButton = document.getElementById('cartItemPlus');
    const inputField = document.querySelector('input[name="cant"]');
    
    let currentValue = parseInt(inputField.value);
    
    dashButton.addEventListener('click', () => {
      currentValue = Math.max(1, currentValue - 1);
      inputField.value = currentValue;
    });
    
    plusButton.addEventListener('click', () => {
      currentValue++;
      inputField.value = currentValue;
    });