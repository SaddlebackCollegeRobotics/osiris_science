import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool


class IRCameraClient(Node):
    """
    Subclass of ROS2 Node class. Receives and displays video feed from camera.
    """
    def __init__(self):
        """
        Class constructor to set up the node
        """
        # initiate the Node class's constructor and give it a name
        super().__init__('ir_camera_client')
        # create client to control camera
        self.cli = self.create_client(SetBool, '/osiris/science/ir_camera/cmd')

    def send_request(self, status):
        """
        ROS2 request function. Sends request command via ROS2 service.
        :param status: Device to be requested by service
        """
        request = SetBool.Request()
        request.data = status
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.future = self.cli.call_async(request)
        self.get_logger().info('Request sent')

    def run_node(self):
        """
        ROS2 spin function. Allows for activation of node class as external dependency.
        :return done: Indicates if requested service is done.
        :rtype: bool
        """
        rclpy.spin_once(self)
        done = False
        if self.future.done():
            try:
                response = self.future.result()
            except Exception as e:
                self.get_logger().info(f'{e}')
            else:
                self.get_logger().info(f'{response.message}')
            done = True
        return done

    def destroy_node(self):
        """
        Shutdown function. Destroys node explicitly.
        """
        self.get_logger().info('Shutting down node')
        super().destroy_node()


def main(args=None):
    """
    Main function. Initializes and spins ROS2 node. Ask user to enter boolean value to simulate GUI control
    :param args: ROS2 command line arguments
    """
    rclpy.init(args=args)
    ir_camera_client = IRCameraClient()
    proceed = 'proceed'
    try:
        while proceed != '':
            height = int(input('Enter 1 to turn the IR camera on, or 0 to turn it off: '))
            while height < 0 or height > 1:
                height = int(input('Enter 1 to turn the IR camera on, or 0 to turn it off: '))
            ir_camera_client.send_request(height)
            while rclpy.ok():
                done = ir_camera_client.run_node()
                if done:
                    break
            proceed = input('\nEnter any character(s) to continue sending IR camera commands: ')
    except Exception as e:
        ir_camera_client.get_logger().info(f'{e})')
    except KeyboardInterrupt:
        print('\n')
    ir_camera_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()