import logging

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "name,command_list",
    [
        (
            "Sort bedfile",
            [
                "import pandas as pd",
                "import pybedtools"
                "x = pd.DataFrame([['chr10', 123, 235], ['chr1', 123, 235]])",
                "bed = pybedtools.BedTool.from_dataframe(x)",
                "print(bed.sort())"
            ]
        ),
    ],
)
def test_pybedtools(container, name, command_list):
    """Basic pandas tests"""
    LOGGER.info(f"Testing pybedtools: {name} ...")
    command = ';'.join(command_list)
    c = container.run(tty=True, command=["start.sh", "python", "-c", command])
    rv = c.wait(timeout=30)
    assert rv == 0 or rv["StatusCode"] == 0, f"Command {command} failed"
    logs = c.logs(stdout=True).decode("utf-8")
    LOGGER.debug(logs)
