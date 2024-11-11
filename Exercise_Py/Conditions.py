import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code-space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("We are in development mode")
elif current_env == PRODUCTION:
    print("We are in production mode")
elif current_env == STAGING:
    print("We are in staging mode")
elif current_env in [CODE_SPACE, LOCAL]:
    print("We are in code-space or local mode")
else:
    print("We are in an unknown mode")
