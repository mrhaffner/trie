const $ = require('jquery');

('use strict');

const testUri = 'http://127.0.0.1:5000/api/trie/suggestions?prefix=';

main();

function main() {
  $('#trie-search-bar').on('click', () => {
    $('#trie-search-bar').addClass('search-bar-active');
  });

  // $('#search-input').on('input', () => {});
}

// test that main is called?

async function getSuggestions(prefix, uri) {
  try {
    const response = await fetch(`${uri}${encodeURI(prefix)}`);
    const suffixes = await response.json();
    return suffixes.map((suffix) => prefix + suffix);
  } catch (e) {
    console.error(e, e.stack);
    return [];
  }
}

module.exports = { getSuggestions, main };
