# Project Description for protein-interaction

This is a Python package for getting interactions of proteins

## Installation

You can install the package using `pip`:

```bash
pip install protein-interaction
```
# Usage

## Import the package

```bash
import protein_interaction
from protein_interaction import get_interaction
```

## Generate df from protein List and network type

```bash
get_interaction.get_interactions_df("physical", ['P1', 'P2'])
get_interaction.get_interactions_df("colocalization", ['P1', 'P2'])
```

## Generate visualization from protein List and network type

```bash
get_interaction.get_visualizations("physical", ['P1', 'P2'])
get_interaction.get_visualizations("colocalization", ['P1', 'P2'])
```