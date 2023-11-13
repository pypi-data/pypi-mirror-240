from guerrilla.device.router.config import BaseConfig

class AutoBackup(BaseConfig):
    def enable_config(self):
        """
        Enables automatic backup of the configuration.
        
        Examples:
            >>> device.config.auto_backup.enable_config()
        """
        self._execute_config_command('auto-backup config', 
                                     success_message="Automatic backup of configuration enabled.")

    def disable_config(self):
        """
        Disables automatic backup of the configuration.
        
        Examples:
            >>> device.config.auto_backup.disable_config()
        """
        self._execute_config_command('no auto-backup config', 
                                     success_message="Automatic backup of configuration disabled.")

    def enable(self):
        """
        Enables hardware interface for auto-backup.
        
        Examples:
            >>> device.config.auto_backup.enable()
        """
        self._execute_config_command('auto-backup enable', 
                                     success_message="Hardware interface for auto-backup enabled.")

    def disable(self):
        """
        Disables hardware interface for auto-backup.
        
        Examples:
            >>> device.config.auto_backup.disable()
        """
        self._execute_config_command('no auto-backup enable', 
                                     success_message="Hardware interface for auto-backup disabled.")

    def enable_auto_load_config(self):
        """
        Enables auto-load of configuration on bootup.
        
        Examples:
            >>> device.config.auto_backup.enable_auto_load_config()
        """
        self._execute_config_command('auto-backup auto-load config', 
                                     success_message="Auto-load of configuration on bootup enabled.")

    def disable_auto_load_config(self):
        """
        Disables auto-load of configuration on bootup.
        
        Examples:
            >>> device.config.auto_backup.disable_auto_load_config()
        """
        self._execute_config_command('no auto-backup auto-load config', 
                                     success_message="Auto-load of configuration on bootup disabled.")