(() => {
  // const apiTrieUri =
  //   'http://127.0.0.1:5000/api/trie/suggestions?limit=10&prefix=';
  // const apiWeightedUri =
  //   'http://127.0.0.1:5000/api/weighted-trie/suggestions?limit=10&prefix=';
  // const apiCachedUri =
  //   'http://127.0.0.1:5000/api/cached-trie/suggestions?limit=10&prefix=';
  const apiTrieUri =
    'http://mrhaffner.pythonanywhere.com/api/trie/suggestions?limit=10&prefix=';
  const apiWeightedUri =
    'http://mrhaffner.pythonanywhere.com/api/weighted-trie/suggestions?limit=10&prefix=';
  const apiCachedUri =
    'http://mrhaffner.pythonanywhere.com/api/cached-trie/suggestions?limit=10&prefix=';

  const arrayToSuggestionsLIs = (suggestions) => {
    return suggestions.map((suggestion) => {
      let li = document.createElement('li');
      li.textContent = suggestion;
      li.className = 'suggestion';
      return li;
    });
  };

  let input = document.getElementById('search-input');
  let weightedInput = document.getElementById('weighted-search-input');
  let cachedInput = document.getElementById('cached-search-input');
  let suggestionsParent = document.getElementById('suggestions');
  let weightedSuggestionsParent = document.getElementById(
    'weighted-suggestions',
  );
  let cachedSuggestionsParent = document.getElementById('cached-suggestions');
  let searchBar = document.getElementById('trie-search-bar');
  let weightedSearchBar = document.getElementById('trie-weighted-search-bar');
  let cachedSearchBar = document.getElementById('trie-cached-search-bar');
  let form = document.getElementById('trie-form');
  let weightedForm = document.getElementById('trie-weighted-form');
  let cachedForm = document.getElementById('trie-cached-form');
  let haveSuggestions = false;
  let haveWeightedSuggestions = false;
  let haveCachedSuggestions = false;

  const hideSuggestions = (parent, search) => {
    parent.hidden = true;
    search.classList.remove('search-bar-suggestions');
  };

  const showSuggestions = (parent, search) => {
    search.classList.add('search-bar-suggestions');
    parent.hidden = false;
  };

  const updateSuggestions = async (e) => {
    const prefix = e.target.value;
    searchBar.classList.add('search-bar-active');

    if (e.target.value == '') {
      hideSuggestions(suggestionsParent, searchBar);
      haveSuggestions = false;
      return;
    }

    const response = await fetch(`${apiTrieUri}${encodeURI(prefix)}`);
    const suffixes = await response.json();
    const suggestions = suffixes.map((suffix) => prefix + suffix);

    if (!suggestions.length) {
      hideSuggestions(suggestionsParent, searchBar);
      haveSuggestions = false;
      return;
    }

    suggestionsParent.children[1]?.remove(); // susceptible to breaking on change of ul structure
    let ul = document.createElement('ul');
    suggestionsParent.append(ul);

    arrayToSuggestionsLIs(suggestions).forEach((node) => ul.appendChild(node));
    showSuggestions(suggestionsParent, searchBar);
    haveSuggestions = true;
  };

  const updateSuggestionsWeighted = async (e) => {
    const prefix = e.target.value;
    weightedSearchBar.classList.add('search-bar-active');

    if (e.target.value == '') {
      hideSuggestions(weightedSuggestionsParent, weightedSearchBar);
      haveWeightedSuggestions = false;
      return;
    }

    const response = await fetch(`${apiWeightedUri}${encodeURI(prefix)}`);
    const suffixes = await response.json();
    const suggestions = suffixes.map((suffix) => prefix + suffix);

    if (!suggestions.length) {
      hideSuggestions(weightedSuggestionsParent, weightedSearchBar);
      haveWeightedSuggestions = false;
      return;
    }

    weightedSuggestionsParent.children[1]?.remove(); // susceptible to breaking on change of ul structure
    let ul = document.createElement('ul');
    weightedSuggestionsParent.append(ul);

    arrayToSuggestionsLIs(suggestions).forEach((node) => ul.appendChild(node));
    showSuggestions(weightedSuggestionsParent, weightedSearchBar);
    haveWeightedSuggestions = true;
  };

  const updateSuggestionsCached = async (e) => {
    const prefix = e.target.value;
    cachedSearchBar.classList.add('search-bar-active');

    if (e.target.value == '') {
      hideSuggestions(cachedSuggestionsParent, cachedSearchBar);
      haveCachedSuggestions = false;
      return;
    }

    const response = await fetch(`${apiCachedUri}${encodeURI(prefix)}`);
    const suffixes = await response.json();
    const suggestions = suffixes.map((suffix) => prefix + suffix);

    if (!suggestions.length) {
      hideSuggestions(cachedSuggestionsParent, cachedSearchBar);
      haveCachedSuggestions = false;
      return;
    }

    cachedSuggestionsParent.children[1]?.remove(); // susceptible to breaking on change of ul structure
    let ul = document.createElement('ul');
    cachedSuggestionsParent.append(ul);

    arrayToSuggestionsLIs(suggestions).forEach((node) => ul.appendChild(node));
    showSuggestions(cachedSuggestionsParent, cachedSearchBar);
    haveCachedSuggestions = true;
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
  weightedInput.addEventListener(
    'input',
    debounce(this, updateSuggestionsWeighted, 150),
  );
  cachedInput.addEventListener(
    'input',
    debounce(this, updateSuggestionsCached, 150),
  );

  document.addEventListener('click', (e) => {
    const clickedInput = input.contains(e.target);
    const clickedOutsideForm = form.contains(e.target);

    if (clickedInput) {
      searchBar.classList.add('search-bar-active');
      if (haveSuggestions) {
        showSuggestions(suggestionsParent, searchBar);
      }
    } else if (!clickedOutsideForm) {
      searchBar.classList.remove('search-bar-active');
      hideSuggestions(suggestionsParent, searchBar);
    }
  });

  document.addEventListener('click', (e) => {
    const clickedInput = weightedInput.contains(e.target);
    const clickedOutsideForm = weightedForm.contains(e.target);

    if (clickedInput) {
      weightedSearchBar.classList.add('search-bar-active');
      if (haveSuggestions) {
        showSuggestions(weightedSuggestionsParent, weightedSearchBar);
      }
    } else if (!clickedOutsideForm) {
      weightedSearchBar.classList.remove('search-bar-active');
      hideSuggestions(weightedSuggestionsParent, weightedSearchBar);
    }
  });

  document.addEventListener('click', (e) => {
    const clickedInput = cachedInput.contains(e.target);
    const clickedOutsideForm = cachedForm.contains(e.target);

    if (clickedInput) {
      cachedSearchBar.classList.add('search-bar-active');
      if (haveSuggestions) {
        showSuggestions(cachedSuggestionsParent, cachedSearchBar);
      }
    } else if (!clickedOutsideForm) {
      cachedSearchBar.classList.remove('search-bar-active');
      hideSuggestions(cachedSuggestionsParent, cachedSearchBar);
    }
  });
})();
