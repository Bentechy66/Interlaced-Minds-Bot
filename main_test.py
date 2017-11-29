import points
import asyncio
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

  
def test_points():
  assert points.AddR() == "Finished with no errors!"
