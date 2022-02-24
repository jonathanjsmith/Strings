"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
"""

from threading import *

class Jobs:
    
    def __init__(self):
        pass

    def printFirst(self):
        print("first")
        
    def printSecond(self):
        print("second")
        
    def printThird(self):
        print("third")
    
class Foo:
    
    def __init__(self):
        self.job1Done = Lock()
        self.job2Done = Lock()
        self.job1Done.acquire()
        self.job2Done.acquire()
        self.jobs = Jobs()
    
    def first(self):
        self.jobs.printFirst()
        self.job1Done.release()
        
    def second(self):
        with self.job1Done:
            self.jobs.printSecond()
            self.job2Done.release()
        
    def third(self):
        with self.job2Done:
            self.jobs.printThird()
            
class myThread(Thread):
    
    def __init__(self, job, foo):
        Thread.__init__(self)
        self.job = job
        self.foo = foo
        
    def run(self):
        switch = {1: self.foo.first, 2: self.foo.second, 3: self.foo.third}
        switch[self.job]()
            
"""
Time: O(1)
Space: O(1)
"""

foo = Foo()
order = [3,1,2]
for x in order:
    t = myThread(x, foo)
    t.start()
