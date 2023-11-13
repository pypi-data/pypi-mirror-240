
class ReloadMixin:
    
    def _reload_factory_default(self, no_cert: bool = False):
        import time
        from yaspin import yaspin
        cmd = "reload factory-default"
        msg = "Router is reloading to factory default settings"
        if no_cert:
            cmd += " no cert"
            msg += " without certificate"
            
        self._back_to_main()
        self.run(cmd, expect_string="[Y/n]")
        self.run_timing('Y')
        self.disconnect()
        
        self.logger.info(msg)
        with yaspin(text="Reloading...").shark as sp:
            time.sleep(30)
            sp.ok("✅ ")
        self.connect()
        self.logger.success("Router reloaded to factory default settings")
        
    
    def reload_factory_default(self):
        """
        Reloads the router device to factory default settings.
        """
        self._reload_factory_default()
        
    def reload_factory_default_no_cert(self):
        """
        Reloads the router device to factory default settings without certificate.
        """
        self._reload_factory_default(no_cert=True)
    
    def reload(self):
        """
        Reloads the router device.
        """
        import time
        from yaspin import yaspin

        self._back_to_main()
        self.run("reload", expect_string="[Y/n]")
        self.run_timing('Y')
        self.disconnect()
        self.logger.info("Router is reloading")
        with yaspin(text="Reloading...").shark as sp:
            time.sleep(30)
            sp.ok("✅ ")
        self.connect()
        self.logger.success("Router reloaded")