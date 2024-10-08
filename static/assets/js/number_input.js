
function formatNumber(input) {
      let value = input.value.replace(/,/g, ".");
      input.value = parseFloat(value).toFixed(2);
  }
  
function convertToComma(value) {
      return value.toString().replace(/\./g, ",");
  }
