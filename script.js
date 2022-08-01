const testArr = ['Apple', 'AppleOrchard', 'Apple Orchard'];
const testUri = 'http://127.0.0.1:5000/trie?prefix=App';

const headers = {};

let suggestionsParent = document.getElementById('suggestions');

const arrayToSuggestionsLIs = (suggestions) => {
  return suggestions.map((suggestion) => {
    let li = document.createElement('li');
    li.textContent = suggestion;
    li.className = 'auto-suggestion';
    return li;
  });
};

// needs to handle error
fetch(testUri, headers)
  .then((response) => response.json())
  .then((suggestions) => arrayToSuggestionsLIs(suggestions))
  .then((nodes) =>
    nodes.forEach((node) => suggestionsParent.appendChild(node)),
  );
