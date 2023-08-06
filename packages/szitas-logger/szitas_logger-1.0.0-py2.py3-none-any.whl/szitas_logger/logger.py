# -*- coding: utf-8 -*-
"""
Features:
 - disabling empty records based on msg both in std out and logfile
 - multi-line messages with the same format

Usage:
inherit your class from Logger and initialize it within class __init__() as
Logger.__init__(self)
"""

__author__ = 'gabor.szitas.work@gmail.com'

import datetime
import logging
import os
import re
import sys
import traceback


class Logger(object):

    class Formatter(logging.Formatter):

        def __init__(self, fmt):
            super(Logger.Formatter, self).__init__(fmt)

        # Enabling multi-line logging
        def format(self, record):
            formatted_records = list()

            record.asctime = self.formatTime(record, self.datefmt)
            record.message = record.getMessage()

            first_line = True
            for message in Logger.split('\r|\n', record.message):
                message = message.lstrip(' ')

                if message != '':
                    record.message = message if first_line else \
                        Logger.indent_message(message)
                    formatted_records.append(self._fmt % record.__dict__)

                if first_line:
                    first_line = False

            return '\n'.join(formatted_records)

    class StreamHandler(logging.StreamHandler):

        def __init__(self, stream=None):
            super(Logger.StreamHandler, self).__init__(stream)

        # Disabling empty records based on msg
        def emit(self, record):
            if record.msg and record.msg != '' and record.msg != 'None':
                super(Logger.StreamHandler, self).emit(record)

    class FileHandler(logging.FileHandler):

        def __init__(self, filename, mode='a', encoding=None, delay=0):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            super(Logger.FileHandler, self).__init__(filename,
                                                     mode,
                                                     encoding,
                                                     delay)

        # Disabling empty records based on msg
        def emit(self, record):
            if record.msg and record.msg != '' and record.msg != 'None':
                super(Logger.FileHandler, self).emit(record)

    def __init__(self,
                 log_file='logger.log',
                 log_file_mode='w',
                 log_logfile_format='%(asctime)s [%(module)-10.10s] '
                                    '[%(levelname)-7.7s] %(message)s',
                 log_std_out_format='%(module)s %(message)s',
                 log_level=logging.INFO):
        self.log_file = log_file
        self.log_file_mode = log_file_mode
        self.log_file_path = os.path.dirname(self.log_file)
        self.log_logfile_format = log_logfile_format
        self.log_std_out_format = log_std_out_format
        self.log_level = log_level

        self.log = Logger.get_logger()
        self.log.timer_start = self.log_timer_start
        self.log.timer_end = self.log_timer_end
        self.start_time = None
        self.stop_time = None

        # prevent to create multiple handlers
        if not self.log.handlers:
            # this should be always DEBUG
            self.log.setLevel(logging.DEBUG)
            self.__set_handlers()

    def log_timer_start(self):
        self.start_time = datetime.datetime.utcnow()
        self.log.debug('Timer start')

    def log_timer_end(self):
        stop_time = datetime.datetime.utcnow()
        if self.start_time and self.log:
            self.log.debug('Timer end')
            self.log.info(f'Elapsed time {stop_time - self.start_time}')
        self.start_time = None

    def __set_handlers(self):
        fh = Logger.FileHandler(self.log_file, mode=self.log_file_mode)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(Logger.Formatter(self.log_logfile_format))

        ch = Logger.StreamHandler()
        ch.setLevel(self.log_level)
        ch.setFormatter(Logger.Formatter(self.log_std_out_format))

        self.log.addHandler(fh)
        self.log.addHandler(ch)

        self.log.debug(f'Logger initialized with log_level='
                       f'{logging.getLevelName(self.log_level)} for std_out')

        # Force to use our exception logging
        sys.excepthook = Logger.log_exception

    def reset_handlers(self):
        handlers = self.log.handlers[:]

        self.log.debug(f'Reset handlers {handlers}')

        for handler in handlers:
            handler.close()
            self.log.removeHandler(handler)

        self.__set_handlers()

    @staticmethod
    def indent_message(message):
        return f'\t{message}'.expandtabs(3)

    @staticmethod
    def split(separator, string):
        return filter(bool, re.split(separator, str(string)))

    @staticmethod
    def get_logger(name=__name__):
        return logging.getLogger(name)

    @staticmethod
    def log_exception(exception_type, exception, trace):
        log = Logger.get_logger()
        trace = ''.join(traceback.format_tb(trace))\
                .replace('    ', '\t').replace('  ', '')

        if exception_type.__name__ == 'KeyboardInterrupt':
            log.exception('{}: execution interrupted by end-user'
                          .format(exception_type.__name__))
            sys.exit(2)
        else:
            if exception_type.__name__ != 'Base':
                exception = f'{exception_type.__name__}: {exception}'

            log.exception(exception)
            log.exception(f'Traceback (most recent call last):\n{trace}')
