from pathlib import Path

import environ

env = environ.Env()
env_file = env("ENV_FILE", default=Path(__file__).resolve().parent.parent.parent / ".env")
if env_file and Path(env_file).exists():
    environ.Env.read_env(env_file)

env_name = env("DJANGO_ENV", default="dev").lower()

if env_name in {"prod", "production"}:
    from .prod import *  # noqa: F401,F403
else:
    from .dev import *  # noqa: F401,F403
