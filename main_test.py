import asyncio
import sys, os
import fuckit
fuckit('checktz')
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

  
def test_time():
  assert checktz.GetTime("test") == "Finished with no errors!"
  
