const $ = require('jquery');
const { main, getSuggestions } = require('../../app/static/script');

describe('main', () => {
  describe('search bar', () => {
    test('has event listener that adds search-bar-active class on click', () => {
      document.body.innerHTML = dom;
      main();
      $('#trie-search-bar').trigger('click');
      expect($('#trie-search-bar').hasClass('search-bar-active')).toEqual(true);
    });
  });
});

describe('getSuggestions', () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve(['p', 'ple', 'ple orchard']),
    }),
  );

  beforeEach(() => {
    fetch.mockClear();
  });

  test('returns a prefix + suffix combo', async () => {
    const suggestions = await getSuggestions('ap', 'uri');
    expect(suggestions).toEqual(['app', 'apple', 'apple orchard']);
    expect(fetch).toHaveBeenCalledTimes(1);
  });

  test('returns empty array with exception', async () => {
    fetch.mockImplementationOnce(() => Promise.reject('API is down'));
    const suggestions = await getSuggestions('ap', 'uri');
    expect(suggestions).toEqual([]);
    expect(fetch).toHaveBeenCalledTimes(1);
  });
});

var dom = `
<body>
    <header><h1>Implementing Search Suggestions with a Trie</h1></header>
    <section>
      <h2>Introduction</h2>
      <div>
        <p>
          Selecting an...
      </div>
      <div class="search-container">
        <form id="trie-form">
          <div id="trie-search-bar" class="search-bar">
            <input
              id="search-input"
              class="search"
              maxlength="2048"
              type="text"
              name="search"
              autocapitalize="off"
              autocomplete="off"
              autocorrect="off"
              autofocus
              spellcheck="false"
              title="Search"
              value=""
            />
          </div>
          <div id="suggestions" class="auto-complete" hidden>
            <div class="auto-line"></div>
          </div>
        </form>
        <figcaption>
          Try me! (<b>Warning:</b> Some suggestions are NSFW)
        </figcaption>
      </div>
      <p>
        This implementation...
      </p>
      <p>
        The Trie ...
      </p>
    </section>
  </body>
`;
