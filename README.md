RDMO re3data plugin
===================

The dynamic re3data optionset will query [re3data.org](https://www.re3data.org/) for repositories that match the research field of the project (as given by the `project/research_field/title` attribute).

Please visit the [RDMO documentation](https://rdmo.readthedocs.io/en/latest/plugins/index.html#optionset-providers) for detailed information.


Setup
-----

Install the plugin in your RDMO virtual environment using pip (directly from GitHub):

```bash
pip install git+https://github.com/rdmorganiser/rdmo-re3data
```

Add the plugin to the `OPTIONSET_PROVIDERS` in `config/settings/local.py`:

```python
OPTIONSET_PROVIDERS = [
    ...
    ('re3data', _('Repositories from re3data'), 'rdmo_re3data.providers.Re3DataProvider')
]
```

After restarting RDMO, the `Re3DataProvider` should be selectable as a provider option for option sets.
