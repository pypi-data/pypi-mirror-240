from guerrilla.device.router.config import BaseConfig

class Snmp(BaseConfig):
    
    def set_contact(self, contact: str):
        """
        Sets the contact of the router.

        Args:
            contact (str): The new contact to set. max 30 characters
        
        Examples:
            >>> device.config.snmp.set_contact('John Doe')
        """ 
        self._execute_config_command(f'snmp-server contact {contact}', 
                                        success_message=f"Contact set to {contact}")
    
    def reset_contact(self):
        """
        Resets the contact of the router to the default.
        
        Examples:
            >>> device.config.snmp.reset_contact()
        """  
        self._execute_config_command('no snmp-server contact', 
                                        success_message="Contact reset to default")
            
    def set_description(self, description: str):
        """
        Sets the description of the router.

        Args:
            description (str): The new description to set. max 30 characters
        
        Examples:
            >>> device.config.snmp.set_description('This is a router')
        """  
        self._execute_config_command(f'snmp-server description {description}', 
                                        success_message=f"Description set to {description}")
    
    def reset_description(self):
        """
        Resets the description of the router to the default.
        
        Examples:
            >>> device.config.snmp.reset_description()
        """  
        self._execute_config_command('no snmp-server description', 
                                        success_message="Description reset to default")
    
    def set_location(self, location: str):
        """
        Sets the location of the router.

        Args:
            location (str): The new location to set. max 80 characters
            
        Examples:
            >>> device.config.snmp.set_location('New York')
        """  
        self._execute_config_command(f'snmp-server location {location}', 
                                        success_message=f"Location set to {location}")
    
    def reset_location(self):
        """
        Resets the location of the router to the default.
        
        Examples:
            >>> device.config.snmp.reset_location()
        """  
        self._execute_config_command('no snmp-server location', 
                                        success_message="Location reset to default")
