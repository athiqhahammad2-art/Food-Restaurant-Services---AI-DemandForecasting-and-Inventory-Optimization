import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from streamlit_app import load_input_data, prepare_dataframe


def test_load_sample_data_returns_dataframe():
    df = load_input_data("Use sample data", uploaded_file=None, sample_days=60)

    assert df is not None
    assert list(df.columns) == ["date", "quantity_sold"]
    assert len(df) == 60


def test_load_upload_data_without_file_returns_none():
    df = load_input_data("Upload CSV", uploaded_file=None, sample_days=60)

    assert df is None


def test_prepare_dataframe_converts_and_sorts_dates():
    raw_df = pd.DataFrame(
        {
            "date": ["2024-01-03", "2024-01-01", "2024-01-02"],
            "quantity_sold": [10, 5, 7],
        }
    )

    cleaned_df = prepare_dataframe(raw_df)

    assert cleaned_df is not None
    assert cleaned_df["date"].tolist() == [
        pd.Timestamp("2024-01-01"),
        pd.Timestamp("2024-01-02"),
        pd.Timestamp("2024-01-03"),
    ]
    assert cleaned_df["quantity_sold"].tolist() == [5, 7, 10]
