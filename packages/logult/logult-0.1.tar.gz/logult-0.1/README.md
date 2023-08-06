# logger_rewrite
Easy way to log everything
### Install
```bash
pip install logult
```

### Use
```
from logult import setup_log
logger=  setup_log(save_dir='saved', name_exp='info.log')
logger.info('Hello')
```
