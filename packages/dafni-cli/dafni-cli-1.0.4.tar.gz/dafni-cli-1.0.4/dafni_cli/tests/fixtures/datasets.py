# Example response from the API for getting all datasets
TEST_DATASETS_DATA: dict = {
    "metadata": [
        {
            "id": {
                "dataset_uuid": "0a0a0a0a-0a00-0a00-a000-0a0a0000000a",
                "version_uuid": "0a0a0a0a-0a00-0a00-a000-0a0a0000000b",
                "metadata_uuid": "0a0a0a0a-0a00-0a00-a000-0a0a0000000c",
                "asset_id": "0a0a0a0a-0a00-0a00-a000-0a0a0000000a:0a0a0a0a-0a00-0a00-a000-0a0a0000000b:0a0a0a0a-0a00-0a00-a000-0a0a0000000c",
            },
            "title": "Title 1",
            "description": None,
            "subject": "Planning / Cadastre",
            "source": "DAFNI",
            "status": "ingested",
            "date_range": {"begin": None, "end": None},
            "modified_date": "2021-03-04T15:59:26+00:00",
            "auth": {
                "name": "Executor",
                "view": True,
                "read": True,
                "update": False,
                "destroy": False,
                "reason": "Accessed as part of the Public group",
            },
        },
        {
            "id": {
                "dataset_uuid": "1a0a0a0a-0a00-0a00-a000-0a0a0000000a",
                "version_uuid": "1a0a0a0a-0a00-0a00-a000-0a0a0000000b",
                "metadata_uuid": "1a0a0a0a-0a00-0a00-a000-0a0a0000000c",
                "asset_id": "1a0a0a0a-0a00-0a00-a000-0a0a0000000a:1a0a0a0a-0a00-0a00-a000-0a0a0000000b:1a0a0a0a-0a00-0a00-a000-0a0a0000000c",
            },
            "title": "Title 2",
            "description": "Description 2",
            "subject": "Environment",
            "source": "DAFNI Workflows",
            "status": "ingested",
            "date_range": {
                "begin": "2019-01-01T12:00:00.000Z",
                "end": "2021-01-01T12:00:00.000Z",
            },
            "modified_date": "2020-08-26T13:21:18.522Z",
            "formats": ["application/zip", None, "text/csv", "text/plain"],
            "auth": {
                "name": "Executor",
                "view": True,
                "read": True,
                "update": False,
                "destroy": False,
                "reason": "Accessed as part of the Public group",
            },
        },
    ],
    "filters": {
        "sources": {
            "Companies House": 1,
            "DAFNI": 1,
            "DAFNI Workflows": 1,
            "Newcastle University": 28,
            "Office for National Statistics": 455,
            "Office of Rail and Road": 2,
        },
        "subjects": {
            "Climatology / Meteorology / Atmosphere": 16,
            "Economy": 1,
            "Environment": 1,
            "Oceans": 2,
            "Planning / Cadastre": 1,
            "Society": 455,
            "Transportation": 10,
            "Utilities / Communication": 2,
        },
        "formats": {
            "text/plain": 1,
            "text/csv": 483,
            "application/zip": 2,
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": 3,
            "application/vnd.ms-excel": 1,
            "application/pdf": 1,
            "application/octet-stream": 3,
        },
    },
}
