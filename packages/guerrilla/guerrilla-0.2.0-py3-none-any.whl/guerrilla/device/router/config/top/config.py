from dataclasses import dataclass, field
from .hostname import Hostname
from .clock import Clock
from .snmp import Snmp
from .backup import AutoBackup
from .user import User

@dataclass
class MainConfig:
    hostname: Hostname = field(default_factory=Hostname, init=False)
    clock: Clock = field(default_factory=Clock, init=False)
    snmp: Snmp = field(default_factory=Snmp, init=False)
    auto_backup: AutoBackup = field(default_factory=AutoBackup, init=False)
    user: User = field(default_factory=User, init=False)
    
    def __post_init__(self):
        self.hostname = Hostname(self.device)
        self.clock = Clock(self.device)
        self.snmp = Snmp(self.device)
        self.auto_backup = AutoBackup(self.device)
        self.user = User(self.device)
