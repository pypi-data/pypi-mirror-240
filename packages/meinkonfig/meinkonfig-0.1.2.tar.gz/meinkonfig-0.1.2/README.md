### Usage example

You can use .env $ENVVARIABLE variables in a YAML file.
They will be automatically replaced with environment variables.

```python
from meinkonfig import Konfig

cfg = Konfig("configfiles/", "config.yaml")
cfg.load_konfig()
print(cfg.config.env)
```
Output:
```python
ENVTEST
```

YAML configuration file:
```yaml
env: $TEST
```
.env file:
```shell
TEST="ENVTEST"
```
