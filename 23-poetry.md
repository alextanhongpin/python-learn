# Poetry

Prefer this over pipenv or virtualenv.



## VSCode can't detect Poetry virtualenv in Jupyterlab

```
$ poetry config virtualenvs.in-project true
```


If you already have created your project, you need to re-create the virtualenv to make it appear in the correct place:

```
poetry env list  # shows the name of the current environment
poetry env remove <current environment>
poetry install  # will create a new environment using your updated configuration
embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")
```

## Switching Python version

Use python 3.9:

```bash
$ poetry env use 3.9
```
