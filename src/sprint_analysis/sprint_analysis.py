"""
Sprint Analysis Module.

This module provides functionality to analyze sprint data from CSV files
and generate status reports.

Example:
    >>> from sprint_analysis import analyze_sprint_data
    >>> results = analyze_sprint_data('path/to/sprint_data.csv')
"""

import sys
from pathlib import Path
from typing import Any

import pandas as pd


def analyze_sprint_data(file_path: str | Path) -> dict[str, Any]:
    """
    Analyze sprint data from a CSV file and generate a status report.

    Args:
        file_path: Path to the CSV file containing sprint data.
                   Must be a valid CSV file with 'Status' column.

    Returns:
        A dictionary containing the analysis results with the following keys:
        - total_tickets: Total number of tickets analyzed
        - status_counts: Dictionary of status to ticket count
        - status_percentages: Dictionary of status to percentage

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the CSV file lacks required 'Status' column.
        pd.errors.ParserError: If the file cannot be parsed as valid CSV.
    """
    # Convert to Path object and resolve to absolute path for security
    path = Path(file_path).resolve()

    # Security: Validate file exists
    if not path.exists():
        raise FileNotFoundError(f"Sprint data file not found: {path}")

    # Security: Validate file is a CSV
    if path.suffix.lower() != '.csv':
        raise ValueError(f"Expected CSV file, got: {path.suffix}")

    # Security: Prevent path traversal by checking the resolved path is within allowed directory
    try:
        path.relative_to(Path.cwd())
    except ValueError:
        raise ValueError("File path traversal detected. Please use paths within the working directory.")

    # Read CSV with explicit encoding and validation
    try:
        df = pd.read_csv(path, encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback to latin-1 if UTF-8 fails
        df = pd.read_csv(path, encoding='latin-1')

    # Validate required columns exist
    required_columns = {'Status', 'Ticket ID'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Perform analysis
    total_tickets = len(df)
    if total_tickets == 0:
        return {
            'total_tickets': 0,
            'status_counts': {},
            'status_percentages': {}
        }

    # Count statuses and calculate percentages
    status_counts = df['Status'].value_counts().to_dict()
    status_percentages = {
        status: (count / total_tickets) * 100
        for status, count in status_counts.items()
    }

    # Generate and print report
    _print_report(total_tickets, status_counts, status_percentages)

    return {
        'total_tickets': total_tickets,
        'status_counts': status_counts,
        'status_percentages': status_percentages
    }


def _print_report(
    total_tickets: int,
    status_counts: dict[str, int],
    status_percentages: dict[str, float]
) -> None:
    """
    Print formatted sprint status report to stdout.

    Args:
        total_tickets: Total number of tickets.
        status_counts: Dictionary mapping status to ticket count.
        status_percentages: Dictionary mapping status to percentage.
    """
    # Use ASCII-safe characters for cross-platform compatibility
    print("\n" + "=" * 40)
    print("       SPRINT STATUS REPORT")
    print("=" * 40)
    print(f"Total Tickets: {total_tickets}")
    print("-" * 40)
    print("Status Breakdown:")
    print("-" * 40)

    # Sort by count descending for better readability
    sorted_statuses = sorted(
        status_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for status, count in sorted_statuses:
        percentage = status_percentages[status]
        bar_length = int(percentage / 5)  # Scale bar to 20 characters
        bar = "#" * bar_length
        print(f"{status:15} | {count:3} ({percentage:5.1f}%) {bar}")

    print("=" * 40 + "\n")


def _get_default_csv_path() -> Path:
    """
    Get the default path to sprint_data.csv relative to this script.

    Returns:
        Path to the default sprint data CSV file.
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.resolve()
    return script_dir / "sprint_data.csv"


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the sprint analysis script.

    Args:
        argv: Command line arguments. If None, uses sys.argv.
              First argument (if provided) is the path to the CSV file.

    Returns:
        Exit code: 0 for success, 1 for errors.
    """
    try:
        if argv is None:
            argv = sys.argv[1:]

        # Use provided path or default
        if argv:
            file_path = argv[0]
        else:
            file_path = _get_default_csv_path()

        analyze_sprint_data(file_path)
        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse CSV file: {e}", file=sys.stderr)
        return 1
    except PermissionError as e:
        print(f"Error: Permission denied accessing file: {e}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"Error: I/O error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
