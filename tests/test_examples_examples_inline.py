import logging

from typer.testing import CliRunner

from datacontract.cli import app
from datacontract.data_contract import DataContract

runner = CliRunner()

logging.basicConfig(level=logging.DEBUG, force=True)


def test_cli():
    result = runner.invoke(app, ["test", "--examples", "./examples/examples/datacontract_inline.yaml"])
    assert result.exit_code == 0


def test_json_inline():
    data_contract = DataContract(data_contract_file="examples/examples/datacontract_inline.yaml", examples=True)
    run = data_contract.test()
    print(run)
    print(run.result)
    assert run.result == "passed"
