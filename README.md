# Static Web Projects

A collection of small, static front-end learning projects and experiments. The repository intentionally keeps multiple related exercises together; each project remains in its own folder.

## Project catalog

### HTML 5 & CSS 3

- **Assertively Maintaining Compassionate Warm Supporting Tender Affirm Vindication** — standalone HTML/CSS page.
- **Bootstrap 4**
  - **Elena Sarah Mattia (aka Lori)** — standalone Bootstrap page.
  - **Full Stack Conf** — responsive conference landing-page exercise with local images and custom CSS.
- **Car Sounds** — interactive car-sound demo with local images and audio assets.
- **Lake-Tahoe-Website** — Lake Tahoe layout and styling exercise.
- **Typography** — typography-focused HTML/CSS exercise.
- **Lift Louisiana** — Git submodule reference; its source is maintained in the separate Lift Louisiana repository.

### Sass

- **Blog** — starter and finished Sass/CSS versions.
- **Color Pallet** — Sass variables, partials, and color-palette exercise.
- **Mixins** — Sass mixin exercise.
- **Test** — small Sass/CSS test files.

## Working with the projects

Most exercises are static and can be previewed by opening their `index.html` file in a browser. Some folders use a named HTML entry point instead. The Sass exercises include both `.scss` source and compiled `.css` output; edit the Sass source and recompile when changing those examples.

No repository-wide build system is currently defined. Work from the individual project folder and retain its local asset paths.

## Repository hygiene

Generated operating-system metadata such as `.DS_Store` and editor artifacts should not be committed. Existing historical files and project assets are retained; this catalog does not remove or relocate them.


## Quality checks

Run the dependency-free static archive checks from the repository root:

```bash
python -m unittest discover -s tests -v
```

The workflow validates document language/title, image alternative text, stable local asset references, and the absence of tracked macOS metadata. The older Elena/Lori photo exercise is excluded from local-asset checks because its referenced media is not present in the repository; restore those files only from an authorized source and review consent/usage rights first.

## Security

See [SECURITY.md](SECURITY.md) for this repository's security, privacy, and responsible-use guidance.


## Personal-media archive boundary

A historical photo-exercise page has been reduced to a noindex, text-only archive notice because its original media is absent and publication rights/consent are not documented. Do not add substitute or recovered personal imagery unless the original source, publication rights, and explicit consent from the people depicted are confirmed.
