from fastapi import APIRouter
from services import *

plfundsrisksrouter = APIRouter()


@plfundsrisksrouter.get("/",response_model=ResponseSchema)
async def get_plfundsrisk():
    plFundsRisk = {"message": "PLFundsRisks!"}
    return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk])


@plfundsrisksrouter.get("/all",response_model=ResponseSchema)
async def get_plfundsrisk_all():
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisks= await plFundsRisk.get_plfundsrisks_all()

        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=plFundsRisks)
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.get("/{date}",response_model=ResponseSchema)
async def get_plfundsrisk_data(date: str):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.get_plfundsrisks_data(date)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.post("/createpldatesummary",response_model=ResponseSchema)
async def create_spread_data(spread: SpreadsSchemaIn):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.create(spread)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)

@plfundsrisksrouter.put("/updatepldatesummary",response_model=ResponseSchema)
async def update_spread_data(spread: SpreadsSchemaOut):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.update(spread)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)


@plfundsrisksrouter.delete("/deletepldatesummary",response_model=ResponseSchema)
async def delete_spread_data(spreadid: int):
    try:
        plFundsRisk = await AlgoPLFundsRisk(settings.Broker,settings.UserId)
        plFundsRisk_data = await plFundsRisk.delete(spreadid)
        return ResponseSchema(status='success', code='plfundsrisk', description='ok', data=[plFundsRisk_data])
    except Exception as e:
        return exception_handler(e)