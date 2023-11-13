"""
Default jorm settings. Override these with settings in the module pointed to
by the JORM_SETTINGS_MODULE environment variable.
"""


# This is defined here as a do-nothing function because we can't import
# jorm.utils.translation -- that module depends on the settings.
def gettext_noop(s):
    return s


####################
# CORE             #
####################

DEBUG = False

# Whether the framework should propagate raw exceptions rather than catching
# them. This is useful under some testing situations and should never be used
# on a live site.
DEBUG_PROPAGATE_EXCEPTIONS = False

# Local time zone for this installation. All choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = "America/Chicago"

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

# Languages we provide translations for, out of the box.
LANGUAGES = [
    ("af", gettext_noop("Afrikaans")),
    ("ar", gettext_noop("Arabic")),
    ("ar-dz", gettext_noop("Algerian Arabic")),
    ("ast", gettext_noop("Asturian")),
    ("az", gettext_noop("Azerbaijani")),
    ("bg", gettext_noop("Bulgarian")),
    ("be", gettext_noop("Belarusian")),
    ("bn", gettext_noop("Bengali")),
    ("br", gettext_noop("Breton")),
    ("bs", gettext_noop("Bosnian")),
    ("ca", gettext_noop("Catalan")),
    ("ckb", gettext_noop("Central Kurdish (Sorani)")),
    ("cs", gettext_noop("Czech")),
    ("cy", gettext_noop("Welsh")),
    ("da", gettext_noop("Danish")),
    ("de", gettext_noop("German")),
    ("dsb", gettext_noop("Lower Sorbian")),
    ("el", gettext_noop("Greek")),
    ("en", gettext_noop("English")),
    ("en-au", gettext_noop("Australian English")),
    ("en-gb", gettext_noop("British English")),
    ("eo", gettext_noop("Esperanto")),
    ("es", gettext_noop("Spanish")),
    ("es-ar", gettext_noop("Argentinian Spanish")),
    ("es-co", gettext_noop("Colombian Spanish")),
    ("es-mx", gettext_noop("Mexican Spanish")),
    ("es-ni", gettext_noop("Nicaraguan Spanish")),
    ("es-ve", gettext_noop("Venezuelan Spanish")),
    ("et", gettext_noop("Estonian")),
    ("eu", gettext_noop("Basque")),
    ("fa", gettext_noop("Persian")),
    ("fi", gettext_noop("Finnish")),
    ("fr", gettext_noop("French")),
    ("fy", gettext_noop("Frisian")),
    ("ga", gettext_noop("Irish")),
    ("gd", gettext_noop("Scottish Gaelic")),
    ("gl", gettext_noop("Galician")),
    ("he", gettext_noop("Hebrew")),
    ("hi", gettext_noop("Hindi")),
    ("hr", gettext_noop("Croatian")),
    ("hsb", gettext_noop("Upper Sorbian")),
    ("hu", gettext_noop("Hungarian")),
    ("hy", gettext_noop("Armenian")),
    ("ia", gettext_noop("Interlingua")),
    ("id", gettext_noop("Indonesian")),
    ("ig", gettext_noop("Igbo")),
    ("io", gettext_noop("Ido")),
    ("is", gettext_noop("Icelandic")),
    ("it", gettext_noop("Italian")),
    ("ja", gettext_noop("Japanese")),
    ("ka", gettext_noop("Georgian")),
    ("kab", gettext_noop("Kabyle")),
    ("kk", gettext_noop("Kazakh")),
    ("km", gettext_noop("Khmer")),
    ("kn", gettext_noop("Kannada")),
    ("ko", gettext_noop("Korean")),
    ("ky", gettext_noop("Kyrgyz")),
    ("lb", gettext_noop("Luxembourgish")),
    ("lt", gettext_noop("Lithuanian")),
    ("lv", gettext_noop("Latvian")),
    ("mk", gettext_noop("Macedonian")),
    ("ml", gettext_noop("Malayalam")),
    ("mn", gettext_noop("Mongolian")),
    ("mr", gettext_noop("Marathi")),
    ("ms", gettext_noop("Malay")),
    ("my", gettext_noop("Burmese")),
    ("nb", gettext_noop("Norwegian Bokmål")),
    ("ne", gettext_noop("Nepali")),
    ("nl", gettext_noop("Dutch")),
    ("nn", gettext_noop("Norwegian Nynorsk")),
    ("os", gettext_noop("Ossetic")),
    ("pa", gettext_noop("Punjabi")),
    ("pl", gettext_noop("Polish")),
    ("pt", gettext_noop("Portuguese")),
    ("pt-br", gettext_noop("Brazilian Portuguese")),
    ("ro", gettext_noop("Romanian")),
    ("ru", gettext_noop("Russian")),
    ("sk", gettext_noop("Slovak")),
    ("sl", gettext_noop("Slovenian")),
    ("sq", gettext_noop("Albanian")),
    ("sr", gettext_noop("Serbian")),
    ("sr-latn", gettext_noop("Serbian Latin")),
    ("sv", gettext_noop("Swedish")),
    ("sw", gettext_noop("Swahili")),
    ("ta", gettext_noop("Tamil")),
    ("te", gettext_noop("Telugu")),
    ("tg", gettext_noop("Tajik")),
    ("th", gettext_noop("Thai")),
    ("tk", gettext_noop("Turkmen")),
    ("tr", gettext_noop("Turkish")),
    ("tt", gettext_noop("Tatar")),
    ("udm", gettext_noop("Udmurt")),
    ("ug", gettext_noop("Uyghur")),
    ("uk", gettext_noop("Ukrainian")),
    ("ur", gettext_noop("Urdu")),
    ("uz", gettext_noop("Uzbek")),
    ("vi", gettext_noop("Vietnamese")),
    ("zh-hans", gettext_noop("Simplified Chinese")),
    ("zh-hant", gettext_noop("Traditional Chinese")),
]

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = ["he", "ar", "ar-dz", "ckb", "fa", "ug", "ur"]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
LOCALE_PATHS = []

