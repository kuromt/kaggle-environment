#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'
#c.Application.log_level = 30
#c.JupyterHub.active_server_limit = 0
#c.JupyterHub.active_user_window = 1800
#c.JupyterHub.activity_resolution = 30
#c.JupyterHub.admin_access = False
#c.JupyterHub.admin_users = set()
#c.JupyterHub.allow_named_servers = False
#c.JupyterHub.answer_yes = False
#c.JupyterHub.api_tokens = {}
#c.JupyterHub.authenticate_prometheus = True
#              e.g. `c.JupyterHub.authenticator_class = 'pam'`
#c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
#c.JupyterHub.base_url = '/'
#c.JupyterHub.bind_url = 'http://:8000'
#c.JupyterHub.cleanup_proxy = True
#c.JupyterHub.cleanup_servers = True
#c.JupyterHub.concurrent_spawn_limit = 100
#c.JupyterHub.config_file = 'jupyterhub_config.py'
#c.JupyterHub.confirm_no_ssl = False
#c.JupyterHub.cookie_max_age_days = 14
#c.JupyterHub.cookie_secret = b''
#c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'
#c.JupyterHub.data_files_path = '/opt/conda/share/jupyterhub'
#c.JupyterHub.db_kwargs = {}
#c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'
#c.JupyterHub.debug_db = False
#c.JupyterHub.debug_proxy = False
#c.JupyterHub.default_server_name = ''
#c.JupyterHub.default_url = ''
#c.JupyterHub.external_ssl_authorities = {}
#c.JupyterHub.extra_handlers = []
#c.JupyterHub.extra_log_file = ''
#c.JupyterHub.extra_log_handlers = []
#c.JupyterHub.generate_certs = False
#c.JupyterHub.generate_config = False
#c.JupyterHub.hub_bind_url = ''
#c.JupyterHub.hub_connect_ip = ''
#c.JupyterHub.hub_connect_port = 0
#c.JupyterHub.hub_connect_url = ''
#c.JupyterHub.hub_ip = '127.0.0.1'
#c.JupyterHub.hub_port = 8081
#c.JupyterHub.init_spawners_timeout = 10
#c.JupyterHub.internal_certs_location = 'internal-ssl'
#c.JupyterHub.internal_ssl = False
#c.JupyterHub.ip = ''
#c.JupyterHub.jinja_environment_options = {}
#c.JupyterHub.last_activity_interval = 300
#c.JupyterHub.load_groups = {}
#c.JupyterHub.logo_file = ''
#c.JupyterHub.named_server_limit_per_user = 0
#c.JupyterHub.pid_file = ''
#c.JupyterHub.port = 8000
#c.JupyterHub.proxy_api_ip = ''
c.JupyterHub.proxy_api_ip = '127.0.0.1'
#c.JupyterHub.proxy_api_port = 0
c.JupyterHub.proxy_api_port = 8888
#c.JupyterHub.proxy_auth_token = ''
#c.JupyterHub.proxy_check_interval = 30
#              e.g. `c.JupyterHub.proxy_class = 'traefik'`
#c.JupyterHub.proxy_class = 'jupyterhub.proxy.ConfigurableHTTPProxy'
#c.JupyterHub.proxy_cmd = []
#c.JupyterHub.recreate_internal_certs = False
#c.JupyterHub.redirect_to_server = True
#c.JupyterHub.reset_db = False
#c.JupyterHub.service_check_interval = 60
#c.JupyterHub.service_tokens = {}
#c.JupyterHub.services = []
#c.JupyterHub.shutdown_on_logout = False
#              e.g. `c.JupyterHub.spawner_class = 'localprocess'`
#c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
#c.JupyterHub.ssl_cert = ''
#c.JupyterHub.ssl_key = ''
#c.JupyterHub.statsd_host = ''
#c.JupyterHub.statsd_port = 8125
#c.JupyterHub.statsd_prefix = 'jupyterhub'
#c.JupyterHub.subdomain_host = ''
#c.JupyterHub.template_paths = []
#c.JupyterHub.template_vars = {}
#c.JupyterHub.tornado_settings = {}
#c.JupyterHub.trust_user_provided_tokens = False
#c.JupyterHub.trusted_alt_names = []
#c.JupyterHub.trusted_downstream_ips = []
#c.JupyterHub.upgrade_db = False
#c.JupyterHub.user_redirect_hook = None
#c.Spawner.args = []
#      c.Spawner.auth_state_hook = userdata_hook
#c.Spawner.auth_state_hook = None
#c.Spawner.cmd = ['jupyterhub-singleuser']
#c.Spawner.consecutive_failure_limit = 0
#c.Spawner.cpu_guarantee = None
#c.Spawner.cpu_limit = None
#c.Spawner.debug = False
c.Spawner.default_url = 'lab'
#c.Spawner.disable_user_config = False
#c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']
#c.Spawner.environment = {}
#c.Spawner.http_timeout = 30
#c.Spawner.ip = ''
#c.Spawner.mem_guarantee = None
#c.Spawner.mem_limit = None
#c.Spawner.notebook_dir = ''
#c.Spawner.options_form = traitlets.Undefined
#c.Spawner.poll_interval = 30
#c.Spawner.port = 0
#c.Spawner.post_stop_hook = None
#      c.Spawner.pre_spawn_hook = my_hook
#c.Spawner.pre_spawn_hook = None
#c.Spawner.ssl_alt_names = []
#c.Spawner.ssl_alt_names_include_local = True
#c.Spawner.start_timeout = 60
#c.Authenticator.admin_users = set()
#c.Authenticator.auth_refresh_age = 300
#c.Authenticator.auto_login = False
#c.Authenticator.blacklist = set()
#  include things like authentication tokens, etc. to be passed to Spawners as
#c.Authenticator.enable_auth_state = False
#      c.Authenticator.post_auth_hook = my_hook
#c.Authenticator.post_auth_hook = None
#c.Authenticator.refresh_pre_spawn = False
#c.Authenticator.username_map = {}
#c.Authenticator.username_pattern = ''
#c.Authenticator.whitelist = set()
#c.CryptKeeper.keys = []
#c.CryptKeeper.n_threads = 2

# for outhenticator
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
print("load file")
c.Authenticator.auto_login = True