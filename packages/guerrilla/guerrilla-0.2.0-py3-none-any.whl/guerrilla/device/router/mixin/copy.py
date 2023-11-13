from dataclasses import dataclass

@dataclass
class CopyMixin:
    """
    This class provides methods to upload firmware, export and import configuration files
    to and from a device using various transfer methods such as TFTP, USB, SCP and SFTP.
    """
    
    error_extend = ["Configuration Upload Fail!", "Config file import failed.", "Input error", "No USB Device"]

    def _validate_transfer_details(self, transfer_method, ip, cfg_path_name, account, password, is_firmware=False):
        """
        Validates the transfer details such as transfer method, IP, configuration path name, account and password.
        Raises ValueError if any of the details are invalid.
        """
        if is_firmware and transfer_method.lower() == 'usb':
            self.logger.error("USB method is not supported for firmware upload.")
            
        valid_methods = ['tftp', 'usb', 'scp', 'sftp']
        if transfer_method.lower() not in valid_methods:
            self.logger.warning(f"Invalid transfer method. Must be one of {valid_methods}.")

        if transfer_method.lower() in ['scp', 'sftp'] and (not account or not password):
            self.logger.warning("Account and password must be provided for SCP/SFTP.")

        if transfer_method.lower() == 'tftp' and (not ip or not cfg_path_name):
            self.logger.warning("IP and configuration path name must be provided for TFTP.")

        if transfer_method.lower() == 'usb' and not cfg_path_name:
            self.logger.warning("Configuration path name must be provided for USB.")

    @staticmethod
    def _construct_command(transfer_method, ip, cfg_path_name, account, password, command_type):
        """
        Constructs the command to be executed based on the transfer method and other details.
        """
        command = "copy "
        if transfer_method.lower() in ['scp', 'sftp']:
            command += f"{transfer_method} {account} {password} {ip} {command_type} {cfg_path_name}"
        elif transfer_method.lower() == 'tftp':
            command += f"tftp {ip} {command_type} {cfg_path_name}"
        elif transfer_method.lower() == 'usb':
            command += f"usb {cfg_path_name}"
        return command
    
    def _construct_export_command(self, transfer_method, ip, cfg_path_name, account, password):
        if transfer_method.lower() == 'tftp':
            return f"copy running-config tftp {ip} {cfg_path_name}"
        elif transfer_method.lower() in ['scp', 'sftp']:
            return f"copy running-config {transfer_method} {account} {password} {ip} {cfg_path_name}"
        elif transfer_method.lower() == 'usb':
            return f"copy running-config usb {cfg_path_name}"
        else:
            self.logger.error("Invalid transfer method.")

    def upload_firmware(self, transfer_method: str, ip: str = '', filename: str = '', account: str = '', password: str = '') -> str:
        """
        Uploads firmware to the device using the specified transfer method.
        
        Examples:
            >>> device.upload_firmware('tftp', '192.168.127.3', 'firmware.rom')
            >>> device.upload_firmware('scp', '192.168.127.3', 'firmware.rom', 'admin', 'admin')
            >>> device.upload_firmware('sftp', '192.168.127.3', 'firmware.rom', 'admin', 'admin')
        
        """
        self._validate_transfer_details(transfer_method, ip, filename, account, password, is_firmware=True)
        command = self._construct_command(transfer_method, ip, filename, account, password, "device-firmware")
        response = self.run(command, 
                            expect_string="Checking transfer:Firmware Upgrade OK! Restart the device.", 
                            extend_error=self.error_extend ,
                            read_timeout=120
                            )
        if not response.failed:
            from yaspin import yaspin
            import time
            
            self.disconnect()
            with yaspin(text="Restarting...").shark as sp:
                time.sleep(30)
                sp.ok("✅ ")
            self.connect()
            self.logger.success(f"Upfrade firmware to {filename}.")
        return response

    def export_config(self, transfer_method: str, ip: str = '', cfg_path_name: str = '', account: str = '', password: str = ''):
        """
        Exports the configuration file from the device using the specified transfer method.
        
        Examples:
            >>> device.export_config('tftp', '192.168.127.3', 'default.ini')
            >>> device.export_config('scp', '192.168.127.3', 'default.ini', 'admin', 'admin')
            >>> device.export_config('sftp', '192.168.127.3', 'default.ini', 'admin', 'admin')
            >>> device.export_config('usb', cfg_path_name='default.ini')
        """
        self._validate_transfer_details(transfer_method, ip, cfg_path_name, account, password)
        command = self._construct_export_command(transfer_method, ip, cfg_path_name, account, password)
        response = self.run(command, 
                            expect_string="Configuration Upload Success!",
                            extend_error=self.error_extend
                            )
        if not response.failed:
            self.logger.success(f"Exported configuration to {cfg_path_name}.")
        return response

    def import_config(self, transfer_method: str, ip: str = '', cfg_path_name: str = '', account: str = '', password: str = ''):
        """
        Imports the configuration file to the device using the specified transfer method.
        
        Examples:
            >>> device.import_config('tftp', '192.168.127.3', 'default.ini')
            >>> device.import_config('scp', '192.168.127.3', 'default.ini', 'admin', 'admin')
            >>> device.import_config('sftp', '192.168.127.3', 'default.ini', 'admin', 'admin')
            >>> device.import_config('usb', cfg_path_name='default.ini')
        """
        self._validate_transfer_details(transfer_method, ip, cfg_path_name, account, password)
        command = self._construct_command(transfer_method, ip, cfg_path_name, account, password, "config-file")
        response = self.run(command, 
                            expect_string="Config file import successfully." ,
                            extend_error=self.error_extend
                            )
        if not response.failed:
            self.logger.success(f"Imported configuration from {cfg_path_name}.")
            self.connect()
        return response
