import template_clients.service_client as service_client

def main():
    service_client.boot(subsystem='science', component_name='uv_light')
    
if __name__ == '__main__':
    main()
