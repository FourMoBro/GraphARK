from typing import List, Optional

from pydantic import BaseModel


class ETFBase(BaseModel):
    symbol: str
    description: Optional[str] = None

class ETFCreate(ETFBase):
    pass

class ETF(ETFBase):
    pass
        
