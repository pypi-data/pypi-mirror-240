import click

from packages import process_module
from packages import run_tests_module

@click.group(
        help="""
        Collection of utilities to help convert dbt projects into Ascend dataflows.
        """)
def cli():
    pass
@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
@click.option('--default-seed', required=False, help='Default seed to connect hanging models to. Defaults to one of the nodes in the dataflow.')
def merge(manifest_file, hostname, data_service, dataflow, default_seed):
    """Process the compiled dbt manifest and SQL files and create/update/delete Ascend dataflow transforms."""
    process_module.merge_cmd(manifest_file, hostname, data_service, dataflow, default_seed)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def update_sql(manifest_file, hostname, data_service, dataflow):
    """Update the SQL of existing Ascend dataflow transforms."""
    process_module.update_sql_cmd(manifest_file, hostname, data_service, dataflow)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def delete(manifest_file, hostname, data_service, dataflow):
    """Delete all dbt models from an Ascend dataflow."""
    process_module.delete_cmd(manifest_file, hostname, data_service, dataflow)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def validate(manifest_file, hostname, data_service, dataflow):
    """Validate the seeds and sources are present in the dataflow."""
    process_module.validate_cmd(manifest_file, hostname, data_service, dataflow)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
def show(manifest_file):
    """Show the dependencies of dbt models."""
    process_module.show_cmd(manifest_file)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def deploy_tests(manifest_file, hostname, data_service, dataflow):
    """Create and run all dbt tests against the deployed models in Ascend."""
    run_tests_module.deploy_tests_cmd(manifest_file, hostname, data_service, dataflow)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def delete_tests(manifest_file, hostname, data_service, dataflow):
    """Delete all dbt tests against the deployed models in Ascend."""
    run_tests_module.delete_tests_cmd(manifest_file, hostname, data_service, dataflow)

@click.command()
@click.option('--manifest-file', required=True, help='Path to the manifest JSON file.')
@click.option('--hostname', required=True, help='Ascend hostname')
@click.option('--data-service', required=True, help='Ascend data service name')
@click.option('--dataflow', required=True, help='Ascend dataflow name')
def check_test_results(manifest_file, hostname, data_service, dataflow):
    """Check the results of all dbt tests against the deployed models in Ascend."""
    run_tests_module.check_test_results_cmd(manifest_file, hostname, data_service, dataflow)

cli.add_command(merge)
cli.add_command(delete)
cli.add_command(validate)
cli.add_command(show)
cli.add_command(deploy_tests)
cli.add_command(delete_tests)
cli.add_command(check_test_results)
cli.add_command(update_sql)

if __name__ == "__main__":
    cli(prog_name='ascend_dbt_transform')