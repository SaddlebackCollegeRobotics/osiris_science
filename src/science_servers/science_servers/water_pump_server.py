from template_servers import *

def main():
    boot(GPIOServer(subsystem='science', component_name='water_pump', pin=14))

if __name__ == '__main__':
    main()
