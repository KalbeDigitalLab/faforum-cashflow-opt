from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import random

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Function to simulate data based on user-defined parameters
def run_simulation(params):
    initial_cash = params["initial_cash"]
    base_sales_volume = params["base_sales_volume"]

    # Generate dynamic data
    data = []
    for time_period in range(1, 51):
        sales_volume = base_sales_volume + random.randint(-50, 50)
        revenue = sales_volume * params["sales_price"]
        variable_costs = sales_volume * params["cost_per_unit"]
        accounts_receivable = revenue * params["receivable_collection_rate"]
        accounts_payable = variable_costs * params["payable_payment_rate"]
        inventory_level = max(0, random.randint(500, 1500) - sales_volume)

        data.append({
            "Time Period": time_period,
            "Sales Volume": sales_volume,
            "Revenue": revenue,
            "Variable Costs": variable_costs,
            "Inventory Level": inventory_level,
            "Accounts Receivable": accounts_receivable,
            "Accounts Payable": accounts_payable,
        })

    # Create DataFrame and save to CSV for debugging
    df = pd.DataFrame(data)
    df.to_csv("simulation_results.csv", index=False)
    return df

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("parameters.html", {"request": request})

@app.post("/run", response_class=HTMLResponse)
async def run(request: Request,
              initial_cash: float = Form(...),
              sales_price: float = Form(...),
              cost_per_unit: float = Form(...),
              base_sales_volume: int = Form(...),
              receivable_collection_rate: float = Form(...),
              payable_payment_rate: float = Form(...)):
    # Capture parameters from the form
    params = {
        "initial_cash": initial_cash,
        "sales_price": sales_price,
        "cost_per_unit": cost_per_unit,
        "base_sales_volume": base_sales_volume,
        "receivable_collection_rate": receivable_collection_rate,
        "payable_payment_rate": payable_payment_rate,
    }

    # Run the simulation
    results_df = run_simulation(params)

    # Convert data to dictionary for the table
    table_data = results_df.to_dict(orient="records")
    return templates.TemplateResponse("results.html", {"request": request, "table_data": table_data})
