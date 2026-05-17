import logging

import subete


def setup_logging() -> None:
    logging.basicConfig(format="%(name)-20s | %(levelname)-8s | %(message)s", level=logging.INFO)
    subete.repo.logger.setLevel(logging.WARNING)  # Reduce the noise of subete
