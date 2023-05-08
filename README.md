# Sustainable Logistics and Digitalization: Wind Turbine Placement Optimization in Switzerland

This project aims to optimize the placement of wind turbines in Switzerland by considering various geographical parameters and constraints. It's created as a project for the course Sustainable Logistics and Digitalization in a master in Sustainable Management and Technology at IMD x HEC-Lausanne x EPFL. Utilizing geospatial data and optimization tools (Google OR tools), we aim to provide a sustainable solution that aligns with the Paris Agreement Policies and meets the Swiss energy requirements for 2050.

## Table of Contents

- [Sustainable Logistics and Digitalization: Wind Turbine Placement Optimization in Switzerland](#sustainable-logistics-and-digitalization-wind-turbine-placement-optimization-in-switzerland)
	- [Table of Contents](#table-of-contents)
	- [Introduction](#introduction)
	- [Collaborators](#collaborators)
	- [Requirements](#requirements)
	- [Installation](#installation)
	- [Usage](#usage)
	- [Data Sources](#data-sources)
	- [Contributing](#contributing)
	- [Methodology](#methodology)
	- [Results](#results)
	- [Future Work](#future-work)

## Introduction

As the demand for renewable energy grows, efficient wind turbine placement becomes crucial for maximizing power generation and minimizing the environmental impact. This project focuses on optimizing wind turbine placements in Switzerland using geospatial data containing various parameters such as distance to the nearest city, national park, UNESCO natural heritage area, and other relevant constraints. We leverage Google's OR-Tools to optimize the placement while taking into account the geospatial constraints.

## Collaborators
- [David Campbell](https://github.com/davdavDTB) 
- [Paula Ramirez Ortega](https://github.com/Pramirezortega) 
- [Noé Lopez](https://github.com/noelopez-E4S)
- [Min Yi Chen](https://github.com/jessicaminyi)
- [Per Christian Wessel](https://github.com/percw)

## Requirements

- Python 3.7 or higher
- Geopandas
- Google OR-Tools
- dbfread
- qgis

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```
If you are using anaconda you can run the following code:
```bash
conda install -r requirements.txt
```

## Usage

Our process and all results are captured by the notebook [Wind Optimization](https://github.com/percw/Swiss_wind-turbine_optimization/blob/main/wind_optimization.ipynb).

Clone this repository:

```bash
git clone https://github.com/percw/Swiss_wind-turbine_optimization.git
cd wind-turbine-placement-optimization
```

## Data Sources

The geospatial data used in this project is acquired from Swiss Federal Office of Topography (swisstopo)

## Contributing

We welcome contributions to this project. If you have an idea or a suggestion, please open an issue or submit a pull request.

1. Fork the repository and create a new branch.
2. Make your changes and commit them to your branch.
3. Submit a pull request and provide a clear description of your changes.

## Methodology

The methodology for this project can be broken down into the following steps:

1. **Data Preparation**: Acquire, clean, and preprocess geospatial data from swisstopo

2. **Constraint Processing**: Define the constraints for wind turbine placement, such as minimum distances from cities, protected areas, and other geographic features. Process the geospatial data to create a binary constraint matrix that represents the feasibility of each location.

3. **Optimization**: Utilize Google's OR-Tools to solve the optimization problem, taking into account the defined constraints and the objective function (maximizing power generation, minimizing environmental impact, etc.). Adjust parameters and constraints as needed to fine-tune the optimization process.

4. **Visualization**: Generate visualizations of the optimized wind turbine placements, including maps and charts displaying the location, power generation, and environmental impact of each turbine. This will help stakeholders better understand the results and make informed decisions.

5. **Sensitivity Analysis**: Perform sensitivity analysis to assess the robustness of the optimization results and the impact of changes in input parameters, constraints, or objectives.

6. **Documentation**: Provide clear and comprehensive documentation of the methodology, data sources, and codebase, enabling others to reproduce the results, modify the project for their own needs, or contribute to its development.

## Results

The results of this project will be presented in various formats, such as:

- **Optimized wind turbine locations**: A list of the optimal wind turbine placements, including coordinates and other relevant information.
- **Maps**: Interactive maps displaying the optimized wind turbine locations, along with the geospatial constraints and other geographic features.
- **Charts and tables**: Visualizations and summary statistics of the optimization results, including power generation, environmental impact, and other relevant metrics.
- **Sensitivity analysis**: A report detailing the sensitivity of the optimization results to changes in input parameters, constraints, or objectives.

These results will be useful for stakeholders in the renewable energy sector, such as energy companies, policymakers, and researchers, to make informed decisions about wind turbine placement and to better understand the trade-offs involved in optimizing for power generation and environmental impact.

## Future Work

Potential future work and improvements to the project include:

- Expanding the scope of the project to include other renewable energy sources, such as solar or hydropower.
- Incorporating more sophisticated optimization algorithms, such as genetic algorithms or machine learning techniques.
- Developing a user-friendly web application or tool that allows users to input their own geospatial data and constraints and obtain optimized results.
- Collaborating with stakeholders and experts in the renewable energy sector to refine the methodology and improve the practical relevance of the project.
