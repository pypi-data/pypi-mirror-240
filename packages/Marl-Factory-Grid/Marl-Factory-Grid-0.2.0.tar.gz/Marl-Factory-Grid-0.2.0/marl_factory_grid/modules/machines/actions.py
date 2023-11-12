from typing import Union

import marl_factory_grid.modules.machines.constants
from marl_factory_grid.environment.actions import Action
from marl_factory_grid.utils.results import ActionResult

from marl_factory_grid.modules.machines import constants as m
from marl_factory_grid.environment import constants as c
from marl_factory_grid.utils import helpers as h


class MachineAction(Action):

    def __init__(self):
        super().__init__(m.MACHINE_ACTION)

    def do(self, entity, state) -> Union[None, ActionResult]:
        if machine := h.get_first(state[m.MACHINES].by_pos(entity.pos)):
            if valid := machine.maintain():
                return ActionResult(entity=entity, identifier=self._identifier, validity=valid, reward=marl_factory_grid.modules.machines.constants.MAINTAIN_VALID)
            else:
                return ActionResult(entity=entity, identifier=self._identifier, validity=valid, reward=marl_factory_grid.modules.machines.constants.MAINTAIN_FAIL)
        else:
            return ActionResult(entity=entity, identifier=self._identifier,
                                validity=c.NOT_VALID, reward=marl_factory_grid.modules.machines.constants.MAINTAIN_FAIL
                                )
