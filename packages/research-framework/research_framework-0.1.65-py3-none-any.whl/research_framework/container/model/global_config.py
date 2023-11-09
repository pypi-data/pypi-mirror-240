from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from research_framework.base.model.base_utils import PyObjectId

class GlobalConfig(BaseModel):
    project_name: Optional[str] = None
    run_name: Optional[str] = None
    store: Optional[bool] = True
    overwrite: Optional[bool] = False
    log: Optional[bool] = True

    model_config = ConfigDict(
        arbitrary_types_allowed = True,
        populate_by_name = True
    )
