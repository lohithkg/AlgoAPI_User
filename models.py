from sqlalchemy import Column, Integer, String, Float, Text, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SpreadsModel(Base):
    __tablename__ = 'trades_spreads'

    TradeId = Column(Integer, primary_key=True, autoincrement=True)
    Broker = Column(String(30), nullable=False)
    UserId = Column(String(30), nullable=False)
    Date = Column(String(10))
    Symbol = Column(String(255))
    Status = Column(String(30))
    ExpiryDate = Column(String(10))
    ExpiryType = Column(String(30))
    ProductType = Column(String(30))
    Exchange = Column(String(10))
    Segment = Column(String(30))
    TradeType = Column(String(30))
    Trend = Column(String(30))
    Spot_Price = Column(Float)
    Strike = Column(Float)
    Leg1_Strike = Column(Float)
    Leg1_Side = Column(String(30))
    Leg1_Symbol = Column(String(255))
    Leg1_Qty = Column(Integer)
    Leg1_BuyPrice = Column(Float)
    Leg1_BuyOrderId = Column(Integer)
    Leg1_SellPrice = Column(Float)
    Leg1_SellOrderId = Column(Integer)
    Leg1_Sl_Price = Column(Float)
    Leg1_Sl_OrderId = Column(Integer)
    Leg1_Tg_Price = Column(Float)
    Leg1_Tg_OrderId = Column(Integer)
    Leg1_Pnl = Column(Float)
    Leg2_Strike = Column(Float)
    Leg2_Side = Column(String(30))
    Leg2_Symbol = Column(String(255))
    Leg2_Qty = Column(Integer)
    Leg2_BuyPrice = Column(Float)
    Leg2_BuyOrderId = Column(Integer)
    Leg2_SellPrice = Column(Float)
    Leg2_SellOrderId = Column(Integer)
    Leg2_Sl_Price = Column(Float)
    Leg2_Sl_OrderId = Column(Integer)
    Leg2_Tg_Price = Column(Float)
    Leg2_Tg_OrderId = Column(Integer)
    Leg2_Pnl = Column(Float)
    Trade_StartTime = Column(String(30))
    Trade_EndTime = Column(String(30))
    Total_Premium = Column(Float)
    Total_Sl = Column(Float)
    LastPrice = Column(Float)
    LastPriceDate = Column(String(30))
    MarketValue = Column(Float)
    Strategy = Column(String(255))
    Instrument = Column(String(30))
    Pyramid = Column(Integer)
    UnderlyingSymbol = Column(String(255))
    TradeDuration = Column(String(30))
    SpreadNumber = Column(Integer)
    SpreadType = Column(String(30))
    SpreadStatus = Column(String(255))
    Pnl = Column(Float)
    Charges = Column(Float)
    PnlNet = Column(Float)
    Remarks = Column(String)

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class HedgesModel(Base):
    __tablename__ = 'trades_hedges'

    TradeId = Column(Integer, primary_key=True, autoincrement=True)
    Broker = Column(String(30), nullable=False)
    UserId = Column(String(30), nullable=False)
    Date = Column(String(10))
    Symbol = Column(String(255))
    Status = Column(String(30))
    ExpiryDate = Column(String(10))
    ExpiryType = Column(String(30))
    ProductType = Column(String(30))
    Exchange = Column(String(10))
    Segment = Column(String(30))
    OptionType = Column(String(30))
    Spot_Price = Column(Float)
    Strike = Column(Float)
    OrderSide = Column(String(30))
    Quantity = Column(Integer)
    BuyPrice = Column(Float)
    SellPrice = Column(Float)
    StopLossPrice = Column(Float)
    StopLossOrderID = Column(Float)
    TargetPrice = Column(Float)
    TargetOrderID = Column(Float)
    Trade_StartTime = Column(String(30))
    Trade_EndTime = Column(String(30))
    LastPrice = Column(Float)
    LastPriceDate = Column(String(30))
    MarketValue = Column(Float)
    Strategy = Column(String(255))
    Instrument = Column(String(30))
    UnderlyingSymbol = Column(String(255))
    Pnl = Column(Float)
    Charges = Column(Float)
    PnlNet = Column(Float)
    Remarks = Column(String)



class PLDateSummary(Base):
    __tablename__ = 'pl_date_summary'

    Broker = Column(String(30), primary_key=True)
    UserId = Column(String(30), primary_key=True)
    Date = Column(String(10), primary_key=True)
    Strategy = Column(String(255))
    Pnl = Column(Float)
    Charges = Column(Float)
    PnlNet = Column(Float)
    TradeType = Column(String(30))
    Brokerage = Column(Float)
    Slippage = Column(Float)
    ActualPnl = Column(Float)
    ActualCharges = Column(Float)
    ActualPnlNet = Column(Float)
    ActualBrokerage = Column(Float)


class PLFundsRisk(Base):
    __tablename__ = 'pl_funds_risk'

    Broker = Column(String(30), primary_key=True)
    UserId = Column(String(30), primary_key=True)
    DateTime = Column(String(30), primary_key=True)
    StartOfTheDayBalance = Column(Float)
    AvailableBalance = Column(Float)
    UtilizedBalance = Column(Float)
    UtilizationPercentage = Column(Float)
    UnrealizedProfit = Column(Float)
    RealizedProfit = Column(Float)
    PnlAmount = Column(Float)
    PnlPercentage = Column(Float)
    RiskAmount = Column(Float)
    RiskPercentage = Column(Float)





