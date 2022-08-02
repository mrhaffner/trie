// needs an IIFE

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

// debounce
// should not make requests if there are character(s) and already no suggestions
// handle spaces? other characters? back and on front

const updateSuggestions = async (e) => {
  if (e.target.value == '') {
    suggestionsParent.hidden = true;
    return;
  }

  const response = await fetch(`${testUri}${encodeQuery(e.target.value)}`);
  const suggestions = await response.json();

  if (!suggestions.length) {
    suggestionsParent.hidden = true;
    return;
  }

  suggestionsParent.firstChild?.remove();
  let ul = document.createElement('ul');
  suggestionsParent.append(ul);

  arrayToSuggestionsLIs(suggestions).forEach((node) => ul.appendChild(node));
  suggestionsParent.hidden = false;
};

input.addEventListener('input', updateSuggestions);

function encodeQuery(query) {
  return query.replaceAll(' ', '%20');
}
