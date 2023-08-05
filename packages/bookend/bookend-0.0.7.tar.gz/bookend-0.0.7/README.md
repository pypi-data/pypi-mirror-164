bookend
=======

A program to keep track of one's books

### usage from pizzimathy/bookend (not integrated yet)

`$ bookend [-a | --add]`
Prompts for a new book to be added to the list.

`$ bookend [-l | --list]`
Prettyprints a list of all the books currently in the list.

`$ bookend [-c | --checkout] <title>`
Specify the title of a book, and it'll be removed from the list.

`$ bookend [-s | --search] <term>`
Searches the list of books for a string matching the term provided.


### checklist from pizzimathy/bookend

- [ ] close-match string searching
- [ ] faster string searching
- [ ] create queryable server to store lists remotely
- [x] case-ins

### License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
```

The project contains code (c) 2016 Anthony Pizzimenti
under The MIT License (MIT).

# Acknowledgements

- This project is an independent continuation of
  [pizzimathy/bookend](https://github.com/pizzimathy/bookend),
  which was the previous codebase for the "bookend" package on PyPI.
  On 2022-08-19, that repo was duplicated in order to preserve
  the contribution entries of its author,
  [Anthony Pizzimenti](https://github.com/pizzimathy).
