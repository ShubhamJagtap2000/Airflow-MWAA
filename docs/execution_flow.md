# How Tasks Are Executed?

Let, you have one node with the components web server, meta database, scheduler, and executor.

First you create a new DAG, dag.py and put that folder DAGS, now as coded the scheduler parses this folder DAGS every 5 minutes by default to detect new dags.

When you apply modification to that DAG, you may need to wait up to 30 seconds before getting your modification

Next, the scheduler runs the dags and for that it creates a DagRun object with the state `'running'`

Then it takes 1st task to execute and it becomes a *TaskInstance* object

The TaskInstance object has the state `'None'` and then scheduled

After that the scheduler sends the TaskInstance into the queue of the executor

Now the state of the task is `'queued'` and the executor creates a subprocess to run the task and TaskInstance object is 'running'

Once the task is done the state of the task is `'success'` ot `'failed'`

![image](https://user-images.githubusercontent.com/63872951/201462607-e4c9a901-d8d7-42a3-b2b7-6bf5fac80355.png)

![image](https://user-images.githubusercontent.com/63872951/201462670-df9ab936-d1f9-4a6e-ba57-b32b7340abdf.png)
