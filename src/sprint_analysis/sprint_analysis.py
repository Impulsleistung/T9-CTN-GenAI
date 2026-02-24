import pandas as pd

def analyze_sprint_data(file_path):
    """
    Analyzes dummy sprint data from a CSV file and prints a status report.
    """
    df = pd.read_csv(file_path)
    total_tickets = len(df)
    status_counts = df['Status'].value_counts()

    print("Sprint Status Report")
    print(f"Total Tickets: {total_tickets}")
    print("\nStatus Breakdown:")
    for status, count in status_counts.items():
        percentage = (count / total_tickets) * 100
        print(f"{status}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    analyze_sprint_data('sprint_data.csv')