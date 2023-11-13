from guerrilla.device.router.config import BaseConfig

class Hostname(BaseConfig):
    
    def set_hostname(self, hostname):
        """
        Sets the hostname of the router.

        Args:
            hostname (str): The new hostname to set. max 30 characters
            
        Examples:
            >>> device.config.hostname.set_hostname('New York')
        """
        self._execute_config_command(f'hostname {hostname}', f"Hostname set to {hostname}")
    
    def reset_hostname(self):
        """
        Resets the hostname of the router to the default.
        
        Examples:
            >>> device.config.hostname.reset_hostname()
        """
        self._execute_config_command('no hostname', "Hostname reset to default")