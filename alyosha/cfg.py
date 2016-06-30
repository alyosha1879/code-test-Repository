#from oslo_config import cfg
import oslo_config.cfg

# usage:
# ./bin/alyosha --list_option 1,2,3 --string_option "test-string" --enable_debugger

CONF = oslo_config.cfg.ConfigOpts()
CONF.register_cli_opts([
    oslo_config.cfg.ListOpt('list_option', default=[], help=''),
    oslo_config.cfg.StrOpt('string_option', default=None, help=''),
    oslo_config.cfg.BoolOpt('enable_debugger', default=False, help=''),
])

from oslo_config.cfg import ConfigOpts
from oslo_config.cfg import BoolOpt
from oslo_config.cfg import IntOpt
from oslo_config.cfg import ListOpt
from oslo_config.cfg import MultiStrOpt
from oslo_config.cfg import StrOpt
from oslo_config.cfg import FloatOpt
from oslo_config.cfg import RequiredOptError
from oslo_config.cfg import ConfigFilesNotFoundError
