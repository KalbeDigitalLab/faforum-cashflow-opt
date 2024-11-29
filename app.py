from fastapi import FastAPI, Request, WebSocket, Form, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict, List
import pandas as pd
import random
import asyncio
import os

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

def generate_tick_data(params: Dict, tick: int) -> Dict:
    sales_volume = params["base_sales_volume"] + random.randint(-50, 50)
    revenue = sales_volume * params["sales_price"]
    variable_costs = sales_volume * params["cost_per_unit"]
    accounts_receivable = revenue * params["receivable_collection_rate"]
    accounts_payable = variable_costs * params["payable_payment_rate"]
    inventory_level = max(0, random.randint(500, 1500) - sales_volume)

    return {
        "Time Period": tick,
        "Sales Volume": sales_volume,
        "Revenue": revenue,
        "Variable Costs": variable_costs,
        "Inventory Level": inventory_level,
        "Accounts Receivable": accounts_receivable,
        "Accounts Payable": accounts_payable,
    }

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("parameters.html", {"request": request})

@app.post("/run", response_class=HTMLResponse)
async def run(
    request: Request,
    ticks: int = Form(...),
    initial_cash: float = Form(...),
    sales_price: float = Form(...),
    cost_per_unit: float = Form(...),
    base_sales_volume: int = Form(...),
    receivable_collection_rate: float = Form(...),
    payable_payment_rate: float = Form(...),
):
    params = {
        "initial_cash": initial_cash,
        "sales_price": sales_price,
        "cost_per_unit": cost_per_unit,
        "base_sales_volume": base_sales_volume,
        "receivable_collection_rate": receivable_collection_rate,
        "payable_payment_rate": payable_payment_rate,
    }
    return templates.TemplateResponse(
        "results.html", 
        {"request": request, "params": params, "ticks": ticks}
    )

@app.websocket("/ws/simulation")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        params = await websocket.receive_json()
        ticks = params.pop("ticks")
        
        results: List[Dict] = []
        for tick in range(1, ticks + 1):
            tick_data = generate_tick_data(params, tick)
            results.append(tick_data)
            await websocket.send_json(tick_data)
            await asyncio.sleep(0.5)
        
        df = pd.DataFrame(results)
        df.to_csv("simulation_results.csv", index=False)
        
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()

@app.get("/download")
async def download_data():
    if not os.path.exists("simulation_results.csv"):
        return {"error": "No simulation results found"}
    return FileResponse(
        "simulation_results.csv",
        media_type="text/csv",
        filename="simulation_results.csv"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)