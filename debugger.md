**To open the debugger in the interactive shell, click Debug-->Debugger**<br/>
-In IDLE, open any .py file<br/>
-Be sure to select the Stack, Locals, Source, and Globals checkboxes. <br/>
-Now when you attempt to run a program and click F5, the program will run under the debugger. <br/>
-You can stpe through the program now and work through it line by line to see exactly what's going on. <br/>

**Three types of errors**<br/>
(1) Syntax: from typos.<br/>
(2) Runtime: occur when the programs is running. Program will work up until this point and then will crash.<br/>
(3) Semantic: probably the most tricky to find. They don't crash the program, but will prevent it from doing what you intended it to do. <br/>

Infinite loops: just press `control-C`<br/>


**Stepping through a program with debugger:**<br/>
-The debugger allows you to execute one instruction at a time; this process is called 'stepping.'<br/>
-just click the **Step** button.<br/>

**Globals Area**<br/>
-This is just a window that displays all of the global variables used in your script. <br/>
-Remember, a global variable is any variable that's been created outside of a function. <br/>

**Locals Area**<br/>
-Same as above, but will allow you to check the variables built within a function. <br/>

**Stepping INTO, OVER, and OUT**<br/>
-INTO: basically just debugging a script line by line<br/>
-OVER: convenient way of skipping things inside a fuction, like print() that we don't need to waste time examining <br/>
-OUT: causes the debugger to step over as many lines as needed until the execution has returned from the function it's in.
      If you're not inside of a function, clicking `Out` will cause the debugger to execute al of the remaining lines in
      the program.<br/>
      
**Setting Breakpoints**<br/>
-Sometimes running the debugger through every line is too slow, and you want it to focus on a specific area. The way to do this is to set a breakpoint on a line that you want the debugger to take control once the execution reaches this line. <br/>
-right click the line you want, then select `Set Breakpoint`<br/>
-you can do this for as many lines as you'd like. <br/>
-to remove a breakpoint, just click the line and select `Clear Breakpoint` from the menu that appears.<br/>

