import requests

__version__ = "0.0.3"

def get_latest_version():
    package_name="fileosninja"
    url = f"https://pypi.org/pypi/{package_name}/json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        package_data = response.json()
        latest_version = package_data['info']['version']
        return latest_version
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None