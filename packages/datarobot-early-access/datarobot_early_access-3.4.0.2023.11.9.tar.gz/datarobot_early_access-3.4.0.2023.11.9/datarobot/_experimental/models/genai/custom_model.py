#
# Copyright 2023 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
from __future__ import annotations

from typing import Optional, Union

import trafaret as t

from datarobot._experimental.models.genai.llm_blueprint import LLMBlueprint
from datarobot.models.api_object import APIObject


def get_entity_id(entity: Union[LLMBlueprint, str]) -> str:
    """
    Get the entity ID from the entity parameter.

    Parameters
    ----------
    entity : ApiObject or str
        May be entity ID or the entity.

    Returns
    -------
    id : str
        Entity ID
    """
    if isinstance(entity, str):
        return entity

    return entity.id


custom_model_trafaret = t.Dict(
    {
        t.Key("custom_model_id"): t.String,
    }
).ignore_extra("*")


class CustomModel(APIObject):
    """
    Metadata for a DataRobot generative AI custom model registered from an LLM blueprint.

    Attributes
    ----------
    custom_model_id : str
        The ID of the registered custom model.
    """

    _path = "api-gw/genai/customModelVersions"

    _converter = custom_model_trafaret

    def __init__(
        self,
        custom_model_id: str,
    ):
        self.custom_model_id = custom_model_id

    @classmethod
    def create(
        cls,
        llm_blueprint: Union[LLMBlueprint, str],
        prompt_column_name: Optional[str] = None,
        target_column_name: Optional[str] = None,
    ) -> CustomModel:
        """
        Create a new CustomModel. This registers a custom model from an LLM blueprint.

        Parameters
        ----------
        llm_blueprint : LLMBlueprint or str
            The LLM blueprint associated with the created chat prompt.
            Accepts LLM blueprint or ID.
        prompt_column_name : str, optional
            The column name of the prompt text.
        target_column_name : str, optional
            The column name of the response text.

        Returns
        -------
        custom_model : CustomModel
            The created custom model.
        """
        payload = {
            "llm_blueprint_id": get_entity_id(llm_blueprint),
            "prompt_column_name": prompt_column_name,
            "target_column_name": target_column_name,
        }

        # TODO: Add option to wait_for_completion
        url = f"{cls._client.domain}/{cls._path}/"
        r_data = cls._client.post(url, data=payload)
        return cls.from_server_data(r_data.json())
