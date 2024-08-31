def is_headless():
    """Check if the environment is running in headless mode."""
    import os
    return os.environ.get("DISPLAY") is None
