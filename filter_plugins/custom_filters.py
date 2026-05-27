def mask_ip(ip):
    if not ip:
        return "unknown"
    parts = ip.split('.')
    if len(parts) == 4:
        return parts[0] + '.' + parts[1] + '.***.***'
    return ip

def format_env(env):
    if env == 'staging':
        return 'STAGING'
    elif env == 'production':
        return 'PRODUCTION'
    return env.upper()

class FilterModule:
    def filters(self):
        return {
            'mask_ip': mask_ip,
            'format_env': format_env,
        }
