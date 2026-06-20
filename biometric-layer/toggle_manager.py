import yaml

def is_feature_enabled(feature_name):
    with open("omni_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    # Check master toggle AND specific feature toggle
    master = config['security_and_identity']['biometrics_enabled']
    feature = config['security_and_identity'].get(f"{feature_name}_enabled", False)
    
    return master and feature
  
