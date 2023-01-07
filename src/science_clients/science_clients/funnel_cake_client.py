from science_clients.template_clients import *

def main():
    rclpy.init()
    boot(ActionClient(subsystem='science', component_name='funnel_cake', max_position=200))
    
if __name__ == '__main__':
    main()
    