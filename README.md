# Top 10 Skills Analyzer

## Overview

The Top 10 Skills Analyzer is a Streamlit-based web application that analyzes job postings data to identify the most frequently mentioned skills for specific job positions. This tool provides valuable insights for job seekers, recruiters, and anyone interested in understanding the current job market trends.

The data is sourced from the "1.3M Linkedin Jobs & Skills (2024)" dataset, offering a comprehensive and up-to-date view of the job market.

## Features

- Search for any job position
- Display top skills (5, 10, 20, 30, or 50) for the selected job position
- Interactive and user-friendly interface
- Data visualization of skill frequency (optional bar chart)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/top-10-skills.git
   cd top-10-skills
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the dataset file `job_and_skills.csv` in the same directory as the script.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Enter a job position in the text input field.

5. Select the number of top skills you want to see using the buttons.

6. Click "Analyze Skills" to view the results.

## Data Source

The data used in this project is sourced from the "1.3M Linkedin Jobs & Skills (2024)" dataset. Please ensure you have the rights to use this dataset and comply with any associated terms and conditions.

## Contributing

Contributions to improve the Top 10 Skills Analyzer are welcome! Please feel free to submit a Pull Request.


## Acknowledgments

- Streamlit for providing an excellent framework for building data apps
- Contributors to the pandas and plotly libraries
- LinkedIn for the original job postings data
