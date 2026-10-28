
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "age": [20, 21, 22, 23, 24, 25, 26, 27],
    "score": [60, 65, 70, 72, 75, 78, 80, 82]
})

current_data = pd.DataFrame({
    "age": [35, 36, 37, 38, 39, 40, 41, 42],
    "score": [30, 35, 40, 42, 45, 48, 50, 52]
})

report = Report(metrics=[DataDriftPreset()])
snapshot = report.run(
    reference_data=reference_data,
    current_data=current_data
)

snapshot.save_html("monitoring_report.html")

print("Monitoring report generated successfully.")
