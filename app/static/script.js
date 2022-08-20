(() => {
  // swap these for testing
  const baseUri = 'http://mrhaffner.pythonanywhere.com/api/';
  // const baseUri = 'http://127.0.0.1:5000/api/';

  class SearchBar {
    constructor(inputId, suggestionsId, searchId, formId, uri) {
      this.input = document.getElementById(inputId);
      this.suggestionsParent = document.getElementById(suggestionsId);
      this.searchBar = document.getElementById(searchId);
      this.form = document.getElementById(formId);
      this.uri = uri;
      this.haveSuggestions = false;
      this.input.addEventListener(
        'input',
        debounce(this, this.updateSuggestions, 150),
      );
      document.addEventListener('click', this.handleClick.bind(this));
    }

    async updateSuggestions(e) {
      const prefix = e.target.value;
      this.searchBar.classList.add('search-bar-active');

      if (e.target.value == '') {
        this.hideSuggestions();
        this.haveSuggestions = false;
        return;
      }

      const response = await fetch(`${this.uri}${encodeURI(prefix)}`);
      const suffixes = await response.json();
      const suggestions = suffixes.map((suffix) => prefix + suffix);

      if (!suggestions.length) {
        this.hideSuggestions();
        this.haveSuggestions = false;
        return;
      }

      this.suggestionsParent.children[1]?.remove();
      let ul = document.createElement('ul');
      this.suggestionsParent.append(ul);

      SearchBar.arrayToSuggestionsLIs(suggestions).forEach((node) =>
        ul.appendChild(node),
      );
      this.showSuggestions();
      this.haveSuggestions = true;
    }

    hideSuggestions() {
      this.suggestionsParent.hidden = true;
      this.searchBar.classList.remove('search-bar-suggestions');
    }

    showSuggestions() {
      this.searchBar.classList.add('search-bar-suggestions');
      this.suggestionsParent.hidden = false;
    }

    handleClick(e) {
      const clickedInput = this.input.contains(e.target);
      const clickedOutsideForm = this.form.contains(e.target);
      if (clickedInput) {
        this.searchBar.classList.add('search-bar-active');
        if (this.haveSuggestions) {
          this.showSuggestions();
        }
      } else if (!clickedOutsideForm) {
        this.searchBar.classList.remove('search-bar-active');
        this.hideSuggestions();
      }
    }

    static arrayToSuggestionsLIs(suggestions) {
      return suggestions.map((suggestion) => {
        let li = document.createElement('li');
        li.textContent = suggestion;
        li.className = 'suggestion';
        return li;
      });
    }
  }

  let standard = new SearchBar(
    'search-input',
    'suggestions',
    'trie-search-bar',
    'trie-form',
    baseUri + 'trie/suggestions?limit=10&prefix=',
  );

  let weighted = new SearchBar(
    'weighted-search-input',
    'weighted-suggestions',
    'trie-weighted-search-bar',
    'trie-weighted-form',
    baseUri + 'weighted-trie/suggestions?limit=10&prefix=',
  );

  let cached = new SearchBar(
    'cached-search-input',
    'cached-suggestions',
    'trie-cached-search-bar',
    'trie-cached-form',
    baseUri + 'cached-trie/suggestions?limit=10&prefix=',
  );

  /**
   * @param {*} ctx The context
   * @param {function} func The function to execute after the debounce time
   * @param {number} delay The amount of time to wait
   * @return {function} The debounced function
   * @note From https://chiamakaikeanyi.dev/event-debouncing-and-throttling-in-javascript/
   */
  function debounce(context, func, delay) {
    ////
    let timeout;

    return (...arguments) => {
      if (timeout) {
        clearTimeout(timeout);
      }

      timeout = setTimeout(() => {
        func.apply(context, arguments);
      }, delay);
    };
  }
})();
