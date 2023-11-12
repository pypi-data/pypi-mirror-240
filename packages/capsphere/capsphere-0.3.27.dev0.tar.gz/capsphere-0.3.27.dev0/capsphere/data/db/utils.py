import os


def check_env_vars(env_vars, logger):
    """Checks if the required environment variables are set."""
    for var in env_vars:
        if os.getenv(var) is None:
            message = f"The environment variable {var} is not set. It is required for the database connection."
            logger.error(message)
            raise EnvironmentError(message)
