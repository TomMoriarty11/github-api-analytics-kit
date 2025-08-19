# Architecture Overview

# Purpose
This project provides a modular framework for extracting and analyzing GitHub repository data using Python.

# Structure

`core/`: API wrapper and fetcher logic
 `utils/`: Profiling, aggregation, logging
 `config/`: Centralized endpoint definitions
 `notebooks/`: Interactive analysis
 `data/`: Sample responses for offline testing
 `docs/`: Documentation and usage scenarios

# Flow Diagram
Load token from `.env`
Initialize `GitHubAPI` wrapper
Fetch data via endpoints
Profile and aggregate using `utils/`
Log activity with `logger.py`
Analyze in notebook or export to dashboard
