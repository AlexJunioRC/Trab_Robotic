import rospy
from std_msgs.msg import String
    
rospy.init_node('Trabalho')

def subCallBack(msg):
    global soma
    soma = msg
    
def timerCallBack(event):
    msg = String()
    msg.data = '2017004555'
    pub.publish(msg)
    mat = int (msg.data)
    print (mat)
    
    
sub = rospy.Subscriber('/Soma',String,subCallBack)   
    
pub = rospy.Publisher ('/topic1', String, queue_size =1)
timer = rospy.Timer(rospy.Duration(0.1),timerCallBack)
    
rospy.spin()