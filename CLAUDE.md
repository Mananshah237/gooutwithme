# CLAUDE.md

Guidance for Claude Code (and other AI assistants) working in this repository.

## What this is

`gooutwithme` is a single-page, dependency-free static web page: a joke "Will you
go out with me?" prompt where the **Yes** button accepts and the **No** button
runs away from the cursor. That is the entire product — there is no backend, no
build step, no package manager, and no test suite.

Repository: https://github.com/Mananshah237/gooutwithme

## Layout

```
index.html    Whole page markup: heading, GIF, and the Yes/No button group
script.js     All behavior: Yes-click handler and No-button evade handler
style.css     All styling: centered flex body, button shapes, colors
```

There are no other directories, config files, CI workflows, or lockfiles. If you
find yourself adding a `package.json`, a bundler, or a framework, stop and
confirm with the user first — that would be a change of kind, not of degree.

## How the pieces connect

`index.html` is the only entry point. It links `style.css` in `<head>` and loads
`script.js` with a plain `<script>` tag at the end of `<body>` (no `defer`/
`type=module`), which is why the script can query the DOM at top level without
waiting for `DOMContentLoaded`.

The three files are coupled entirely through **CSS class names**. `script.js`
grabs elements with `document.querySelector` on `.wrapper`, `.question`, `.gif`,
`.yes-btn`, and `.no-btn`. Renaming or removing any of those classes in
`index.html` silently breaks the JS (`querySelector` returns `null` and the
`addEventListener` call throws). Always update markup and script together.

### Behavior in `script.js`

- **Yes** (`click`): rewrites `.question`'s `innerHTML` to the acceptance
  message and swaps `.gif`'s `src` to a celebratory Giphy URL.
- **No** (`mouseover`): computes a random `(x, y)` inside the viewport bounds
  (`window.innerWidth/innerHeight` minus the button's own size via
  `getBoundingClientRect()`) and assigns it to `noBtn.style.left/top`, so the
  button jumps away before it can be clicked. There is deliberately no `click`
  handler on **No**.

### Styling quirks worth knowing before you edit `style.css`

- Both buttons are `position: absolute` with no positioned ancestor, so they are
  laid out against the initial containing block (the viewport). This is what
  makes the inline `left`/`top` writes in `script.js` work as viewport
  coordinates.
- Because of that, `.btn-group`'s flex centering does **not** position the
  buttons; the initial side-by-side look comes from the negative
  `margin-left: -200px` / `margin-right: -200px` on `button:nth-child(1)` and
  `:nth-child(2)`. Those margins keep applying after the No button moves, so its
  `left` value is offset by `-200px`. Keep that in mind if you touch either the
  margins or the random-position math — they are two halves of the same layout.
- Buttons are selected by `:nth-child`, not by `.yes-btn` / `.no-btn`. Reordering
  the buttons in `index.html` swaps their colors.
- `.gif` is `height: 100%; width: 100%`, so the image stretches to whatever box
  it is in rather than preserving its aspect ratio.
- `.wrapper` is queried in `script.js` but never used; harmless, but do not
  assume it is load-bearing.

Images are hot-linked from `media.giphy.com`. Nothing is vendored locally, so
the page needs network access to render its GIFs.

## Running it

There is nothing to install or build. Either open `index.html` directly in a
browser, or serve the directory so relative paths behave exactly as in
production:

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

Verification is manual and visual: load the page, hover the **No** button and
confirm it moves without leaving the viewport, click **Yes** and confirm both
the heading text and the GIF swap. Check at a narrow width too — the absolute
positioning and fixed `150px` button width are not responsive, so regressions
show up on small screens first.

## Deployment

The site is published with **GitHub Pages** from the default branch (`main`).
History shows a `CNAME` file being added and removed more than once for a custom
domain; there is no `CNAME` in the tree today, so the site serves from the
default `github.io` URL. If you add a `CNAME` back, it must sit at the
repository root and contain the bare domain on one line — and the user must set
the matching DNS records, which is outside this repo.

There is no CI: a push to `main` is a deploy. Treat every change to `main` as
user-visible immediately.

## Conventions

- **Vanilla only.** No frameworks, no libraries, no build tooling. Match the
  existing plain-DOM, `querySelector`-plus-`addEventListener` style.
- **Formatting.** `script.js` uses 2-space indentation and double-quoted
  strings; `index.html` and `style.css` use 4 spaces. Follow whichever file you
  are editing rather than reformatting across the repo.
- **Keep it three files.** New behavior belongs in `script.js`, new styling in
  `style.css`. Don't introduce inline `<style>` or `<script>` blocks in
  `index.html`.
- **Copy is personal.** The heading and the Yes-response message are the user's
  own words (currently mentioning "Froyo on monday"). Do not rewrite, polish, or
  "fix" that wording unless asked — including the typo currently in the heading
  (`wisdfsdfth`), which should be corrected only on request.

## Git workflow

Most existing commits were made through the GitHub web editor, hence the terse
`Update script.js` messages. When committing from a session, write a descriptive
message instead.

Work on a feature branch and push with `git push -u origin <branch-name>`; do not
commit straight to `main` unless the user asks. Open a pull request only when the
user explicitly requests one.
