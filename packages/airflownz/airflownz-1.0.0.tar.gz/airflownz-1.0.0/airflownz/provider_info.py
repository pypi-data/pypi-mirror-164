def get_provider_info():
    return {
        "package-name": "airflownz",
        "name": "netezza",
        "description": "Airflow Hook for Netezza",
        "hook-class-names": [
            "airflownz.hooks.netezza.NetezzaHook",
        ],
        "connection-types": [
            {'connection-type': "netezza", 'hook-class-name': "airflownz.hooks.netezza.NetezzaHook"}
        ],
        "extra-links": [
            "airflownz.operators.netezza.NetezzaOperator"
        ]
    }
