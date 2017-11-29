import asyncio
import sys, os
import fuckit
fuckit('status')
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

  
def test_status():
  assert status.GetStatus("test") == "Test passed"
  
