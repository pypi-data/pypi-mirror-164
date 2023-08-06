# STREAM SAGE PYTHON LOGGER

## Basic operation
### Logger format

```shell
[<Date> <Time>][<logLevel>][<context>][<file>:<line>] <message>
```

Date format: `YYYY-MM-DD`<br/>
Time format: `HH:mm:ss`


### Logger output

```shell
[2022-04-15 12:06:34][INFO][Sample App][samle_file.py:1] Sample INFO message
[2022-04-15 12:06:34][DEBUG][Sample App][samle_file.py:1] Sample DEBUG message
```

# Installation

Add `streamsage-python-logger` to requirements.txt 

```
streamsage-python-logger =< 0.1.0
```

or install via pip:

```shell
pip install streamsage-python-logger
```

# Environment Variables 

| Variable      | Description        | Default         | Supported  |
|---------------|--------------------|-----------------|------------|
| `APP_CONTEXT` | Logger context     | `NoContextApp`  | `str`      |
| `TRANSPORTS`  | List of transports | -               | `fluent`   |


### **Logger parameters and configuration:**

### Optional:

- `context` - The context of logger instance. Can be specified via environment variables or the context parameter in the get_logger method

### Levels:

**Logging levels table**

| Level    | Numeric value      |
|----------|--------------------|
| CRITICAL | 50                 |
| ERROR    | 40                 |
| WARNING  | 30                 |
| INFO     | 20                 |
| DEBUG    | 10                 |
| TRACE    | 1                  |
| NOTSET   | 0                  |

**Default: `info`**
  Then, you can use following methods `log()`, `fatal()`, `error()`, `warning()`, `info()`, `debug()`, `trace()`:
- `log()` - displays message in given log level.
- `fatal()` - displays message in `critical` log level.
- `error()` - displays message in `error` log level.
- `warning()` - displays message in `warning` log level.
- `info()` - displays message in `info` log level.
- `debug()` - displays message in `debug` log level.
- `trace()` - displays message in `trace` log level.



## Available transports

Description of all currently supported transport by the Logger.

### Console

> **Notice:** Console transport is always enabled.

| Variable                    | Description                | Default | Supported                                             |
|-----------------------------|----------------------------|---------|-------------------------------------------------------|
| `LOG_SDK_TRANSPORT_CONSOLE_LEVEL`   | Logging level to console   | `INFO`  | `FATAL`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, `TRACE` |

### Fluent

| Variable                                | Description                                      | Default | Supported                                             |
|-----------------------------------------| ------------------------------------------------ |---------|-------------------------------------------------------|
| `LOG_SDK_TRANSPORT_FLUENT_LEVEL`                | Logging level to FluentD                         | `INFO`  | `FATAL`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, `TRACE` |
| `LOG_SDK_TRANSPORT_FLUENT_URL`                  | URL of the FluentD server                        | -       | -                                                     |
| `LOG_SDK_TRANSPORT_FLUENT_TIMEOUT`              | Timeout for response from the FluentD server.    | `3.0`   | -                                                     |

# Logger sample usage

Logger can be initialized by `get_logger()` method:
```python
from streamsage_python_logger.streamsage_logger import get_logger

logger = get_logger(context='SomeApp')

logger.trace('Something has happened to log on TRACE level')
logger.debug('Something has happened to log on DEBUG level')
logger.info('Something has happened to log on INFO level')
logger.warning('Something has happened to log on DEBUG level')
logger.error('Something has happened to log on ERROR level')
logger.fatal('Something has happened to log on FATAL level')

logger.log(10, 'Something has happened to log on 10 level')
```
output:
```shell
[2022-08-17 11:50:29][TRACE][SomeApp][workshop.py:8] Something has happened to log on TRACE level
[2022-08-17 11:50:29][DEBUG][SomeApp][workshop.py:9] Something has happened to log on DEBUG level
[2022-08-17 11:50:29][INFO][SomeApp][workshop.py:10] Something has happened to log on INFO level
[2022-08-17 11:50:29][WARNING][SomeApp][workshop.py:11] Something has happened to log on DEBUG level
[2022-08-17 11:50:29][ERROR][SomeApp][workshop.py:12] Something has happened to log on ERROR level
[2022-08-17 11:50:29][CRITICAL][SomeApp][workshop.py:13] Something has happened to log on FATAL level
[2022-08-17 11:50:29][DEBUG][SomeApp][workshop.py:15] Something has happened to log on 10 level
```

for implementing logger with other libraries use `LoggerConfig` class with logging `dictConfig` e.g. on FastApi and uvicorn server:

```python
import uvicorn
from fastapi import FastAPI
from logging.config import dictConfig
from streamsage_python_logger.streamsage_logger import LoggerConfig

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080,
                access_log=False,
                log_config=dictConfig(LoggerConfig().dict()),
                log_level='info')
```
output:
```shell
SomeFlaskApp  | [2022-08-21 20:49:50][INFO][uvicorn.error][server.py:75] Started server process [11]
SomeFlaskApp  | [2022-08-21 20:49:50][INFO][uvicorn.error][on.py:45] Waiting for application startup.
SomeFlaskApp  | [2022-08-21 20:49:50][INFO][uvicorn.error][on.py:59] Application startup complete.
SomeFlaskApp  | [2022-08-21 20:49:50][INFO][uvicorn.error][server.py:206] Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)

```
