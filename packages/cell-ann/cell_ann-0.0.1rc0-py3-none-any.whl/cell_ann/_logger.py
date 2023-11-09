
import ABCParse
import logging
import pathlib
import os

from typing import Union, Optional


class Logger(ABCParse.ABCParse):
    def __init__(
        self,
        name: Optional[Union[str, None]] = "cell-ann-logger",
        wd: Union[pathlib.Path, str] = pathlib.Path(os.getcwd()),
        log_dir: Optional[Union[pathlib.Path, str]] = None,
        level: int = logging.DEBUG,
        format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        *args,
        **kwargs
    ):
        """"""

        self.__parse__(locals())
        self._configure_logging()

    @property
    def _WD(self):
        if not isinstance(self._wd, pathlib.Path):
            self._wd = pathlib.Path(self._wd)
        return self._wd
    
    @property
    def _LOG_DIR(self):
        if not hasattr(self, "_log_dir") or (self._log_dir is None):
            self._log_dir = self._WD.joinpath("logs")
        if not self._log_dir.exists():
            self._log_dir.mkdir()
        return self._log_dir

    @property
    def _BASIC_LOG_PATH(self):
        return self._LOG_DIR.joinpath("cell_ann.log")
    
    @property
    def _EXISTING_LOG_PATHS(self):
        return list(self._BASIC_LOG_PATH.parent.glob("cell_ann*log"))
    
    @property
    def _N_LOGS(self):
        return len(self._EXISTING_LOG_PATHS)
    
    @property
    def _LOG_PATH(self):
        return self._BASIC_LOG_PATH.parent.joinpath(f"cell_ann.{self._N_LOGS}.log")

    def _configure_logging(self):
        logging.basicConfig(
            filename=self._LOG_PATH,
            filemode="a",
            level=self._level,
            format=self._format,
        )
        # disable logging from nb_black
        for logger_key in ['h5py', 'blib2to3']:
            logging.getLogger(logger_key).setLevel(logging.ERROR)

    @property
    def logger(self):
        if not hasattr(self, "_logger"):
            self._logger = logging.getLogger(self._name)
        return self._logger

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
