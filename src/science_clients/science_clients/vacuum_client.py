from template_clients import *

def main():
    boot(ServiceClient(subsystem='science', component_name='vacuum'))
    
if __name__ == '__main__':
    main()
