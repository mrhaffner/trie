const testArr = ['Apple', 'AppleOrchard', 'Apple Orchard'];

let suggestionsParent = document.getElementById('suggestions');

const suggestions = testArr.map((s) => {
  let li = document.createElement('li');
  li.textContent = s;
  li.className = 'auto-suggestion';
  return li;
});

suggestions.forEach((e) => suggestionsParent.appendChild(e));
