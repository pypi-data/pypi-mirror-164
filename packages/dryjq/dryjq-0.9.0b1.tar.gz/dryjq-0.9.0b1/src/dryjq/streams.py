# -*- coding: utf-8 -*-

"""

dryjq.streams

Stream and file handlers

Copyright (C) 2022 Rainer Schwarzbach

This file is part of dryjq.

dryjq is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

dryjq is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import json
import logging
import sys

try:
    import fcntl
except ModuleNotFoundError:
    ...
#

from typing import Any, IO, Optional, Type

import yaml

import dryjq

from dryjq import access


class StreamHandler:

    """YAML or JSON stream reader and data handler"""

    def __init__(self, stream_io: IO) -> None:
        """Read all data from the stream"""
        contents = stream_io.read()
        logging.info("----- Finished reading data")
        try:
            self.__filtered_data = json.loads(contents)
        except json.JSONDecodeError:
            self.__filtered_data = yaml.safe_load(contents)
            self.__input_format = dryjq.FORMAT_YAML
        else:
            self.__input_format = dryjq.FORMAT_JSON
        #
        self.__original_contents = contents
        self.__modified_contents = contents
        self.__changed_format = False
        self.__stream_io = stream_io

    @property
    def stream_io(self) -> IO:
        """Return the stream handle"""
        return self.__stream_io

    @property
    def modified_contents(self) -> str:
        """Return the modified contents"""
        return self.__modified_contents

    @property
    def original_contents(self) -> str:
        """Return the original contents"""
        return self.__original_contents

    @property
    def changed_format(self) -> bool:
        """Return True if the format changed"""
        return self.__changed_format

    def dump_data(
        self,
        output_format: Optional[str] = dryjq.FORMAT_INPUT,
        indent: int = dryjq.DEFAULT_INDENT,
        sort_keys: bool = False,
    ) -> None:
        """Fill modified_contents
        with a dump of self.__filtered_data
        """
        if output_format == dryjq.FORMAT_INPUT:
            output_format = self.__input_format
        elif output_format == dryjq.FORMAT_TOGGLE:
            output_format = dryjq.SUPPORTED_FORMATS[
                1 - dryjq.SUPPORTED_FORMATS.index(self.__input_format)
            ]
        #
        if output_format != self.__input_format:
            self.__changed_format = True
        #
        if output_format == dryjq.FORMAT_JSON:
            output = json.dumps(
                self.__filtered_data,
                indent=indent,
                ensure_ascii=True,
                sort_keys=sort_keys,
            )
        else:
            output = yaml.safe_dump(
                self.__filtered_data,
                allow_unicode=True,
                default_flow_style=False,
                indent=indent,
                sort_keys=sort_keys,
                explicit_end=False,
            )
            if not isinstance(
                self.__filtered_data, (dict, list)
            ) and output.rstrip().endswith("\n..."):
                output = output.rstrip()[:-3]
            #
        #
        self.__modified_contents = output

    def execute_single_query(
        self,
        access_path: access.Path,
    ) -> None:
        """Apply the provided path to self.__filtered_data"""
        logging.debug("Filtered data before executing the query:")
        logging.debug("%r", self.__filtered_data)
        self.__filtered_data = access_path.apply_to(self.__filtered_data)
        logging.debug("Filtered data after executing the query:")
        logging.debug("%r", self.__filtered_data)

    def write_output(self) -> None:
        """Write output to stdout"""
        output = self.modified_contents.rstrip()
        sys.stdout.write(f"{output}\n")


class FileReader(StreamHandler):

    """File reader"""

    def __init__(self, stream_io: IO) -> None:
        """Go to the first byte in the file,
        then act as a normal StreamReader instance
        """
        stream_io.seek(0)
        super().__init__(stream_io)


class FileWriter(FileReader):

    """File writer
    Required locking can be done using the FileHelper class.
    """

    def write_output(self) -> None:
        """Write output to the file if data has changed
        and the format did not change
        """
        not_writing = "Not writing file:"
        if self.modified_contents == self.original_contents:
            logging.error("%s contents did not change.", not_writing)
            return
        #
        if self.changed_format:
            logging.error("%s data format changed.", not_writing)
            return
        #
        self.stream_io.seek(0)
        self.stream_io.truncate(0)
        self.stream_io.write(self.modified_contents)


class FileHelper:

    """File handling helper class"""

    no_lock_operation = 0

    def __init__(
        self,
        file_name: Optional[str],
        modify_in_place: bool = False,
        replace_mode: bool = False,
    ) -> None:
        """Determine whether the file should be opened in r
        in r or r+ mode, then return a tuple containing
        the file handler class, the open mode for the file
        and the lock and unlock operation magic numbers
        """
        if file_name is None:
            raise ValueError("No file name supplied!")
        #
        self.file_name = file_name
        exclusive_lock = self.no_lock_operation
        shared_lock = self.no_lock_operation
        unlock_operation = self.no_lock_operation
        try:
            exclusive_lock = fcntl.LOCK_EX
        except NameError:
            logging.warning(
                "File locking/unlocking using fcntl not avaliable on %s.",
                sys.platform,
            )
        else:
            shared_lock = fcntl.LOCK_SH
            unlock_operation = fcntl.LOCK_UN
        #
        self.lock_operation = shared_lock
        self.unlock_operation = unlock_operation
        self.handler_class: Type[StreamHandler] = FileReader
        self.open_mode = "r"
        if modify_in_place and replace_mode:
            self.lock_operation = exclusive_lock
            self.handler_class = FileWriter
            self.open_mode = "r+"
        #

    def open(self, encoding: str = "utf-8") -> IO[Any]:
        """Wrapper around open()"""
        return open(self.file_name, mode=self.open_mode, encoding=encoding)

    def execute_lock_op(self, file_handle: IO, operation: int) -> None:
        """Execute the supplied lock operation"""
        if operation != self.no_lock_operation:
            fcntl.flock(file_handle, operation)
        #

    def lock(self, file_handle: IO) -> None:
        """Lock the file"""
        self.execute_lock_op(file_handle, self.lock_operation)

    def unlock(self, file_handle: IO) -> None:
        """Lock the file"""
        self.execute_lock_op(file_handle, self.unlock_operation)


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
