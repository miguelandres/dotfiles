# -*- coding: utf-8 -*-
from subprocess import CalledProcessError, check_call
from typing import Any, List, Sequence

import dotbot


class Snap(dotbot.Plugin):
    def can_handle(self, directive: str) -> bool:
        return directive == 'snap'

    def handle(self, directive: str, packages: List[str]) -> bool:
        self._log.info('Snap Installing {}'.format(', '.join(packages)))
        success = True
        for pkg in packages:
            success = success and self._run(
                ['sudo', 'snap', 'install', pkg], 'Installing {}. May need to sudo.'.format(pkg))

        if success:
            self._log.info('SNAP packages installed successfully')

        return success

    def _run(self, command: Sequence[Any], log_message: str) -> bool:
        self._log.lowinfo(log_message)
        try:
            check_call(command)
            return True
        except CalledProcessError as e:
            self._log.error(e)
            return False
