from typing import Union

from pydantic import BaseModel


class Features(BaseModel):
    user_id: str
    region: Union[str, None]
    tenure: Union[str, None]
    montant: Union[float, None]
    frequence_rech: Union[float, None]
    revenue: Union[float, None]
    arpu_segment: Union[float, None]
    frequence: Union[float, None]
    data_volume: Union[float, None]
    on_net: Union[float, None]
    orange: Union[float, None]
    tigo: Union[float, None]
    zone1: Union[float, None]
    zone2: Union[float, None]
    regularity: Union[float, None]
    top_pack: Union[str, None]
    freq_top_pack: Union[float, None]
