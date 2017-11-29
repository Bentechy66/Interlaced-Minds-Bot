import points
import asyncio

  
def test_points():
  assert await points.AddR() == "Finished with no errors!"
