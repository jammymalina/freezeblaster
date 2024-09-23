DEFAULT_IGNORE_LIST = [
    "nose.plugins",
    "six.moves",
    "django.utils.six.moves",
    "google.gax",
    "threading",
    "multiprocessing",
    "queue",
    "selenium",
    "_pytest.terminal.",
    "_pytest.runner.",
    "gi",
    "prompt_toolkit",
]


class Settings:
    default_ignore_list: set[str]

    def __init__(self, default_ignore_list: list[str] | None = None) -> None:
        self.default_ignore_list = set(default_ignore_list or DEFAULT_IGNORE_LIST)


settings = Settings()


def configure(default_ignore_list: list[str] | None = None, extend_ignore_list: list[str] | None = None) -> None:
    if default_ignore_list is not None and extend_ignore_list is not None:
        settings.default_ignore_list = set([*default_ignore_list, *extend_ignore_list])
    if default_ignore_list is not None:
        settings.default_ignore_list = set(default_ignore_list)
    if extend_ignore_list:
        settings.default_ignore_list = set([*settings.default_ignore_list, *extend_ignore_list])


def reset_config() -> None:
    global settings
    settings = Settings()
