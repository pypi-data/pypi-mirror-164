def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-y42demo",
        "name": "Y42demo",
        "description": "Y42demo",
        "versions": [
            "1.0.32",
        ],
        "dependencies": [
            "apache-airflow>=2.2.0",
        ],
        "sensors": [
            {
                "integration-name": "Orchestration",
                "python-modules": ["airflow.providers.y42demo.sensors.orchestration"],
            },
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.y42demo.hooks.orchestration.OrchestrationHttpHook",
                "connection-type": "y42demo_orchestration",
            },
        ],
    }
