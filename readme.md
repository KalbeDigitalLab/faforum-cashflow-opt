# Agent-Based Cashflow Optimization Simulation Model

This project is a FastAPI-based web application that allows users to:
1. Set parameters for a simulation.
2. Run the simulation dynamically.
3. View results in an interactive table and charts.

## Features
- **Parameter Input**: Set custom parameters for the simulation.
- **Dynamic Simulation**: Run the simulation directly from the web interface.
- **Interactive Results**:
  - View results in a sortable and filterable table.
  - Analyze trends with interactive charts using Chart.js.
- **Minimalist Design**: Clean UI with a green theme and Roboto font.

## Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- PIP (Python package manager)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KalbeDigitalLab/faforum-cashflow-opt.git
   cd faforum-cashflow-opt
   ```

2. **Install Dependencies**:
   Install all required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the FastAPI application using Uvicorn:
   ```bash
   uvicorn app:app --reload
   ```

4. **Access the Web Interface**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## File Structure
```
simulation-results-viewer/
├── app.py                 # FastAPI application code
├── requirements.txt       # Python dependencies
├── static/                # Static assets (CSS, JS)
│   ├── css/
│   │   └── styles.css     # Styling for the web interface
│   └── js/
│       └── scripts.js     # JavaScript for interactivity
├── templates/             # HTML templates for the app
│   ├── parameters.html    # Parameter input form
│   └── results.html       # Results table and charts
├── nlogo-models/          # NetLogo models folder
│   └── cashflow-opt.nlogo # Current NetLogo model for the ABM
├── notebook/              # HTML templates for the app
│   └── simulation.ipynb   # For prototyping and testing the model
└── README.md              # Project documentation
```


## Usage
1. **Set Simulation Parameters**:
   - Input initial cash, sales price, cost per unit, and other parameters in the web interface.
   - Click "Run Simulation" to start the simulation.

2. **View Results**:
   - **Table**: View simulation results in a sortable table.
   - **Charts**: Analyze trends like sales, revenue, and inventory levels using interactive charts.

## Dependencies

All required packages are listed in `requirements.txt`. Main dependencies:
- **FastAPI**: Backend framework
- **Uvicorn**: ASGI server
- **Pandas**: Data manipulation
- **Chart.js**: Frontend charting library
- **Jinja2**: HTML templating

## Development

To modify or extend the application:
1. Edit `app.py` to add new simulation logic or routes.
2. Customize templates in the `templates/` folder for UI changes.
3. Use the `static/` folder for custom styles or JavaScript.