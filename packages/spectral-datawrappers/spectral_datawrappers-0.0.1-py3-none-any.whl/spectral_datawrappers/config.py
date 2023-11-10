
from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    env_switcher='ENV',
    envvar_prefix="DATA_WRAPPERS",
    settings_files=['spectral_datawrappers/config/settings.toml', 'spectral_datawrappers/config/.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
