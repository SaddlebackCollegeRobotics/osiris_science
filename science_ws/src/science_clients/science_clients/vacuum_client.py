import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class VacuumClient(Node):
    """
    Subclass of ROS2 Node. Issues control commands to vacuum component.
    """
    def __init__(self):
        """
        Class constructor to set up the node
        """
        super().__init__('vacuum_client')
        self.client = self.create_client(SetBool, '/osiris/science/vacuum/cmd')
        self.request = SetBool.Request()

    def send_request(self, state):
        """
        ROS2 request function. Sends request command via ROS2 service.
        :param state: Device to be requested by service
        """
        self.request.data = state
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Vacuum service not available, waiting again...')
        self.future = self.client.call_async(self.request)
        self.get_logger().info('Request sent')

    def run(self):
        """
        ROS2 spin function. Allows for activation of node class as external dependency.
        :return done: Indicates if requested service is done.
        :rtype: bool
        """
        while rclpy.ok():
            rclpy.spin_once(self)
            if self.future.done():
                try:
                    response = self.future.result()
                except Exception as e:
                    self.get_logger().info(f'{e}')
                else:
                    self.get_logger().info(f'Result of /osiris/science/vacuum/cmd:' +
                                           f'\n\tstate - {self.request.data}' +
                                           f'\n\tsuccess - {response.success}' +
                                           f'\n\tmessage - {response.message}')
                break


def main(args=None):
    """
    Main function. Initializes and spins ROS2 node. Ask user to enter boolean value to simulate GUI control
    :param args: ROS2 command line arguments
    """
    rclpy.init(args=args)
    vacuum_client = VacuumClient()
    proceed = 'proceed'
    try:
        while proceed != '':
            state = input('Enter 1 to turn the vacuum on, or 0 to turn it off: ')
            while state != '0' or state != '1':
                state = input('Enter 1 to turn the vacuum on, or 0 to turn it off: ')
            vacuum_client.send_request(bool(state))
            vacuum_client.run()
            proceed = input('\nEnter any character(s) to continue sending vacuum commands: ')
    except Exception as e:
        vacuum_client.get_logger().info(f'{e})')
    except KeyboardInterrupt:
        print('\n')
    finally:
        vacuum_client.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()