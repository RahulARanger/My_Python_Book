import sys
import os

sys.path.remove(__file__) if __file__ in sys.path else None
sys.path.append((os.path.dirname(os.path.dirname(__file__))))

from LinkedList.linked_list import DoubleNode