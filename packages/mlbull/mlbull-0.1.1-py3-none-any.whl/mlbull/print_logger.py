from logging import getLogger
from tempfile import TemporaryFile

logger = getLogger(__file__)


class PrintLogger:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self.formated_prefix = f"{prefix}:\t"
        self.output_buffer = TemporaryFile("w+", suffix="output")
        logger.debug(
            f"Creating logger for {prefix} with buffer {self.output_buffer.name}"
        )

    def __call__(self, *args, **kwargs):
        print(*args, **kwargs, file=self.output_buffer)
        new_args = [str(a).replace("\n", f"\n{self.formated_prefix}") for a in args]
        print(self.formated_prefix, *new_args, **kwargs)

    def get_logged_data(self):
        self.output_buffer.seek(0)
        return self.output_buffer.read()
