import json
import zoneinfo
from datetime import datetime

import click
import requests
from gql import gql
from jsonschema import ValidationError, validate

from .auth import get_auth_token
from .util import (
    RUN_SCHEMA_PATH,
    be_host,
    display_error_and_exit,
    get_client,
    fe_host,
    list_test_suites,
    prompt_user_for_suite,
)


@click.group()
def run():
    """
    Commands relating to starting or viewing runs
    """
    pass


@click.command()
@click.argument("config-file", type=click.File("r"), required=True)
def start(config_file: bool):
    """
    Start a new run of a test suite.

    Optionally, if the test suite was defined with "fixed_output" fields
    and if the --use-fixed-output flag is passed, then it will
    use a fixed set of outputs instead of querying the model under test.
    This is useful to evaluate the performance of the evaluator itself.
    """
    try:
        parameters = json.load(config_file)
    except Exception:
        display_error_and_exit("Config file was not valid JSON")

    try:
        with open(RUN_SCHEMA_PATH, "r") as f:
            schema = json.load(f)
            validate(instance=parameters, schema=schema)
    except ValidationError as e:
        display_error_and_exit(
            f"Config file provided did not conform to JSON schema. Message: {e.message}"
        )

    suiteid = prompt_user_for_suite()

    response = requests.post(
        url=f"{be_host()}/start_run/",
        headers={"Authorization": get_auth_token()},
        json={"test_suite_id": suiteid, "parameters": parameters},
    )

    if response.status_code == 200:
        run_id = response.json()["run_id"]
        click.secho("Successfully started run.", fg="green")
        click.secho(f"{fe_host()}/results?run_id={run_id}", bold=True)
    else:
        click.secho("Could not start run", fg="red")


@click.command()
@click.option(
    "--show-archived",
    is_flag=True,
    show_default=True,
    default=False,
    help="When enabled, archived runs are displayed in the output",
)
def list_results(show_archived: bool):
    """
    Display a list of run results.
    """
    query = gql(
        f"""
        query MyQuery {{
          runs(archived: {"null" if show_archived else "false"}) {{
            passPercentage
            status
            runId
            textSummary
            timestamp
            archived
            parameters
            testSuite {{
              title
            }}
          }}
        }}
    """
    )
    results = get_client().execute(query)
    click.secho(
        f"{'Title':30} {'Timestamp':24} {'Status':13} {'Pass %':8} {'Archived':9}",
        bold=True,
    )
    for result in results["runs"]:
        # print(zoneinfo.available_timezones())
        localtz = datetime.now().astimezone().tzinfo  # zoneinfo.ZoneInfo("localtime")

        timestamp = datetime.strptime(
            result["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z"
        ).astimezone(localtz)
        # Print the timestamp in our own arbitrary format
        timestamp_str = datetime.strftime(timestamp, "%Y-%m-%d %H:%M %Z")
        click.secho(
            f"{result['testSuite']['title']:30} {timestamp_str:24} {result['status']:13} {result['passPercentage'] * 100:<8.2f} {'yes' if result['archived'] else 'no':10}",
        )


run.add_command(start)
run.add_command(list_results)
