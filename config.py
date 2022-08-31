from abc import ABC, abstractmethod


class Config:
    notify_command: str
    tmp_files_folder: str
    work_set_duration: str
    break_duration: str


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
