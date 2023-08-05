from pydantic import BaseModel
from datetime import datetime
from typing import Dict


class AnnotationLabel(BaseModel):
    """This annotation label is the class that defines the contract
    of annotation labels for signals"""
    label_value: str
    parameters: Dict


class AnnotationLabelPayload(BaseModel):
    """This class gives all the context for an annotation of a signal
    in the persistence tables.
    """
    tenant_id: str
    edge_logical_id: str
    observation_timestamp: int
    label: AnnotationLabel
    version: str
    dataset_name: str
