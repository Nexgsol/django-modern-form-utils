Contributing
============

Thank you for considering a contribution to **modern-form-utils**!  
Contributions of code, documentation, and tests are always welcome and appreciated.

Submitting Issues
-----------------

If you discover a bug or unexpected behavior, please:

- Check if the issue already exists in the [GitHub Issues](https://github.com/yourusername/modern-form-utils/issues)
- Provide a clear and concise description of the problem
- Include a minimal reproducible example of the issue
- Include the relevant stack trace or error message (if applicable)
- Mention your Python and Django versions

Bonus: Submit a failing test case that demonstrates the issue via a pull request!

Pull Requests
-------------

When submitting a pull request:

- Ensure your code is **PEP8-compliant**
- Add **tests** for new features or bug fixes
- Update the **README.rst** if behavior or usage changes
- Document changes in the **CHANGES.rst**
- Add yourself to the **AUTHORS.rst**
- Ensure all tests pass locally before submitting the PR

Pull requests should be created against the `main` branch.

Project Structure
-----------------

- Core Code: `modern_form_utils/`
- Tests: `tests/`
- Templates: `modern_form_utils/templates/`
- JavaScript: `modern_form_utils/media/`

Testing
-------

To run the test suite:

```bash
python tests/runtests.py
```

Or use `tox` to run tests against all supported Python and Django versions:

```bash
pip install tox
tox
```

Supported test environments include:

- Python 3.8 – 3.12
- Django 3.2, 4.2, 5.0+

Tox will automatically detect which Python versions are available on your machine and run only those environments. Full test coverage across all environments is required before merging pull requests.

Continuous Integration
----------------------

If you're contributing frequently, consider setting up pre-commit hooks or using GitHub Actions locally to match our CI testing matrix.

Code Style
----------

Follow these guidelines for code consistency:

- Use `black` or `ruff` (recommended) for formatting
- Keep code backward-compatible with Django 3.2+
- Use modern Python 3.8+ features, but avoid breaking compatibility with lower-supported versions

Releases
--------

Maintainers will handle PyPI publishing and version tagging.  
Please do not manually bump versions in `setup.cfg` or `pyproject.toml`.

Feedback & Community
---------------------

We're open to feedback, ideas, and improvements. Feel free to:

- Open a GitHub Issue
- Submit an Enhancement Proposal (as a PR or issue)
- Share your use-case for advanced form rendering patterns

Thanks for contributing!

– Maintainers of `modern-form-utils`