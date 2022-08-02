// needs an IIFE

const testUri = 'http://127.0.0.1:5000/trie?prefix=';

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

const updateSuggestions = async (e) => {
  if (e.target.value == '') {
    suggestionsParent.hidden = true;
    return;
  }

  const response = await fetch(`${testUri}${encodeURI(e.target.value)}`);
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

const debounce = (context, func, delay) => {
  let timeout;

  return (...arguments) => {
    if (timeout) {
      clearTimeout(timeout);
    }

    timeout = setTimeout(() => {
      func.apply(context, arguments);
    }, delay);
  };
};

input.addEventListener('input', debounce(this, updateSuggestions, 150));
