from logging import basicConfig, WARNING, INFO


def logs_config(
    file_path: str | None = None,
    verbose: bool = None
) -> None:
    basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='[%m/%d/%Y %I:%M:%S %p]',
        encoding='utf-8',
        level=INFO if verbose else WARNING,
        filename=file_path,
    )
