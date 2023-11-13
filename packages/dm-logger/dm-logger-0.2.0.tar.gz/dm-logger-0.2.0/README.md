# DM-Logger

## Example

```python
from dm_logger import DMLogger

custom_logger = DMLogger("main")

custom_logger.info("test message", tag="test tag")
custom_logger.debug("new message", id=123312)
custom_logger.info("only mess")
custom_logger.critical(env="production")
custom_logger.warning({"key": "value"})
custom_logger.error(["item1", "item2", 3])
custom_logger.info()
```

## Initial parameters

```python
         name: str  # logger name (*required)
logging_level: str = "DEBUG",  # min logging level
logs_dir_path: str = "logs",  # log parent directories, leave blank to not write
   print_logs: bool = True,  # print to the console or not
    file_name: str = "",  # log file name, default = <name>.log
   write_mode: Literal["a", "w"] = "w",  # start with new file or continue old one
       max_MB: int = 5,  # max log file size (MB)
    max_count: int = 10,  # max count of saved logs
format_string: str = "%(asctime)s.%(msecs)03d [%(levelname)s] (%(module)s.%(funcName)s:%(lineno)d) %(message)s",
```