# Settings for language cookie
LANGUAGE_COOKIE_NAME = "django_language"
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_PATH = "/"
LANGUAGE_COOKIE_SECURE = False
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = None

# Default charset to use for all HttpResponse objects, if a MIME type isn't
# manually specified. It's used to construct the Content-Type header.
DEFAULT_CHARSET = "utf-8"

# Database connection info. If left empty, will default to the dummy backend.
DATABASES = {}

# Classes used to implement DB routing behavior.
DATABASE_ROUTERS = []

# A secret key for this particular Django installation. Used in secret-key
# hashing algorithms. Set this in your settings, or Django will complain
# loudly.
SECRET_KEY = ""

# List of secret keys used to verify the validity of signatures. This allows
# secret key rotation.
SECRET_KEY_FALLBACKS = []

STORAGES = {
    "default": {
        "BACKEND": "jorm.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "jorm.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# List of upload handler classes to be applied in order.
FILE_UPLOAD_HANDLERS = [
    "jorm.core.files.uploadhandler.MemoryFileUploadHandler",
    "jorm.core.files.uploadhandler.TemporaryFileUploadHandler",
]

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum number of GET/POST parameters that will be read before a
# SuspiciousOperation (TooManyFieldsSent) is raised.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000

# Maximum number of files encoded in a multipart upload that will be read
# before a SuspiciousOperation (TooManyFilesSent) is raised.
DATA_UPLOAD_MAX_NUMBER_FILES = 100

# Directory in which upload streamed files will be temporarily saved. A value of
# `None` will make Django use the operating system's default temporary directory
# (i.e. "/tmp" on *nix systems).
FILE_UPLOAD_TEMP_DIR = None

# The numeric mode to set newly-uploaded files to. The value should be a mode
# you'd pass directly to os.chmod; see
# https://docs.python.org/library/os.html#files-and-directories.
FILE_UPLOAD_PERMISSIONS = 0o644

# The numeric mode to assign to newly-created directories, when uploading files.
# The value should be a mode as you'd pass to os.chmod;
# see https://docs.python.org/library/os.html#files-and-directories.
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# Python module path where user will place custom format definition.
# The directory where this setting is pointing should contain subdirectories
# named as the locales, containing a formats.py file
# (i.e. "myproject.locale" for myproject/locale/en/formats.py etc. use)
FORMAT_MODULE_PATH = None

# Default formatting for date objects. See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = "N j, Y"

# Default formatting for datetime objects. See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATETIME_FORMAT = "N j, Y, P"

# Default formatting for time objects. See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
TIME_FORMAT = "P"

# Default formatting for date objects when only the year and month are relevant.
# See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
YEAR_MONTH_FORMAT = "F Y"

# Default formatting for date objects when only the month and day are relevant.
# See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
MONTH_DAY_FORMAT = "F j"

# Default short formatting for date objects. See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
SHORT_DATE_FORMAT = "m/d/Y"

# Default short formatting for datetime objects.
# See all available format strings here:
# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
SHORT_DATETIME_FORMAT = "m/d/Y P"

# Default formats to be used when parsing dates from input boxes, in order
# See all available format string here:
# https://docs.python.org/library/datetime.html#strftime-behavior
# * Note that these format strings are different from the ones to display dates
DATE_INPUT_FORMATS = [
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
]

# Default formats to be used when parsing times from input boxes, in order
# See all available format string here:
# https://docs.python.org/library/datetime.html#strftime-behavior
# * Note that these format strings are different from the ones to display dates
TIME_INPUT_FORMATS = [
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
    "%H:%M",  # '14:30'
]

# Default formats to be used when parsing dates and times from input boxes,
# in order
# See all available format string here:
# https://docs.python.org/library/datetime.html#strftime-behavior
# * Note that these format strings are different from the ones to display dates
DATETIME_INPUT_FORMATS = [
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
]

# First day of week, to be used on calendars
# 0 means Sunday, 1 means Monday...
FIRST_DAY_OF_WEEK = 0

# Decimal separator symbol
DECIMAL_SEPARATOR = "."

# Boolean that sets whether to add thousand separator when formatting numbers
USE_THOUSAND_SEPARATOR = False

# Number of digits that will be together, when splitting them by
# THOUSAND_SEPARATOR. 0 means no grouping, 3 means splitting by thousands...
NUMBER_GROUPING = 0

# Thousand separator symbol
THOUSAND_SEPARATOR = ","

# The tablespaces to use for each model when not specified otherwise.
DEFAULT_TABLESPACE = ""
DEFAULT_INDEX_TABLESPACE = ""

# Default primary key field type.
DEFAULT_AUTO_FIELD = "jorm.db.models.AutoField"

#########
# CACHE #
#########

# The cache backends to use.
CACHES = {
    "default": {
        "BACKEND": "jorm.core.cache.backends.locmem.LocMemCache",
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ""
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = "default"

##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = "auth.User"

AUTHENTICATION_BACKENDS = ["jorm.contrib.auth.backends.ModelBackend"]

# The number of seconds a password reset link is valid for (default: 3 days).
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3

# the first hasher in this list is the preferred algorithm.  any
# password using different algorithms will be converted automatically
# upon login
PASSWORD_HASHERS = [
    "jorm.contrib.auth.hashers.PBKDF2PasswordHasher",
    "jorm.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "jorm.contrib.auth.hashers.Argon2PasswordHasher",
    "jorm.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "jorm.contrib.auth.hashers.ScryptPasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = []

###########
# SIGNING #
###########

SIGNING_BACKEND = "jorm.core.signing.TimestampSigner"

###########
# LOGGING #
###########

# The callable to use to configure logging
LOGGING_CONFIG = "logging.config.dictConfig"

# Custom logging configuration.
LOGGING = {}

# Default exception reporter class used in case none has been
# specifically assigned to the HttpRequest instance.
DEFAULT_EXCEPTION_REPORTER = "jorm.views.debug.ExceptionReporter"

# Default exception reporter filter class used in case none has been
# specifically assigned to the HttpRequest instance.
DEFAULT_EXCEPTION_REPORTER_FILTER = "jorm.views.debug.SafeExceptionReporterFilter"

###########
# TESTING #
###########

# The name of the class to use to run the test suite
TEST_RUNNER = "jorm.test.runner.DiscoverRunner"

# Apps that don't need to be serialized at test database creation time
# (only apps with migrations are to start with)
TEST_NON_SERIALIZED_APPS = []

############
# FIXTURES #
############

# The list of directories to search for fixtures
FIXTURE_DIRS = []

###############
# STATICFILES #
###############

# A list of locations of additional static files
STATICFILES_DIRS = []

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "jorm.contrib.staticfiles.finders.FileSystemFinder",
    "jorm.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'jorm.contrib.staticfiles.finders.DefaultStorageFinder',
]

##############
# MIGRATIONS #
##############

# Migration module overrides for apps, by app label.
MIGRATION_MODULES = {}

#################
# SYSTEM CHECKS #
#################

# List of all issues generated by system checks that should be silenced. Light
# issues like warnings, infos or debugs will not generate a message. Silencing
# serious issues like errors and criticals does not result in hiding the
# message, but Django will not stop you from e.g. running server.
SILENCED_SYSTEM_CHECKS = []
