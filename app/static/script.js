(() => {
  const testUri = 'http://127.0.0.1:5000/api/trie/suggestions?limit=10&prefix=';
  const liveUri = 'http://mrhaffner.pythonanywhere.com/api/trie/suggestions?limit=10&prefix=';

  const arrayToSuggestionsLIs = (suggestions) => {
    return suggestions.map((suggestion) => {
      let li = document.createElement('li');
      li.textContent = suggestion;
      li.className = 'suggestion';
      return li;
    });
  };

  let input = document.getElementById('search-input');
  let suggestionsParent = document.getElementById('suggestions');
  let searchBar = document.getElementById('trie-search-bar');
  let form = document.getElementById('trie-form');
  let haveSuggestions = false;

  const hideSuggestions = () => {
    suggestionsParent.hidden = true;
    searchBar.classList.remove('search-bar-suggestions');
  };

  const showSuggestions = () => {
    searchBar.classList.add('search-bar-suggestions');
    suggestionsParent.hidden = false;
  };

  const updateSuggestions = async (e) => {
    const prefix = e.target.value;
    searchBar.classList.add('search-bar-active');

    if (e.target.value == '') {
      hideSuggestions();
      haveSuggestions = false;
      return;
    }

    const response = await fetch(`${liveUri}${encodeURI(prefix)}`);
    const suffixes = await response.json();
    const suggestions = suffixes.map((suffix) => prefix + suffix);

    if (!suggestions.length) {
      hideSuggestions();
      haveSuggestions = false;
      return;
    }

    suggestionsParent.children[1]?.remove(); // susceptible to breaking on change of url structure
    let ul = document.createElement('ul');
    suggestionsParent.append(ul);

    arrayToSuggestionsLIs(suggestions).forEach((node) => ul.appendChild(node));
    showSuggestions();
    haveSuggestions = true;
  };

  /**
   * @param {*} ctx The context
   * @param {function} func The function to execute after the debounce time
   * @param {number} delay The amount of time to wait
   * @return {function} The debounced function
   * @note From https://chiamakaikeanyi.dev/event-debouncing-and-throttling-in-javascript/
   */
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

  document.addEventListener('click', (e) => {
    const clickedInput = input.contains(e.target);
    const clickedOutsideForm = form.contains(e.target);

    if (clickedInput) {
      searchBar.classList.add('search-bar-active');
      if (haveSuggestions) {
        showSuggestions();
      }
    } else if (!clickedOutsideForm) {
      searchBar.classList.remove('search-bar-active');
      hideSuggestions();
    }
  });
})();
