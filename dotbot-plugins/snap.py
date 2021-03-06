# -*- coding: utf-8 -*-
from subprocess import CalledProcessError, check_call
from typing import Any, List, Sequence

import dotbot


class Snap(dotbot.Plugin):
    def can_handle(self, directive: str) -> bool:
        return directive == 'snap' or directive == 'snap-classic'

    def handle(self, directive: str, packages: List[str]) -> bool:
        use_classic = False
        if directive == 'snap-classic':
            use_classic = True

        self._log.info('Snap {} Installing {}'.format('classic' if use_classic else '', ', '.join(packages)))
        success = True
        base_command = ['sudo', 'snap', 'install', '--classic'] if use_classic else ['sudo', 'snap', 'install']
        for pkg in packages:
            success = success and self._run(base_command + [pkg], 'Installing {}. May need to sudo.'.format(pkg))

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
