# -*- coding: utf-8 -*-
from subprocess import CalledProcessError, check_call
from typing import Any, List, Sequence

import dotbot


class Apt(dotbot.Plugin):
    def can_handle(self, directive: str) -> bool:
        return directive == 'apt'

    def handle(self, directive: str, packages: List[str]) -> bool:
        success = self._run(['sudo','apt', 'update'], 'Updating APT, may require sudoing') \
                  and self._run(['sudo', 'apt', 'install', '-y'] + packages,
                                'Installing: {}'.format(', '.join(packages)))

        if success:
            self._log.info('APT packages installed successfully')

        return success

    def _run(self, command: Sequence[Any], log_message: str) -> bool:
        self._log.lowinfo(log_message)
        try:
            check_call(command)
            return True
        except CalledProcessError as e:
            self._log.error(e)
            return False
