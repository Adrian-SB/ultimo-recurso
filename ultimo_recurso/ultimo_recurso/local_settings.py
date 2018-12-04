# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "_#vmb%!lbhggfuo-=f)$7)3^nx!=61ytmil7gf)krb7=gx8yne"
NEVERCACHE_KEY = "o301pljr0^#0&ek!dwafwxt@)0c6)3_kah@b61!rt+sbsrdw18"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "viveros",
        "USER": "adri",
        "PASSWORD": "adri",
        "HOST": "localhost",
        "PORT": "",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1"]

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
#     "SSH_USER": "",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": [""],  # Will be used as ALLOWED_HOSTS in production
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }

#PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
#PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
#PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)
#CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP
#STATIC_URL = "/static/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
