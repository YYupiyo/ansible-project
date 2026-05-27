#!/usr/bin/env python3
import json
import sys

def main():
    inventory = {
        "staging": {
            "hosts": ["staging-1", "staging-2"],
            "vars": {
                "env": "staging",
                "app_port": 8080
            }
        },
        "production": {
            "hosts": ["prod-1", "prod-2"],
            "vars": {
                "env": "production",
                "app_port": 80
            }
        },
        "_meta": {
            "hostvars": {
                "staging-1": {"ansible_host": "192.168.1.10"},
                "staging-2": {"ansible_host": "192.168.1.11"},
                "prod-1": {"ansible_host": "10.0.1.10"},
                "prod-2": {"ansible_host": "10.0.1.11"}
            }
        }
    }
    
    if len(sys.argv) == 2 and sys.argv[1] == "--list":
        print(json.dumps(inventory, indent=2))
    elif len(sys.argv) == 2 and sys.argv[1] == "--host":
        print(json.dumps({}))

if __name__ == "__main__":
    main()
