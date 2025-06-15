# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Literal
# import pandas as pd
# from docs_data import docs_data


# app = FastAPI()

# retail_data = {
#     ('UAE', 0.5): 13.41, ('UAE', 1.0): 13.41, ('UAE', 1.5): 18.15, ('UAE', 2.0): 18.15,
#     ('USA', 0.5): 43.00, ('USA', 1.0): 48.09, ('USA', 1.5): 53.18, ('USA', 2.0): 58.27,
#     ('UK', 0.5): 24.91, ('UK', 1.0): 24.91, ('UK', 1.5): 33.78, ('UK', 2.0): 33.78,
#     ('Canada', 0.5): 43.00, ('Canada', 1.0): 48.09, ('Canada', 1.5): 53.18, ('Canada', 2.0): 58.27,
#     ('Australia', 0.5): 39.61, ('Australia', 1.0): 45.97, ('Australia', 1.5): 52.34, ('Australia', 2.0): 58.71,
# }

# bigbox_data = {
#     ('UAE', 1): 17.0, ('UAE', 2): 21.0, ('UAE', 5): 29.8, ('UAE', 9): 46.0, ('UAE', 10): 50.8,
#     ('UAE', 15): 72.1, ('UAE', 20): 92.3, ('UAE', 23): 104.4, ('UAE', 25): 112.5,
#     ('UK', 1): 28.6, ('UK', 2): 35.8, ('UK', 5): 51.2, ('UK', 9): 80.1, ('UK', 10): 88.0,
#     ('UK', 15): 124.7, ('UK', 20): 167.9, ('UK', 23): 182.3, ('UK', 25): 196.7,
#     ('USA', 1): 44.3, ('USA', 2): 55.8, ('USA', 5): 94.0, ('USA', 9): 141.7, ('USA', 10): 154.3,
#     ('USA', 15): 221.7, ('USA', 20): 288.3, ('USA', 23): 299.9, ('USA', 25): 299.9,
# }

# class RateRequest(BaseModel):
#     country: str
#     weight: float
#     type: Literal['docs', 'non-docs']

# @app.post("/get-rate")
# async def get_rate(req: RateRequest):
#     if req.type == 'docs':
#         rate = docs_data.get((req.country, float(req.weight)))
#         discount = None
#     else:
#         rate = retail_data.get((req.country, float(req.weight)))
#         discount = bigbox_data.get((req.country, int(req.weight)))

#     return {
#         "country": req.country,
#         "weight": req.weight,
#         "document_type": req.type,
#         "retail_rate": rate,
#         "discount_rate": discount if discount is not None else "No discount available"
#     }

# @app.get("/all-rates")
# async def get_all_rates():
#     rates = []
#     for (country, weight), rate in docs_data.items():
#         rates.append({
#             "Country": country,
#             "Weight": weight,
#             "Type": "docs",
#             "Retail Rate": rate,
#             "Discount Rate": "No discount available"
#         })
#     for (country, weight), rate in retail_data.items():
#         discount = bigbox_data.get((country, int(weight)))
#         rates.append({
#             "Country": country,
#             "Weight": weight,
#             "Type": "non-docs",
#             "Retail Rate": rate,
#             "Discount Rate": discount if discount is not None else "No discount available"
#         })
#     return {"data": rates}

# @app.get("/download-excel")
# async def download_excel():
#     data = []
#     for (country, weight), rate in docs_data.items():
#         data.append({
#             "Country": country,
#             "Weight": weight,
#             "Type": "docs",
#             "Retail Rate": rate,
#             "Discount Rate": "No discount"
#         })
#     for (country, weight), rate in retail_data.items():
#         discount = bigbox_data.get((country, int(weight)))
#         data.append({
#             "Country": country,
#             "Weight": weight,
#             "Type": "non-docs",
#             "Retail Rate": rate,
#             "Discount Rate": discount if discount is not None else "No discount"
#         })
#     df = pd.DataFrame(data)
#     file_path = "/mnt/data/shipping_rates.xlsx"
#     df.to_excel(file_path, index=False)
#     return {"file_url": file_path}

# @app.get("/")
# async def read_root():
#     return {"message": "Shipping Rate API is up!"}
