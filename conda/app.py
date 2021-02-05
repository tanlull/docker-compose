from fastapi import FastAPI
import thaiaddress

app = FastAPI()

@app.get("/")
async def main(addr : str):
    result = thaiaddress.parse(addr)
    #print(result)
    return result