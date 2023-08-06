# Iseq meta

A bunch of scripts to operate on iseq meta

More info here: https://workflows-dev-documentation.readthedocs.io/en/latest/index.html

# Install

Optional steps (create virtual environment):
```
python3 -m venv venv
source venv/bin/activate
```


Obligatory steps:
```
python3 -m pip install --upgrade pip
pip install iseqmetatools
```



# Parsing google spreadsheet to meta

You can parse inputs, outputs or workflows parameters for the workflow.
Example use for workflows parameters (after installing):

```
parse_inputs \
  --workflow-name "germline" \
  --credentials "/path/to/credentials.json" \
  --meta-json "/path/to/wdl/meta.json" \
  --spreadsheet-key "key" \
  --output-meta-json "/path/to/output/meta.json"
```

```
parse_outputs \
  --workflow-name "germline" \
  --credentials "/path/to/credentials.json" \
  --meta-json "/path/to/wdl/meta.json" \
  --spreadsheet-key "key" \
  --output-meta-json "/path/to/output/meta.json"
```

```
parse_workflows \
  --workflow-name "germline" \
  --credentials "/path/to/credentials.json" \
  --meta-json "/path/to/wdl/meta.json" \
  --spreadsheet-key "key" \
  --output-meta-json "/path/to/output/meta.json"
```

More info here:
https://workflows-dev-documentation.readthedocs.io/en/latest/Developer%20tools.html#parsing-google-spreadsheet-to-meta