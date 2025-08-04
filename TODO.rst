modern-form-utils TODO
=======================

General Cleanup
~~~~~~~~~~~~~~~

- ✅ Update all code to Python 3.8+ syntax (no more `__future__` or `six`).
- ✅ Refactor deprecated imports (e.g. `MIDDLEWARE_CLASSES`, `render_to_string`).
- ✅ Ensure compatibility with Django 4.x and 5.x.
- ✅ Rename template paths and tags from `form_utils` to `modern_form_utils`.
- ✅ Move JS files under modern naming convention.

ClearableFileField Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Django special-cases `FileField` in `BaseForm._clean_fields` and `BoundField.as_widget()`:

- This causes inconsistencies when redisplaying `ClearableFileField`, which is based on `MultiValueField`.
- Unlike `FileField`, it doesn't retain its value on bound redisplay because the initial data is not re-injected.

🛠 Possible Workarounds:
- Add explicit initial-data handling to `ClearableFileField`'s widget.
- Patch Django internals via mixin or monkey-patch (not ideal).
- Accept this as a known behavior with a documented warning.

Future Enhancements
~~~~~~~~~~~~~~~~~~~

- ⏳ Support for async form rendering (for upcoming Django features).
- ⏳ Rewrite `autosize.js` to avoid jQuery dependency (move to vanilla JS or Alpine).
- ⏳ Add Tailwind-compatible form template variants.
- ⏳ Optional support for HTMX integration on dynamic forms.
- ⏳ Add Sphinx docs and publish to ReadTheDocs.

Tests
~~~~~

- ✅ Add tests for `BetterForm`, `fieldsets`, and `row_attrs`.
- ✅ Add test coverage for `ClearableFileField`, `ImageWidget`, `AutoResizeTextarea`.
- ⏳ Add Django admin integration tests using `AdminSite`.
- ⏳ Integrate GitHub Actions for CI testing across Django/Python versions.

Packaging
~~~~~~~~~

- ✅ Prepare for PyPI release as `modern-form-utils`.
- ✅ Add README, LICENSE, and long description for PyPI.
- ⏳ Create `setup.cfg` and/or `pyproject.toml`.
- ⏳ Add wheel and source distribution scripts.

