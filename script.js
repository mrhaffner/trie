const testArr = ['Apple', 'AppleOrchard', 'Apple Orchard'];
const testUri = 'http://127.0.0.1:5000/trie?prefix=';

const headers = {};

const arrayToSuggestionsLIs = (suggestions) => {
  return suggestions.map((suggestion) => {
    let li = document.createElement('li');
    li.textContent = suggestion;
    li.className = 'auto-suggestion';
    return li;
  });
};

let input = document.getElementById('search-input');
let suggestionsParent = document.getElementById('suggestions');

// needs to handle error
const updateSuggestions = (e) => {
  suggestionsParent.firstChild?.remove();
  let ul = document.createElement('ul');
  suggestionsParent.append(ul);
  fetch(`${testUri}${e.target.value}`)
    .then((response) => response.json())
    .then((suggestions) => arrayToSuggestionsLIs(suggestions))
    .then((nodes) => nodes.forEach((node) => ul.appendChild(node)));
};

input.addEventListener('change', updateSuggestions);
