from ascend.sdk import definitions
from ascend.sdk.applier import DataflowApplier
from ascend.sdk.client import Client

from .manifest_utils import _load_manifest, _get_nodes_and_dependencies
from .transform_utils import _create_transform, _translate_sql

# This is currently only handling models and seeds
# TODO: handle the rest of dbt structures, such as tests, sources, etc.
def show_cmd(manifest_file):
    """
    Load and parse manifest JSON file and print the dependencies of dbt models.
    """
    # Load and parse manifest JSON file
    manifest = _load_manifest(manifest_file)
    nodes, dependencies = _get_nodes_and_dependencies(manifest)

    # Print nodes in topological order
    for node in nodes:
        print(f"\nNode: {node}. Depends on:")
        for dependency in dependencies[node]:
            print(f"  -> {dependency}")

def merge_cmd(manifest_file, hostname, data_service, dataflow, default_seed):
    """
    Merge dbt models into an Ascend dataflow.
    """
    # Create Ascend Client
    client = Client(hostname)

    # Get existing nodes in dataflow
    existing_nodes = client.list_dataflow_components(data_service_id=data_service, dataflow_id=dataflow, deep=True).data
    existing_node_ids = [node.id for node in existing_nodes]

    # Load and parse manifest JSON file
    manifest = _load_manifest(manifest_file)
    nodes, dependencies = _get_nodes_and_dependencies(manifest=manifest, default_seed=existing_node_ids[0] if default_seed is None else default_seed)

    # Ensure seed nodes present in the manifest are present in the dataflow. Exit if not.
    for node_str in nodes:
        if hasattr(manifest['nodes'], node_str) and manifest['nodes'][node_str]['resource_type'] in ['seed', 'source']:
            node = node_str.split('.')[-1]
            if node not in existing_node_ids:
                print(f"Seed node {node} is not present in the dataflow. Please add it manually and try again.")
                exit(1)

    # For every "model" node create a component
    components = []
    for node_str in nodes:

        # Skip if node is not a model
        if node_str.split('.')[0] != 'model':
            continue

        node = node_str.split('.')[-1]
        # Create component
        component = _create_transform(
            id=node, 
            sql=_get_compiled_sql(manifest=manifest, node_str=node_str), 
            inputs=dependencies[node_str],
            description=_get_description(manifest=manifest, node_str=node_str)
        )
        # Add component to list of existing nodes
        components.append(component)

    # Get dataflow definition
    dataflow_def = client.get_dataflow(data_service_id=data_service, dataflow_id=dataflow).data

    # Perform a non-deleting append
    applier = DataflowApplier(client)
    applier.apply(data_service_id=data_service, dataflow=definitions.Dataflow(id=dataflow_def.id, name=dataflow_def.name, components=components), delete=False, dry_run=False)

def delete_cmd(manifest_file, hostname, data_service, dataflow):
    """
    Delete dbt models from Ascend dataflow.
    """
    # Create Ascend Client
    client = Client(hostname)

    # Load and parse manifest JSON file
    manifest = _load_manifest(manifest_file)
    nodes, _ = _get_nodes_and_dependencies(manifest=manifest)

    # Remove all nodes from the list of existing nodes in reverse order
    node_ids = [node.split('.')[-1] for node in reversed(nodes) if node.split('.')[0] == 'model']
    for node in node_ids:
        print(f"Deleting transform {node}")
        client.delete_transform(data_service_id=data_service, dataflow_id=dataflow, id=node)

def validate_cmd(manifest_file, hostname, data_service, dataflow):
    """
    Validate the seeds are present in the dataflow.
    """
    # Create Ascend Client
    client = Client(hostname)

    # Load and parse manifest JSON file
    manifest = _load_manifest(manifest_file)
    nodes, _ = _get_nodes_and_dependencies(manifest=manifest)

    # Validate the seeds are present in the dataflow
    node_ids = [node.split('.')[-1] for node in nodes if node.split('.')[0] in ['seed', 'source']]

    # Get existing nodes in dataflow
    existing_nodes = client.list_dataflow_components(data_service_id=data_service, dataflow_id=dataflow, deep=True).data
    existing_node_ids = [node.id for node in existing_nodes]

    # Print the list of nodes present and absent in the dataflow
    print("Nodes present in the dataflow:")
    for node in node_ids:
        if node in existing_node_ids:
            print(f"  {node}")
    print("Nodes absent in the dataflow:")
    for node in node_ids:
        if node not in existing_node_ids:
            print(f"  {node}")


def update_sql_cmd(manifest_file, hostname, data_service, dataflow):
    """
    Update the SQL of existing Ascend dataflow transforms.
    """

    # Create Ascend Client
    client = Client(hostname)

    # Load and parse manifest JSON file
    manifest = _load_manifest(manifest_file)
    nodes, dependencies = _get_nodes_and_dependencies(manifest=manifest)

    # For every node, if there is a transform with the same name, update the SQL. Otherwise, display a message.
    for node_str in nodes:
        node_type = node_str.split('.')[0]

        if node_type != 'model':
            continue

        node = node_str.split('.')[-1]
        input_ids = [node.split('.')[-1] for node in dependencies[node_str]]
        print(f"Updating SQL of the transform {node}")
        try:
            transform_body = client.get_transform(data_service_id=data_service, dataflow_id=dataflow, id=node).data
            transform_body.view.operator.spark_function.executable.code.source.inline = _translate_sql(_get_compiled_sql(manifest=manifest, node_str=node_str), input_ids)
            client.update_transform(data_service_id=data_service, dataflow_id=dataflow, transform_id=node, body=transform_body)
        except Exception as e:
            print(f"Could not update transform {node}. Error: {e}") 


def _get_compiled_sql(manifest, node_str):
    """
    Get compiled SQL from manifest.
    """
    return manifest['nodes'][node_str]['compiled_code']

def _get_description(manifest, node_str):
    """
    Get description from manifest.
    """
    return manifest['nodes'][node_str].get('description', '')
