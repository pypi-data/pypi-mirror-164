# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable
from dataclasses import dataclass, field
import dearpygui.dearpygui as dpg

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaApplication:
    # The sub_systems and their constructors are stored in lists
    #   because their execution order might be of importance
    # `sub_systems` is not part of init as it shouldn't house any objects at the start of the application
    #   Is only populated during startup procedure
    sub_systems:list[SubSystem] = field(init=False, default_factory=list)

    # ------------------------------------------------------------------------------------------------------------------
    # - Sub System related methods -
    # ------------------------------------------------------------------------------------------------------------------
    def sub_systems_register(self, constructor: Callable):
        obj = constructor(app=self)
        self.sub_systems.append(obj)
        return obj

    def sub_systems_run(self):
        """
        Run at application startup down.
        AFTER the DPG context has been created
        """
        for sub_system in self.sub_systems: #type: SubSystem
            sub_system.run()

    def sub_systems_close_down_controlled(self):
        """
        Run at application close down.
        As the sub systems themselves might have some protocols to handle close downs
        """
        for sub_system in self.sub_systems: #type: SubSystem
            sub_system.close_down()

    # ------------------------------------------------------------------------------------------------------------------
    # - Main Application methods -
    # ------------------------------------------------------------------------------------------------------------------
    def run(self):
        # Anything that has to be run before DPG is created,
        #   must be called in `__post_init__` of the application

        # Create the context
        #   done here so `self.sub_systems_startup()` sub systems can use dpg functions
        #   if the context was created later functions that depend on dpg, would refuse to work
        dpg.create_context()
        self.sub_systems_run() # runs all constructors for the sub systems
        self.main()
        # Shows dpg window to the user
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui() # BLOCKING
        # Closedown procedure after blocking `dpg.start_dearpygui()` function
        # TODO check if this is correct placement for this method
        #   Else place after `dpg.destroy_context()`
        self.sub_systems_close_down_controlled()
        dpg.destroy_context()


    def main(self):
        """
        Run any dpg functions in this method if no custom sub system is used for the creation of dpg UI.
        The functions `dpg.show_viewport()` and `dpg.start_dearpygui()`
            ares run after this method so calling it within this method will cause issues
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class SubSystem:
    app: AthenaApplication

    def __post_init__(self):
        pass

    def run(self):
        """Is ran after DPG has been started"""
        pass

    def close_down(self):
        pass