from abc import ABC, abstractmethod


class Config:
    notify_command: str
    tmp_files_folder: str
    notify_sound_filename:str
    work_set_duration: int
    break_duration: int
    take_longer_break_after_how_many_work_sets: int
    long_break_multiplier: int
    enable_tracker: bool


class ConfigTemplate:
    @abstractmethod
    def get_config_path(self):
        pass

    def get_config(self) -> Config:
        """Get config data from config folder
        :returns: dict

        """
        path = self.get_config_path()
        pass


class WindowsConfig(ConfigTemplate):
    def get_config_path(self):
        pass


class UnixConfig(ConfigTemplate):
    def get_config_path(self):
        pass
