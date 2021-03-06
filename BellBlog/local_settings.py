# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "jnlmly&n@0q90hsg-cq@0z^8hq4j=orn@cb*ju4&4l_-3ux1kt"
NEVERCACHE_KEY = ")n6(63%o=-!ku!@&u6u^o_8a1)oe1&sea%j_=wyr^e7g)ug5kf"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
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

FABRIC = {
    "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
    # "SSH_USER": "",  # VPS SSH username
    # "HOSTS": [""],  # The IP address of your VPS
    # "DOMAINS": [""],  # Will be used as ALLOWED_HOSTS in production
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    # "DB_PASS": "",  # Live database password
    # "ADMIN_PASS": "",  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
