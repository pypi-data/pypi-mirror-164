from __future__ import annotations
"""
Python Package Management (PIP) Client
"""

import re
import sys

from urllib.parse import urlparse, urlunparse, ParseResult
from typing import Union, Any, Sequence, Optional
from packaging.version import parse

# Trust Platform Modules
from .client_model import PackageManagerClient
from .data_models import PackageDependencies, PackageDetails


class PipPackageClient(PackageManagerClient):
    """
    Interact with the python packaging system
    """
    __rePipList = re.compile(r'^(?P<name>[\w\-]+)\s+(?P<installed>[\w\-\.]+)\s+((?P<loc>[\S]+)$|(?P<loc_tool>[\S]+)\s+(?P<tool>[\w]+)$)')
    __rePipIndex = re.compile(r'^(?P<name>[\w\-]+)\s+\((?P<latest>[\w\-\.]+)\)')
    __cmdBase = [sys.executable, '-m', 'pip']

    def __init__(self, package_list: Sequence[str] = [], index: Optional[str] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._installed: dict[str, Any] = {}
        self._available: dict[str, Any] = {}
        self._search_list = package_list
        self._index: Optional[str] = index

    def login(self, username: str, password: str, hostname: str) -> None:
        """
        Provide the user credentials for logging into the system
        """
        urlinfo = urlparse(hostname)._asdict()
        urlinfo['netloc'] = f"{username}:{password}@{urlinfo['netloc']}"
        self._index = urlunparse(ParseResult(**urlinfo))

    def logout(self) -> None:
        """
        Log out of the system
        """
        if self._index and '@' in self._index:
            self._index = self._index.split('@')[1]

    def is_logged_in(self) -> Union[str, None]:
        """
        Check if anyone is logged in
        """
        if self._index and '@' in self._index:
            urlinfo = urlparse(self._index)
            return urlinfo.username
        else:
            return None

    def update_local(self, **kwargs: Any) -> None:
        """
        Update the packaging information
        """
        cmd = self.__cmdBase + ['list', '-v']
        outs, _ = self._proc.run_cmd(cmd, **kwargs)

        for line in outs.splitlines():
            if match := self.__rePipList.match(line):
                info = match.groupdict()
                if info['tool'] == 'pip':
                    self._installed[info['name']] = PackageDetails(**info, channel='pypi')

    def update_remote(self, **kwargs: Any) -> None:
        """
        Retrieve the list of available packages and their versions
        """
        for package in self._search_list:
            cmd = self.__cmdBase + ['index', '--pre']
            if self._index:
                cmd += ['-i', self._index]
            cmd += ['versions', package]
            outs, _ = self._proc.run_cmd(cmd, err_handling=self._proc.LOG, **kwargs)
            for line in outs.splitlines():
                match = self.__rePipIndex.match(line)
                if match and match.group('name') == package:
                    self._available[package] = PackageDetails(**match.groupdict(), channel='pypi')

    def install(self, packages: Sequence[str], **kwargs: Any) -> None:
        """
        Install the selected packages and their dependencies
        """
        cmd = self.__cmdBase + ['install', '--upgrade']
        if self._index:
            cmd += ['-i', self._index]
        cmd += packages
        outs, returncode = self._proc.run_cmd(cmd, err_handling=self._proc.LOG, **kwargs)
        self._log.log(outs)
        self.update_local()

    def upgrade(self, packages: Sequence[str], **kwargs: Any) -> None:
        """
        Upgrade the selected packages to the latest versions
        """
        self.install(packages, **kwargs)

    def update_dependency_list(self, packages: Union[str, Sequence[str]], channel: Optional[str]=None, **kwargs: Any) -> PackageDependencies:
        """
        Dependencies are listed as part of additional metadata so we need to retrieve
        that information first before we execute additional steps
        """
        return PackageDependencies()

    def get_dependencies(self, pattern: str = 'tpds') -> Sequence[PackageDetails]:
        """
        Get a list of dependencies we need to watch
        """
        return []

    def get_installed_packages(self, pattern: str = 'tpds') -> Sequence[PackageDetails]:
        """
        Get a list of installed tpds packages
        """
        
        return list(filter(lambda x: pattern in x.name, self._installed.values()))

    def get_available_packages(self, pattern: str = 'tpds') -> Sequence[PackageDetails]:
        """
        Get a list of all available packages that can be installed
        """
        return list(filter(lambda x: pattern in x.name, self._available.values()))

__all__ = ['PipPackageClient']
