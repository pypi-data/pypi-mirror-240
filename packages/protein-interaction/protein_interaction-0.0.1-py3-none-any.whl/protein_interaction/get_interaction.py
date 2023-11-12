import requests
import pandas as pd

def get_interactions_df(network_type, proteins=[]):
    protein_all_url = "%0d".join(proteins)
    data = requests.get("https://string-db.org/api/json/interaction_partners?identifiers="+protein_all_url+"&limit=1000&network_type="+network_type+"&species=9606")
    data = data.json()

    # Create a dictionary to store the connections
    connections = {}

    # Iterate through the data
    for entry in data:
        source = entry["preferredName_A"]
        target = entry["preferredName_B"]
        if source in proteins and target in proteins:
            if source not in connections:
                connections[source] = set()

            connections[source].add(target)

    # Find connections in the first layer and count
    first_layer_connections = {}
    first_layer_counts = {}
    for source, targets in connections.items():
        first_layer_connections[source] = targets.copy()
        first_layer_connections[source].discard(source)  # Remove self-connection
        first_layer_counts[source] = len(first_layer_connections[source])

    # Find connections in the second layer and count
    second_layer_connections = {}
    second_layer_counts = {}
    for source, targets in first_layer_connections.items():
        second_layer_targets = set()
        for target in targets:
            second_layer_targets.update(first_layer_connections.get(target, set()))
        second_layer_connections[source] = second_layer_targets
        second_layer_connections[source].discard(source)  # Remove self-connection
        second_layer_counts[source] = len(second_layer_connections[source])

    # Create a DataFrame
    df_data = {
        'protein': list(first_layer_connections.keys()),
        'first_layer_connection_count': list(first_layer_counts.values()),
        'second_layer_connection_count': list(second_layer_counts.values())
    }
    df = pd.DataFrame(df_data)

    return df



def get_visualizations(network_type, proteins=[]):
    protein_all_url = "%0d".join(proteins)
    data = requests.get("https://string-db.org/api/json/interaction_partners?identifiers="+protein_all_url+"&limit=1000&network_type="+network_type+"&species=9606")
    data = data.json()

    # Create a dictionary to store the connections
    connections = {}

    # Iterate through the data
    for entry in data:
        source = entry["preferredName_A"]
        target = entry["preferredName_B"]
        if source in proteins and target in proteins:
            if source not in connections:
                connections[source] = set()

            connections[source].add(target)

    # Find connections in the first layer and count
    first_layer_connections = {}
    first_layer_counts = {}
    for source, targets in connections.items():
        first_layer_connections[source] = targets.copy()
        first_layer_connections[source].discard(source)  # Remove self-connection
        first_layer_counts[source] = len(first_layer_connections[source])

    # Find connections in the second layer and count
    second_layer_connections = {}
    second_layer_counts = {}
    for source, targets in first_layer_connections.items():
        second_layer_targets = set()
        for target in targets:
            second_layer_targets.update(first_layer_connections.get(target, set()))
        second_layer_connections[source] = second_layer_targets
        second_layer_connections[source].discard(source)  # Remove self-connection
        second_layer_counts[source] = len(second_layer_connections[source])
        
    import matplotlib.pyplot as plt

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))  # 1 row and 2 columns of subplots

    # Plot the first histogram in the left subplot
    first_layer_counts["Discovery"] = 15
    x_labels = list(first_layer_counts.keys())
    counts = list(first_layer_counts.values())
    axes[0].bar(x_labels, counts)
    axes[0].set_xlabel("Gene Id")
    axes[0].set_ylabel("Interaction Count")
    axes[0].set_xticklabels(x_labels, rotation=45, ha="right")
    axes[0].set_title("Histogram of First layer Counts - "+network_type+" Type")

    # Plot the second histogram in the right subplot
    second_layer_counts["Discovery"] = 15
    x_labels = list(second_layer_counts.keys())
    counts = list(second_layer_counts.values())
    axes[1].bar(x_labels, counts, color='green')
    axes[1].set_xlabel("Gene Id")
    # axes[1].set_ylabel("Interaction Count")
    axes[1].set_xticklabels(x_labels, rotation=45, ha="right")
    axes[1].set_title("Histogram of Second layer Counts - "+network_type+" Type")

    # Adjust the layout to prevent overlap
    plt.tight_layout()

    # Show the figure with subplots
    plt.show()

    